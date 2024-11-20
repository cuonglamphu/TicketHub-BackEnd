using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Data;
using TicketHub_BackEnd.Models;
using TicketHub_BackEnd.DTOs;
using Type = TicketHub_BackEnd.Models.Type;
using Microsoft.Extensions.Logging;

namespace TicketHub_BackEnd.Services
{
    public class TypeService : ITypeService
    {
        private readonly AppDbContext _context;
        private readonly ILogger<TypeService> _logger;

        public TypeService(AppDbContext context, ILogger<TypeService> logger)
        {
            _context = context;
            _logger = logger;
        }

        public async Task<IEnumerable<TypeResponseDto>> GetAllTypes()
        {
            return await _context.Types
                .Select(t => new TypeResponseDto
                {
                    TypeId = t.TypeId,
                    TypeName = t.TypeName,
                    TypeDesc = t.TypeDesc,
                    EventId = t.EventId,
                })
                .ToListAsync();
        }

        public async Task<TypeResponseDto?> GetTypeById(int id)
        {
            return await _context.Types
                .Where(t => t.TypeId == id)
                .Select(t => new TypeResponseDto
                {
                    TypeId = t.TypeId,
                    TypeName = t.TypeName,
                    TypeDesc = t.TypeDesc,
                    EventId = t.EventId,
                })
                .FirstOrDefaultAsync();
        }

        public async Task<IEnumerable<TypeResponseDto>> GetTypesByEvent(int eventId)
        {
            return await _context.Types
                .Where(t => t.EventId == eventId)
                .Select(t => new TypeResponseDto
                {
                    TypeId = t.TypeId,
                    TypeName = t.TypeName,
                    TypeDesc = t.TypeDesc,
                    EventId = t.EventId,
                })
                .ToListAsync();
        }

        public async Task<TypeResponseDto?> UpdateType(int id, UpdateTypeDto dto)
        {
            try
            {
                var type = await _context.Types.FindAsync(id);
                if (type == null)
                    throw new KeyNotFoundException($"Không tìm thấy type với id: {id}");

                type.TypeName = dto.TypeName;
                type.TypeDesc = dto.TypeDesc;

                await _context.SaveChangesAsync();
                return await GetTypeById(id);
            }
            catch (Exception ex)
            {
                throw new Exception($"Lỗi khi cập nhật type: {ex.Message}");
            }
        }

        public async Task<bool> DeleteType(int id)
        {
            var type = await _context.Types.FindAsync(id);
            if (type == null)
                return false;

            _context.Types.Remove(type);
            await _context.SaveChangesAsync();
            return true;
        }

        public async Task<TypeResponseDto> CreateType(CreateTypeDto dto)
        {
            // Kiểm tra Event tồn tại
            var eventExists = await _context.Events
                .AnyAsync(e => e.EveId == dto.EventId);

            if (!eventExists)
            {
                _logger.LogError($"Event with ID {dto.EventId} not found");
                throw new KeyNotFoundException($"Event with ID {dto.EventId} not found");
            }

            var type = new Type
            {
                TypeName = dto.TypeName,
                TypeDesc = dto.TypeDesc,
                EventId = dto.EventId
            };

            _context.Types.Add(type);
            await _context.SaveChangesAsync();

            // Return TypeResponseDto instead of Type
            return await GetTypeById(type.TypeId);
        }

        public async Task<TypeResponseDto> GetTypeByTicket(int ticketId)
        {
            var type = await _context.Types.FindAsync(ticketId);
            return new TypeResponseDto { TypeId = type.TypeId, TypeName = type.TypeName, TypeDesc = type.TypeDesc, EventId = type.EventId };
        }


    }
}