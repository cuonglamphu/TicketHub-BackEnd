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
                // Get ticket and validate availability
                var ticket = await _context.Tickets
                    .FirstOrDefaultAsync(t => t.TicketId == purchase.TicketId);

                if (ticket == null)
                    throw new KeyNotFoundException($"Ticket with ID {purchase.TicketId} not found");

                if (ticket.TicketQty < purchase.Quantity)
                    throw new InvalidOperationException("Not enough tickets available");

                // Create new sale
                var sale = new Sale
                {
                    UserId = userId,
                    SaleDate = DateTime.UtcNow,
                    SaleTotal = ticket.TicketPrice * purchase.Quantity
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

                // Update ticket quantity
                ticket.TicketQty -= purchase.Quantity;

                await _context.SaveChangesAsync();
                await transaction.CommitAsync();

                // Return purchase response
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
                            Quantity = purchase.Quantity,
                            Price = ticket.TicketPrice,
                            Total = sale.SaleTotal
                        }
                    }
                };
            }
            catch (Exception)
            {
                await transaction.RollbackAsync();
                throw;
            }
        }
    }
}