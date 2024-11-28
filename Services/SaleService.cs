using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public class SaleService : ISaleService
    {
        private readonly AppDbContext _context;

        public SaleService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<SaleResponseDto>> GetAllSales()
        {
            var sales = await _context.Sales
                .Include(s => s.User)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket != null ? p.Ticket : null)
                        .ThenInclude(t => t != null ? t.Event : null)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket != null ? p.Ticket : null)
                        .ThenInclude(t => t != null ? t.Type : null)
                .OrderByDescending(s => s.SaleDate)
                .ToListAsync();

            return sales.Select(s => new SaleResponseDto
            {
                SaleId = s.SaleId,
                UserId = s.UserId,
                UserName = s.User != null ? $"{s.User.FirstName} {s.User.LastName}" : "Unknown User",
                UserEmail = s.User != null ? s.User.UserEmail : "Unknown Email",
                SaleDate = s.SaleDate,
                SaleTotal = s.SaleTotal,
                Purchases = s.Purchases.Select(p => new PurchaseDetailDto
                {
                    TicketId = p.TicketId,
                    EventName = p.Ticket != null && p.Ticket.Event != null ? p.Ticket.Event.EveName : "Unknown Event",
                    EventCity = p.Ticket != null && p.Ticket.Event != null ? p.Ticket.Event.EveCity : "Unknown City",
                    EventTimeStart = p.Ticket != null && p.Ticket.Event != null ? p.Ticket.Event.EveTimestart : DateTime.MinValue,
                    EventThumb = p.Ticket != null && p.Ticket.Event != null ? p.Ticket.Event.EveThumb : "",
                    TicketType = p.Ticket != null && p.Ticket.Type != null ? p.Ticket.Type.TypeName : "Unknown Type",
                    Quantity = p.Quantity,
                    Price = p.Ticket != null ? p.Ticket.TicketPrice : 0,
                    Total = p.Quantity * (p.Ticket != null ? p.Ticket.TicketPrice : 0)
                }).ToList()
            }).ToList();
        }

        public async Task<SaleResponseDto?> GetSaleById(int id)
        {
            var sale = await _context.Sales
                .Include(s => s.User)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket != null ? p.Ticket : null)
                        .ThenInclude(t => t != null ? t.Event : null)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket != null ? p.Ticket : null)
                        .ThenInclude(t => t != null ? t.Type : null)
                .FirstOrDefaultAsync(s => s.SaleId == id);

            if (sale == null)
                return null;

            return new SaleResponseDto
            {
                SaleId = sale.SaleId,
                UserId = sale.UserId,
                UserName = sale.User != null ? $"{sale.User.FirstName} {sale.User.LastName}" : "Unknown User",
                UserEmail = sale.User?.UserEmail ?? "Unknown Email",
                SaleDate = sale.SaleDate,
                SaleTotal = sale.SaleTotal,
                Purchases = sale.Purchases.Select(p => new PurchaseDetailDto
                {
                    TicketId = p.TicketId,
                    EventName = p.Ticket?.Event?.EveName ?? "Unknown Event",
                    EventCity = p.Ticket?.Event?.EveCity ?? "Unknown City",
                    EventTimeStart = p.Ticket?.Event?.EveTimestart ?? DateTime.MinValue,
                    EventThumb = p.Ticket?.Event?.EveThumb ?? "",
                    TicketType = p.Ticket?.Type?.TypeName ?? "Unknown Type",
                    Quantity = p.Quantity,
                    Price = p.Ticket?.TicketPrice ?? 0,
                    Total = p.Quantity * (p.Ticket?.TicketPrice ?? 0)
                }).ToList()
            };
        }

        public async Task<IEnumerable<SaleResponseDto>> GetUserSales(int userId)
        {
            var sales = await _context.Sales
                .Include(s => s.User)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket != null ? p.Ticket : null)
                        .ThenInclude(t => t != null ? t.Event : null)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket != null ? p.Ticket : null)
                        .ThenInclude(t => t != null ? t.Type : null)
                .Where(s => s.UserId == userId)
                .OrderByDescending(s => s.SaleDate)
                .ToListAsync();

            return sales.Select(s => new SaleResponseDto
            {
                SaleId = s.SaleId,
                UserId = s.UserId,
                UserName = s.User != null ? $"{s.User.FirstName} {s.User.LastName}" : "Unknown User",
                UserEmail = s.User?.UserEmail ?? "Unknown Email",
                SaleDate = s.SaleDate,
                SaleTotal = s.SaleTotal,
                Purchases = s.Purchases.Select(p => new PurchaseDetailDto
                {
                    TicketId = p.TicketId,
                    EventName = p.Ticket?.Event?.EveName ?? "Unknown Event",
                    EventCity = p.Ticket?.Event?.EveCity ?? "Unknown City",
                    EventTimeStart = p.Ticket?.Event?.EveTimestart ?? DateTime.MinValue,
                    EventThumb = p.Ticket?.Event?.EveThumb ?? "",
                    TicketType = p.Ticket?.Type?.TypeName ?? "Unknown Type",
                    Quantity = p.Quantity,
                    Price = p.Ticket?.TicketPrice ?? 0,
                    Total = p.Quantity * (p.Ticket?.TicketPrice ?? 0)
                }).ToList()
            }).ToList();
        }
    }
}