using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public interface ITicketService
    {
        Task<IEnumerable<Ticket>> GetAllTickets();
        Task<Ticket?> GetTicketById(int id);
        Task<IEnumerable<Ticket>> GetTicketsByEvent(int eventId);
        Task<Ticket> CreateTicket(CreateTicketDto dto);

        Task<Ticket> DeleteTicket(int id);
        Task<Ticket> UpdateTicket(int id, UpdateTicketDto dto);         
        // Task<Sale> PurchaseTicket(int userId, PurchaseTicketDto dto);
        Task<PurchaseResponseDto> PurchaseTicket(int userId, CreatePurchaseDto purchase);
    }
}