using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public interface IEventService
    {
        Task<IEnumerable<Event>> GetAllEvents();
        Task<Event?> GetEventById(int id);
        Task<IEnumerable<Event>> GetEventsByCategory(int catId);
        Task<Event> CreateEvent(CreateEventDto dto);
        Task<bool> UpdateEvent(int id, UpdateEventDto dto);
        Task<bool> DeleteEvent(int id);
    }
}