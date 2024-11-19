using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Models;

namespace TicketHub_BackEnd.Services
{
    public interface ICategoryService
    {
        Task<IEnumerable<Category>> GetAllCategories();
        Task<Category?> GetCategoryById(int id);
        Task<Category> CreateCategory(CreateCategoryDto dto);
        Task<bool> UpdateCategory(int id, UpdateCategoryDto dto);
        Task<bool> DeleteCategory(int id);
    }
}