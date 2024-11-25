using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.Services;

namespace TicketHub_BackEnd.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class StatisticsController : ControllerBase
    {
        private readonly IStatisticsService _statisticsService;
        private readonly ILogger<StatisticsController> _logger;

        public StatisticsController(IStatisticsService statisticsService, ILogger<StatisticsController> logger)
        {
            _statisticsService = statisticsService;
            _logger = logger;
        }

        [HttpGet]
        public async Task<ActionResult<SalesStatisticsDto>> GetSalesStatistics()
        {
            try
            {
                var statistics = await _statisticsService.GetSalesStatistics();
                return Ok(statistics);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error getting sales statistics");
                return StatusCode(500, "Internal server error while fetching statistics");
            }
        }
    }
}
