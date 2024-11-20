using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Services;

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
    }
}