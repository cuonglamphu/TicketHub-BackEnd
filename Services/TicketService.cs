using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;
using Microsoft.EntityFrameworkCore;
using Type = TicketHub_BackEnd.Models.Type;

namespace TicketHub_BackEnd.Services
{
    public class TicketService : ITicketService
    {
        private readonly AppDbContext _context;

        public TicketService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Ticket>> GetAllTickets()
        {
            return await _context.Tickets
                .ToListAsync();
        }

        public async Task<Ticket?> GetTicketById(int id)
        {
            return await _context.Tickets.FindAsync(id);

        }

        public async Task<IEnumerable<Ticket>> GetTicketsByEvent(int eventId)
        {
            return await _context.Tickets
                .Where(t => t.EveId == eventId)
                .ToListAsync();
        }

        public async Task<Ticket> CreateTicket(CreateTicketDto dto)
        {
            var ticket = new Ticket
            {

                TicketPrice = dto.TicketPrice,
                TicketQty = dto.TicketQty,
                EveId = dto.EveId,
                TypeId = dto.TypeId
            };

            _context.Tickets.Add(ticket);
            await _context.SaveChangesAsync();

            return ticket;
        }

        public async Task<Ticket> DeleteTicket(int id)
        {
            var ticket = await _context.Tickets.FindAsync(id);
            if (ticket == null)
                throw new KeyNotFoundException($"Ticket with ID {id} not found");

            _context.Tickets.Remove(ticket);
            await _context.SaveChangesAsync();
            return ticket;
        }

        public async Task<Ticket> UpdateTicket(int id, UpdateTicketDto dto)
        {
            var ticket = await _context.Tickets.FindAsync(id);
            if (ticket == null)
            {
                throw new KeyNotFoundException($"Ticket with ID {id} not found");
            }
            return ticket;
        }

        public async Task<PurchaseResponseDto> PurchaseTicket(int userId, CreatePurchaseDto purchase)
        {
            using var transaction = await _context.Database.BeginTransactionAsync();
            try
            {
                var ticket = await _context.Tickets
                    .Include(t => t.Event)
                    .Include(t => t.Type)
                    .FirstOrDefaultAsync(t => t.TicketId == purchase.TicketId);

                if (ticket == null)
                    throw new KeyNotFoundException($"Ticket with ID {purchase.TicketId} not found");

                // Kiểm tra số lượng vé còn đủ không
                if (ticket.TicketQty < purchase.Quantity)
                    throw new InvalidOperationException($"Không đủ vé! Chỉ còn {ticket.TicketQty} vé cho sự kiện {ticket.Event?.EveName}");

                var user = await _context.Users.FindAsync(userId);
                if (user == null)
                    throw new KeyNotFoundException($"User with ID {userId} not found");

                decimal total = ticket.TicketPrice * purchase.Quantity;

                var sale = new Sale
                {
                    UserId = userId,
                    SaleDate = DateTime.UtcNow,
                    SaleTotal = total,
                    BrowserInfo = purchase.BrowserInfo,
                    DeviceInfo = purchase.DeviceInfo,
                    IpAddress = purchase.IpAddress
                };

                _context.Sales.Add(sale);
                await _context.SaveChangesAsync();

                // Create purchase record
                var purchaseRecord = new Purchase
                {
                    TicketId = purchase.TicketId,
                    SaleId = sale.SaleId,
                    Quantity = purchase.Quantity
                };

                _context.Purchases.Add(purchaseRecord);

                // Trừ số lượng vé
                ticket.TicketQty = ticket.TicketQty - purchase.Quantity;
                _context.Tickets.Update(ticket); // Đảm bảo cập nhật ticket

                // Log để debug
                Console.WriteLine($"Số lượng vé còn lại sau khi mua: {ticket.TicketQty}");

                await _context.SaveChangesAsync();
                await transaction.CommitAsync();

                // Return purchase response with full details
                return new PurchaseResponseDto
                {
                    SaleId = sale.SaleId,
                    SaleTotal = sale.SaleTotal,
                    SaleDate = sale.SaleDate,
                    Purchases = new List<PurchaseDetailDto>
                    {
                        new PurchaseDetailDto
                        {
                            TicketId = ticket.TicketId,
                            EventName = ticket.Event?.EveName ?? "Unknown Event",
                            EventCity = ticket.Event?.EveCity ?? "Unknown City",
                            EventTimeStart = ticket.Event?.EveTimestart ?? DateTime.MinValue,
                            EventThumb = ticket.Event?.EveThumb ?? "",
                            TicketType = ticket.Type?.TypeName ?? "Unknown Type",
                            Quantity = purchase.Quantity,
                            Price = ticket.TicketPrice,
                            Total = total
                        }
                    }
                };
            }
            catch (Exception ex)
            {
                await transaction.RollbackAsync();
                // Log lỗi để debug
                Console.WriteLine($"Error during purchase: {ex.Message}");
                throw;
            }
        }
    }
}