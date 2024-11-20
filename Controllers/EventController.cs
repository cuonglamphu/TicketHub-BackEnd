using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.Services;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;

namespace TicketHub.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class EventController : ControllerBase
    {
        private readonly IEventService _eventService;

        public EventController(IEventService eventService)
        {
            _eventService = eventService;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Event>>> GetEvents()
        {
            var events = await _eventService.GetAllEvents();
            return Ok(events);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Event>> GetEvent(int id)
        {
            var @event = await _eventService.GetEventById(id);
            if (@event == null)
            {
                return NotFound();
            }
            return Ok(@event);
        }

        [HttpGet("category/{catId}")]
        public async Task<ActionResult<IEnumerable<Event>>> GetEventsByCategory(int catId)
        {
            var events = await _eventService.GetEventsByCategory(catId);
            return Ok(events);
        }

        [HttpPost]
        public async Task<ActionResult<Event>> CreateEvent(CreateEventDto dto)
        {
            var @event = await _eventService.CreateEvent(dto);
            return CreatedAtAction(nameof(GetEvent), new { id = @event.EveId }, @event);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateEvent(int id, UpdateEventDto dto)
        {
            var result = await _eventService.UpdateEvent(id, dto);
            if (!result)
            {
                return NotFound();
            }
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteEvent(int id)
        {
            var result = await _eventService.DeleteEvent(id);
            if (!result)
            {
                return NotFound();
            }
            return NoContent();
        }
    }
}