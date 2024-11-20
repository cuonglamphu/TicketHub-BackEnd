namespace TicketHub_BackEnd.DTOs
{
    public class CreateEventDto
    {
        public string EveName { get; set; } = string.Empty;
        public string EveDesc { get; set; } = string.Empty;
        public string EveCity { get; set; } = string.Empty;
        public DateTime EveTimestart { get; set; }
        public DateTime? EveTimeend { get; set; }
        public string EveThumb { get; set; } = string.Empty;
        public int CatId { get; set; }
    }

    public class UpdateEventDto
    {
        public string EveName { get; set; } = string.Empty;
        public string EveDesc { get; set; } = string.Empty;
        public string EveCity { get; set; } = string.Empty;
        public DateTime EveTimestart { get; set; }
        public DateTime? EveTimeend { get; set; }
        public string EveThumb { get; set; } = string.Empty;
        public int CatId { get; set; }
    }
}