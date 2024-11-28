using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public class PurchaseService : IPurchaseService
    {
        private readonly AppDbContext _context;

        public PurchaseService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<PurchaseResponseDto>> GetUserPurchases(int userId)
        {
            var sales = await _context.Sales
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t != null ? t.Event : null)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t != null ? t.Type : null)
                .Where(s => s.UserId == userId)
                .OrderByDescending(s => s.SaleDate)
                .ToListAsync();

            return sales.Select(sale => new PurchaseResponseDto
            {
                SaleId = sale.SaleId,
                SaleTotal = sale.SaleTotal,
                SaleDate = sale.SaleDate,
                Purchases = sale.Purchases?.Select(p => new PurchaseDetailDto
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
                }).ToList() ?? new List<PurchaseDetailDto>()
            }).ToList();
        }
    }
}
