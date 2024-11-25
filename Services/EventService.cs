using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Services;
using Microsoft.EntityFrameworkCore.Query.SqlExpressions;

namespace TicketHub_BackEnd.Services
{
    public class EventService : IEventService
    {
        private readonly AppDbContext _context;

        public EventService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Event>> GetAllEvents()
        {
            return await _context.Events
                .Include(e => e.Category)
                .ToListAsync();
        }

        public async Task<Event?> GetEventById(int id)
        {
            return await _context.Events
                .Include(e => e.Category)
                .FirstOrDefaultAsync(e => e.EveId == id);
        }

        public async Task<IEnumerable<Event>> GetEventsByCategory(int catId)
        {
            return await _context.Events
                .Include(e => e.Category)
                .Where(e => e.CatId == catId)
                .ToListAsync();
        }

        public async Task<Event> CreateEvent(CreateEventDto dto)
        {
            var @event = new Event
            {
                EveName = dto.EveName,
                EveDesc = dto.EveDesc,
                EveCity = dto.EveCity,
                EveTimestart = dto.EveTimestart,
                EveTimeend = dto.EveTimeend,
                EveThumb = dto.EveThumb,
                CatId = dto.CatId
            };

            _context.Events.Add(@event);
            await _context.SaveChangesAsync();

            return @event;
        }

        public async Task<bool> UpdateEvent(int id, UpdateEventDto dto)
        {
            var @event = await _context.Events.FindAsync(id);
            if (@event == null)
                return false;

            @event.EveName = dto.EveName;
            @event.EveDesc = dto.EveDesc;
            @event.EveCity = dto.EveCity;
            @event.EveTimestart = dto.EveTimestart;
            @event.EveTimeend = dto.EveTimeend;
            @event.EveThumb = dto.EveThumb;
            @event.CatId = dto.CatId;

            try
            {
                await _context.SaveChangesAsync();
                return true;
            }
            catch (DbUpdateConcurrencyException)
            {
                return false;
            }
        }

        public async Task<bool> DeleteEvent(int id)
        {
            var @event = await _context.Events.FindAsync(id);
            if (@event == null)
                return false;

            _context.Events.Remove(@event);
            await _context.SaveChangesAsync();
            return true;
        }

        public async Task<IEnumerable<Event>> GetHotEvents()
        {
            var now = DateTime.Now;

            // Debug: Kiểm tra số lượng events tổng cộng
            var totalEvents = await _context.Events.CountAsync();
            Console.WriteLine($"Total events: {totalEvents}");

            // Lấy tất cả các sự kiện sắp diễn ra và include Category
            var eventsWithTickets = await _context.Events
                .Include(e => e.Category)
                .Include(e => e.Tickets)
                .Where(e => e.EveTimestart > now)  // Chỉ lấy sự kiện chưa diễn ra
                .Select(e => new
                {
                    Event = e,
                    TicketCount = e.Tickets.Count(),
                    DaysUntilEvent = (int)(e.EveTimestart - now).TotalDays
                })
                .ToListAsync();

            // Debug: Kiểm tra số lượng events sắp diễn ra
            Console.WriteLine($"Upcoming events: {eventsWithTickets.Count}");

            // Nếu không có sự kiện nào sắp diễn ra, lấy 5 sự kiện gần nhất
            if (!eventsWithTickets.Any())
            {
                return await _context.Events
                    .Include(e => e.Category)
                    .OrderByDescending(e => e.EveTimestart)
                    .Take(6)
                    .ToListAsync();
            }

            var result = eventsWithTickets
                .Select(e => new
                {
                    Event = e.Event,
                    Score = (e.TicketCount * 0.4) +
                           (1.0 / (Math.Abs(e.DaysUntilEvent) + 1) * 0.6)
                })
                .OrderByDescending(x => x.Score)
                .Take(6)
                .Select(x => x.Event)
                .ToList();

            // Debug: Kiểm tra số lượng kết quả cuối cùng
            Console.WriteLine($"Final results: {result.Count}");

            return result;
        }

        // Thêm các class để lưu trữ preferences
        private class CategoryPreference
        {
            public int CategoryId { get; set; }
            public double Weight { get; set; }
            public DateTime RecentPurchase { get; set; }
        }

        private class CityPreference
        {
            public string City { get; set; }
            public double Weight { get; set; }
        }

        public async Task<IEnumerable<Event>> GetRecommendedEvents(int userId)
        {

            var now = DateTime.UtcNow;

            // Lấy lịch sử mua vé của user với thông tin chi tiết
            var userPurchaseHistory = await _context.Sales
                .Where(s => s.UserId == userId)
                .SelectMany(s => s.Purchases)
                .Select(p => new
                {
                    CategoryId = p.Ticket.Event.CatId,
                    City = p.Ticket.Event.EveCity,
                    EventTime = p.Ticket.Event.EveTimestart,
                    PurchaseDate = p.Sale.SaleDate
                })
                .ToListAsync();

            if (!userPurchaseHistory.Any())
            {
                return await GetHotEvents();
            }

            // Phân tích thói quen người dùng
            var categoryPreferences = userPurchaseHistory
                .GroupBy(h => h.CategoryId)
                .Select(g => new CategoryPreference
                {
                    CategoryId = g.Key,
                    Weight = g.Count() * (1.0 / userPurchaseHistory.Count),
                    RecentPurchase = g.Max(x => x.PurchaseDate)
                })
                .ToList();

            var cityPreferences = userPurchaseHistory
                .GroupBy(h => h.City)
                .Select(g => new CityPreference
                {
                    City = g.Key,
                    Weight = g.Count() * (1.0 / userPurchaseHistory.Count)
                })
                .ToList();

            // Phân tích thời gian tham gia sự kiện ưa thích
            var preferredEventTimes = userPurchaseHistory
                .Select(h => h.EventTime.TimeOfDay)
                .ToList();
            var avgPreferredTime = new TimeSpan(
                (long)preferredEventTimes.Average(t => t.Ticks)
            );

            // Lấy các sự kiện sắp diễn ra
            var upcomingEvents = await _context.Events
                .Include(e => e.Category)
                .Where(e => e.EveTimestart > now)
                .Select(e => new
                {
                    Event = e,
                    DaysUntil = EF.Functions.DateDiffDay(now, e.EveTimestart)
                })
                .ToListAsync();

            // Tính điểm chi tiết cho mỗi sự kiện
            var scoredEvents = upcomingEvents
                .Select(e => new
                {
                    Event = e.Event,
                    Score = CalculateEventScore(
                        e.Event,
                        e.DaysUntil,
                        categoryPreferences,
                        cityPreferences,
                        avgPreferredTime
                    )
                })
                .OrderByDescending(x => x.Score)
                .Take(6)
                .Select(x => x.Event)
                .ToList();

            return scoredEvents.Any() ? scoredEvents : await GetHotEvents();
        }

        private double CalculateEventScore(
            Event evt,
            int daysUntil,
            List<CategoryPreference> categoryPreferences,
            List<CityPreference> cityPreferences,
            TimeSpan avgPreferredTime)
        {
            // 1. Category Score (35%)
            var categoryScore = categoryPreferences
                .Where(c => c.CategoryId == evt.CatId)
                .Select(c => c.Weight * (1 +
                    Math.Exp(-0.1 * (DateTime.UtcNow - c.RecentPurchase).TotalDays)))
                .FirstOrDefault();

            // 2. City Score (25%)
            var cityScore = cityPreferences
                .Where(c => c.City == evt.EveCity)
                .Select(c => c.Weight)
                .FirstOrDefault();

            // 3. Time Preference Score (20%)
            var timeScore = 1.0 - (Math.Abs((evt.EveTimestart.TimeOfDay - avgPreferredTime).TotalHours) / 24.0);

            // 4. Proximity Score (20%)
            var proximityScore = 1.0 / (Math.Abs(daysUntil) + 1);

            return (categoryScore * 0.35) +
                   (cityScore * 0.25) +
                   (timeScore * 0.20) +
                   (proximityScore * 0.20);
        }

        public async Task<IEnumerable<Event>> SearchEvents(string keyword, int catId, string city, DateTime startDate)
        {
            return await _context.Events
                .Where(e => e.EveName.Contains(keyword) || e.EveDesc.Contains(keyword))
                .ToListAsync();
        }
    }
}