using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Models;

namespace TicketHub_BackEnd.Services
{
    public class SaleService : ISaleService
    {
        private readonly AppDbContext _context;
        private readonly ILogger<SaleService> _logger;

        public SaleService(AppDbContext context, ILogger<SaleService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public async Task<IEnumerable<SaleResponseDto>> GetAllSales()
        {
            return await _context.Sales
                .Include(s => s.User)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t.Event)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t.Type)
                .OrderByDescending(s => s.SaleDate)
                .Select(s => new SaleResponseDto
                {
                    SaleId = s.SaleId,
                    UserId = s.UserId,
                    UserName = $"{s.User.FirstName} {s.User.LastName}",
                    UserEmail = s.User.UserEmail,
                    SaleDate = s.SaleDate,
                    SaleTotal = s.SaleTotal,
                    Purchases = s.Purchases.Select(p => new PurchaseDetailDto
                    {
                        TicketId = p.TicketId,
                        EventName = p.Ticket.Event.EveName,
                        EventCity = p.Ticket.Event.EveCity,
                        EventTimeStart = p.Ticket.Event.EveTimestart,
                        EventThumb = p.Ticket.Event.EveThumb,
                        TicketType = p.Ticket.Type.TypeName,
                        Quantity = p.Quantity,
                        Price = p.Ticket.TicketPrice,
                        Total = p.Quantity * p.Ticket.TicketPrice
                    }).ToList()
                })
                .ToListAsync();
        }

        public async Task<SaleResponseDto?> GetSaleById(int id)
        {
            return await _context.Sales
                .Include(s => s.User)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t.Event)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t.Type)
                .Where(s => s.SaleId == id)
                .Select(s => new SaleResponseDto
                {
                    SaleId = s.SaleId,
                    UserId = s.UserId,
                    UserName = $"{s.User.FirstName} {s.User.LastName}",
                    UserEmail = s.User.UserEmail,
                    SaleDate = s.SaleDate,
                    SaleTotal = s.SaleTotal,
                    Purchases = s.Purchases.Select(p => new PurchaseDetailDto
                    {
                        TicketId = p.TicketId,
                        EventName = p.Ticket.Event.EveName,
                        EventCity = p.Ticket.Event.EveCity,
                        EventTimeStart = p.Ticket.Event.EveTimestart,
                        EventThumb = p.Ticket.Event.EveThumb,
                        TicketType = p.Ticket.Type.TypeName,
                        Quantity = p.Quantity,
                        Price = p.Ticket.TicketPrice,
                        Total = p.Quantity * p.Ticket.TicketPrice
                    }).ToList()
                })
                .FirstOrDefaultAsync();
        }

        public async Task<IEnumerable<SaleResponseDto>> GetUserSales(int userId)
        {
            return await _context.Sales
                .Include(s => s.User)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t.Event)
                .Include(s => s.Purchases)
                    .ThenInclude(p => p.Ticket)
                        .ThenInclude(t => t.Type)
                .Where(s => s.UserId == userId)
                .OrderByDescending(s => s.SaleDate)
                .Select(s => new SaleResponseDto
                {
                    SaleId = s.SaleId,
                    UserId = s.UserId,
                    UserName = $"{s.User.FirstName} {s.User.LastName}",
                    UserEmail = s.User.UserEmail,
                    SaleDate = s.SaleDate,
                    SaleTotal = s.SaleTotal,
                    Purchases = s.Purchases.Select(p => new PurchaseDetailDto
                    {
                        TicketId = p.TicketId,
                        EventName = p.Ticket.Event.EveName,
                        EventCity = p.Ticket.Event.EveCity,
                        EventTimeStart = p.Ticket.Event.EveTimestart,
                        EventThumb = p.Ticket.Event.EveThumb,
                        TicketType = p.Ticket.Type.TypeName,
                        Quantity = p.Quantity,
                        Price = p.Ticket.TicketPrice,
                        Total = p.Quantity * p.Ticket.TicketPrice
                    }).ToList()
                })
                .ToListAsync();
        }
    }
}