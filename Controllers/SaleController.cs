using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.DTOs;
using TicketHub_BackEnd.Services;

namespace TicketHub_BackEnd.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SaleController : ControllerBase
    {
        private readonly ISaleService _saleService;
        private readonly ILogger<SaleController> _logger;

        public SaleController(ISaleService saleService, ILogger<SaleController> logger)
        {
            _saleService = saleService;
            _logger = logger;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<SaleResponseDto>>> GetAllSales()
        {
            try
            {
                var sales = await _saleService.GetAllSales();
                return Ok(sales);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error retrieving all sales");
                return StatusCode(500, "Internal server error while retrieving sales");
            }
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<SaleResponseDto>> GetSaleById(int id)
        {
            try
            {
                var sale = await _saleService.GetSaleById(id);
                if (sale == null)
                {
                    return NotFound($"Sale with ID {id} not found");
                }
                return Ok(sale);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error retrieving sale {SaleId}", id);
                return StatusCode(500, "Internal server error while retrieving sale");
            }
        }

        [HttpGet("user/{userId}")]
        public async Task<ActionResult<IEnumerable<SaleResponseDto>>> GetUserSales(int userId)
        {
            try
            {
                var sales = await _saleService.GetUserSales(userId);
                return Ok(sales);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error retrieving sales for user {UserId}", userId);
                return StatusCode(500, "Internal server error while retrieving user sales");
            }
        }
    }
}