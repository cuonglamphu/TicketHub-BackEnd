namespace TicketHub_BackEnd.Services
{
    public interface ITypeService
    {
        Task<IEnumerable<TypeResponseDto>> GetAllTypes();
        Task<TypeResponseDto> GetTypeById(int typeId);
        Task<TypeResponseDto> CreateType(CreateTypeDto typeDto);
        Task<TypeResponseDto> UpdateType(int typeId, UpdateTypeDto typeDto);
        Task<bool> DeleteType(int typeId);
        Task<IEnumerable<TypeResponseDto>> GetTypesByEvent(int eventId);
        Task<TypeResponseDto> GetTypeByTicket(int ticketId);
    }



    public class CreateTypeDto
    {
        public string TypeName { get; set; } = string.Empty;
        public string TypeDesc { get; set; } = string.Empty;
        public int EventId { get; set; }
    }

    public class UpdateTypeDto
    {
        public string TypeName { get; set; } = string.Empty;
        public string TypeDesc { get; set; } = string.Empty;
    }

    public class TypeDto
    {
        public string TypeName { get; set; } = string.Empty;
        public string TypeDesc { get; set; } = string.Empty;
    }

    public class TypeResponseDto
    {
        public int TypeId { get; set; }
        public string TypeName { get; set; } = string.Empty;
        public string TypeDesc { get; set; } = string.Empty;
        public int EventId { get; set; }
    }
}