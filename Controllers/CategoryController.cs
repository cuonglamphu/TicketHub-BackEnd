using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.Services;

namespace TicketHub_BackEnd.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class CategoryController : ControllerBase
    {
        private readonly ICategoryService _categoryService;

        public CategoryController(ICategoryService categoryService)
        {
            _categoryService = categoryService;
        }

        // GET: api/Category
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Category>>> GetCategories()
        {
            var categories = await _categoryService.GetAllCategories();
            return Ok(categories);
        }

        // GET: api/Category/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Category>> GetCategory(int id)
        {
            var category = await _categoryService.GetCategoryById(id);
            if (category == null)
            {
                return NotFound();
            }
            return Ok(category);
        }

        // POST: api/Category
        [HttpPost]
        public async Task<ActionResult<Category>> CreateCategory(CreateCategoryDto dto)
        {
            var category = await _categoryService.CreateCategory(dto);
            return CreatedAtAction(nameof(GetCategory), new { id = category.CatId }, category);
        }

        // PUT: api/Category/5
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateCategory(int id, UpdateCategoryDto dto)
        {
            var result = await _categoryService.UpdateCategory(id, dto);
            if (!result)
            {
                return NotFound();
            }
            return NoContent();
        }

        // DELETE: api/Category/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCategory(int id)
        {
            var result = await _categoryService.DeleteCategory(id);
            if (!result)
            {
                return NotFound();
            }
            return NoContent();
        }
    }
}
