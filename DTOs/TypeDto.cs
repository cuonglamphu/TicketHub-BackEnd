namespace TicketHub_BackEnd.DTOs
{
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
        public decimal TypePrice { get; set; }
    }

    public class TypeResponseDto
    {
        public int TypeId { get; set; }
        public string TypeName { get; set; } = string.Empty;
        public string TypeDesc { get; set; } = string.Empty;
        public int EventId { get; set; }
    }
}