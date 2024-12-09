using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public interface IFraudDetectionService
    {
        Task<bool> IsFraudulentAsync(int userId, CreatePurchaseDto purchase);
    }
}