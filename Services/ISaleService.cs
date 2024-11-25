using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public interface ISaleService
    {
        Task<IEnumerable<SaleResponseDto>> GetAllSales();
        Task<SaleResponseDto?> GetSaleById(int id);
        Task<IEnumerable<SaleResponseDto>> GetUserSales(int userId);
    }
}