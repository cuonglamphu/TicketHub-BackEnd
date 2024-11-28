using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.Services;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Data;
namespace TicketHub_BackEnd.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PurchaseController : ControllerBase
    {
        private readonly IPurchaseService _purchaseService;
        private readonly AppDbContext _context;

        public PurchaseController(IPurchaseService purchaseService, AppDbContext context)
        {
            _purchaseService = purchaseService;
            _context = context;
        }

        // GET: api/purchase/user/{userId}
        [HttpGet("user/{userId}")]
        public async Task<ActionResult<IEnumerable<PurchaseResponseDto>>> GetUserPurchases(int userId)
        {
            try
            {
                var user = await _context.Users.FindAsync(userId);
                if (user == null)
                {
                    return NotFound($"User with ID {userId} not found");
                }

                var purchases = await _purchaseService.GetUserPurchases(userId);
                return Ok(purchases);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }
    }
}