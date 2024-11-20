using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;
namespace TicketHub_BackEnd.Services
{
    public interface IPurchaseService
    {
        Task<PurchaseResponseDto> CreatePurchase(int userId, List<CreatePurchaseDto> purchases);
        Task<IEnumerable<PurchaseResponseDto>> GetUserPurchases(int userId);
        Task<Sale?> GetPurchaseDetails(int saleId);
    }
}