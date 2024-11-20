using Microsoft.AspNetCore.Mvc;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.Services;
using TicketHub_BackEnd.DTOs;

namespace TicketHub_BackEnd.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TicketController : ControllerBase
    {
        private readonly ITicketService _ticketService;

        public TicketController(ITicketService ticketService)
        {
            _ticketService = ticketService;
        }

        // GET: api/ticket
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Ticket>>> GetTickets()
        {
            try
            {
                var tickets = await _ticketService.GetAllTickets();
                return Ok(tickets);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // GET: api/ticket/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Ticket>> GetTicket(int id)
        {
            try
            {
                var ticket = await _ticketService.GetTicketById(id);
                if (ticket == null)
                {
                    return NotFound($"Ticket with ID {id} not found");
                }
                return Ok(ticket);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // GET: api/ticket/event/5
        [HttpGet("event/{eventId}")]
        public async Task<ActionResult<IEnumerable<Ticket>>> GetTicketsByEvent(int eventId)
        {
            try
            {
                var tickets = await _ticketService.GetTicketsByEvent(eventId);
                return Ok(tickets);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // POST: api/ticket
        [HttpPost]
        public async Task<ActionResult<Ticket>> CreateTicket(CreateTicketDto dto)
        {
            try
            {
                var ticket = await _ticketService.CreateTicket(dto);
                return CreatedAtAction(nameof(GetTicket), new { id = ticket.TicketId }, ticket);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }

        // DELETE: api/ticket/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTicket(int id)
        {
            await _ticketService.DeleteTicket(id);
            return NoContent();
        }

        // PUT: api/ticket/5
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateTicket(int id, UpdateTicketDto dto)
        {
            await _ticketService.UpdateTicket(id, dto);
            return NoContent();
        }

        [HttpPost("purchase")]
        public async Task<ActionResult<PurchaseResponseDto>> PurchaseTicket(
            [FromQuery] int userId,
            [FromBody] CreatePurchaseDto purchase)
        {
            try
            {
                var result = await _ticketService.PurchaseTicket(userId, purchase);
                return Ok(result);
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (InvalidOperationException ex)
            {
                return BadRequest(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }
    }
}
