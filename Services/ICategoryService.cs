using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Services
{
    public interface ICategoryService
    {
        Task<IEnumerable<CategoryResponseDto>> GetAllCategories();
        Task<CategoryResponseDto?> GetCategoryById(int id);
        Task<CategoryResponseDto?> GetCategoryBySlug(string slug);
        Task<CategoryResponseDto> CreateCategory(CreateCategoryDto dto);
        Task<bool> UpdateCategory(int id, UpdateCategoryDto dto);
        Task<bool> DeleteCategory(int id);
    }
}