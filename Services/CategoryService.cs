using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.Services;

namespace TicketHub_BackEnd.Services
{
    public class CategoryService : ICategoryService
    {
        private readonly AppDbContext _context;

        public CategoryService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Category>> GetAllCategories()
        {
            return await _context.Categories.ToListAsync();
        }

        public async Task<Category?> GetCategoryById(int id)
        {
            return await _context.Categories.FindAsync(id);
        }

        public async Task<Category> CreateCategory(CreateCategoryDto dto)
        {
            var category = new Category
            {
                CatName = dto.CatName,
                CatDesc = dto.CatDesc,
                CatSlug = dto.CatSlug,
                CatThumb = dto.CatThumb
            };

            _context.Categories.Add(category);
            await _context.SaveChangesAsync();
            return category;
        }

        public async Task<bool> UpdateCategory(int id, UpdateCategoryDto dto)
        {
            var category = await _context.Categories.FindAsync(id);
            if (category == null)
                return false;

            category.CatName = dto.CatName;
            category.CatDesc = dto.CatDesc;
            category.CatSlug = dto.CatSlug;
            category.CatThumb = dto.CatThumb;

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

        public async Task<bool> DeleteCategory(int id)
        {
            var category = await _context.Categories.FindAsync(id);
            if (category == null)
                return false;

            _context.Categories.Remove(category);
            await _context.SaveChangesAsync();
            return true;
        }
    }
}
