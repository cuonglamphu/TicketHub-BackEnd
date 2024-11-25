using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Models;

namespace TicketHub_BackEnd.Services
{
    public class CategoryService : ICategoryService
    {
        private readonly AppDbContext _context;

        public CategoryService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<CategoryResponseDto>> GetAllCategories()
        {
            var now = DateTime.UtcNow;
            var futureDate = now.AddDays(14);

            return await _context.Categories
                .Select(c => new CategoryResponseDto
                {
                    CatId = c.CatId,
                    CatName = c.CatName,
                    CatDesc = c.CatDesc,
                    CatSlug = c.CatSlug,
                    CatThumb = c.CatThumb,
                    EventCount = _context.Events.Count(e => e.CatId == c.CatId),
                    UpcomingEventCount = _context.Events.Count(e =>
                        e.CatId == c.CatId &&
                        e.EveTimestart >= now &&
                        e.EveTimestart <= futureDate
                    ),
                    TotalRevenue = _context.Events
                        .Where(e => e.CatId == c.CatId)
                        .Join(
                            _context.Tickets,
                            e => e.EveId,
                            t => t.EveId,
                            (e, t) => t
                        )
                        .Join(
                            _context.Purchases,
                            t => t.TicketId,
                            p => p.TicketId,
                            (t, p) => new { t.TicketPrice, p.Quantity }
                        )
                        .Sum(x => x.TicketPrice * x.Quantity)
                })
                .ToListAsync();
        }

        public async Task<CategoryResponseDto?> GetCategoryById(int id)
        {
            var now = DateTime.UtcNow;
            var futureDate = now.AddDays(14);

            return await _context.Categories
                .Where(c => c.CatId == id)
                .Select(c => new CategoryResponseDto
                {
                    CatId = c.CatId,
                    CatName = c.CatName,
                    CatDesc = c.CatDesc,
                    CatSlug = c.CatSlug,
                    CatThumb = c.CatThumb,
                    EventCount = _context.Events.Count(e => e.CatId == c.CatId),
                    UpcomingEventCount = _context.Events.Count(e =>
                        e.CatId == c.CatId &&
                        e.EveTimestart >= now &&
                        e.EveTimestart <= futureDate
                    ),
                    TotalRevenue = _context.Events
                        .Where(e => e.CatId == c.CatId)
                        .Join(
                            _context.Tickets,
                            e => e.EveId,
                            t => t.EveId,
                            (e, t) => t
                        )
                        .Join(
                            _context.Purchases,
                            t => t.TicketId,
                            p => p.TicketId,
                            (t, p) => new { t.TicketPrice, p.Quantity }
                        )
                        .Sum(x => x.TicketPrice * x.Quantity)
                })
                .FirstOrDefaultAsync();
        }

        public async Task<CategoryResponseDto?> GetCategoryBySlug(string slug)
        {
            var now = DateTime.UtcNow;
            var futureDate = now.AddDays(14);

            return await _context.Categories
                .Where(c => c.CatSlug == slug)
                .Select(c => new CategoryResponseDto
                {
                    CatId = c.CatId,
                    CatName = c.CatName,
                    CatDesc = c.CatDesc,
                    CatSlug = c.CatSlug,
                    CatThumb = c.CatThumb,
                    EventCount = _context.Events.Count(e => e.CatId == c.CatId),
                    UpcomingEventCount = _context.Events.Count(e =>
                        e.CatId == c.CatId &&
                        e.EveTimestart >= now &&
                        e.EveTimestart <= futureDate
                    ),
                    TotalRevenue = _context.Events
                        .Where(e => e.CatId == c.CatId)
                        .Join(
                            _context.Tickets,
                            e => e.EveId,
                            t => t.EveId,
                            (e, t) => t
                        )
                        .Join(
                            _context.Purchases,
                            t => t.TicketId,
                            p => p.TicketId,
                            (t, p) => new { t.TicketPrice, p.Quantity }
                        )
                        .Sum(x => x.TicketPrice * x.Quantity)
                })
                .FirstOrDefaultAsync();
        }

        public async Task<CategoryResponseDto> CreateCategory(CreateCategoryDto dto)
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

            return new CategoryResponseDto
            {
                CatId = category.CatId,
                CatName = category.CatName,
                CatDesc = category.CatDesc,
                CatSlug = category.CatSlug,
                CatThumb = category.CatThumb,
                EventCount = 0,
                UpcomingEventCount = 0,
                TotalRevenue = 0
            };
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
