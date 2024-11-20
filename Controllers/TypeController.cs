using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.Services;
using TypeResponseDto = TicketHub_BackEnd.DTOs.TypeResponseDto;
using CreateTypeDto = TicketHub_BackEnd.Services.CreateTypeDto;
using UpdateTypeDto = TicketHub_BackEnd.Services.UpdateTypeDto;


namespace TicketHub_BackEnd.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TypeController : ControllerBase
    {
        private readonly ITypeService _typeService;
        private readonly ILogger<TypeController> _logger;

        public TypeController(ITypeService typeService, ILogger<TypeController> logger)
        {
            _typeService = typeService;
            _logger = logger;
        }

        // GET: api/type
        [HttpGet]
        public async Task<ActionResult<IEnumerable<TypeResponseDto>>> GetTypes()
        {
            try
            {
                var types = await _typeService.GetAllTypes();
                return Ok(types);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // GET: api/type/5
        [HttpGet("{id}")]
        public async Task<ActionResult<TypeResponseDto>> GetType(int id)
        {
            try
            {
                var type = await _typeService.GetTypeById(id);
                if (type == null)
                {
                    return NotFound($"Type with ID {id} not found");
                }
                return Ok(type);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // POST: api/type
        [HttpPost]
        public async Task<ActionResult<TypeResponseDto>> CreateType(CreateTypeDto dto)
        {
            try
            {
                var type = await _typeService.CreateType(dto);
                return Ok(new TypeResponseDto
                {
                    TypeId = type.TypeId,
                    TypeName = type.TypeName,
                    TypeDesc = type.TypeDesc,
                    EventId = type.EventId
                });
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error creating type");
                return StatusCode(500, "Internal server error while creating type");
            }
        }

        // PUT: api/type/5
        [HttpPut("{id}")]
        public async Task<ActionResult<TypeResponseDto>> UpdateType(int id, UpdateTypeDto dto)
        {
            try
            {
                var type = await _typeService.UpdateType(id, dto);
                if (type == null)
                {
                    return NotFound($"Type with ID {id} not found");
                }
                return Ok(type);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // DELETE: api/type/5
        [HttpDelete("{id}")]
        public async Task<ActionResult> DeleteType(int id)
        {
            try
            {
                var result = await _typeService.DeleteType(id);
                if (!result)
                {
                    return NotFound($"Type with ID {id} not found");
                }
                return NoContent();
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // GET: api/type/event/5
        [HttpGet("event/{eventId}")]
        public async Task<ActionResult<IEnumerable<TypeResponseDto>>> GetTypesByEvent(int eventId)
        {
            var types = await _typeService.GetTypesByEvent(eventId);
            return Ok(types);
        }

        // GET: api/type/ticket/5
        [HttpGet("ticket/{ticketId}")]
        public async Task<ActionResult<TypeResponseDto>> GetTypeByTicket(int ticketId)
        {
            var type = await _typeService.GetTypeByTicket(ticketId);
            return Ok(type);
        }
    }
}