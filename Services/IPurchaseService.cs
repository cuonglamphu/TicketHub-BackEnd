using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;
namespace TicketHub_BackEnd.Services
{
    public interface IPurchaseService
    {
        Task<IEnumerable<PurchaseResponseDto>> GetUserPurchases(int userId);
    }
}