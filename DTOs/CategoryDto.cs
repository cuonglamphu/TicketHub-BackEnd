namespace TicketHub_BackEnd.DTOs
{
    public class CreateCategoryDto
    {
        public string CatName { get; set; } = string.Empty;
        public string CatDesc { get; set; } = string.Empty;
        public string CatSlug { get; set; } = string.Empty;
        public string CatThumb { get; set; } = string.Empty;
    }

    public class UpdateCategoryDto
    {
        public string CatName { get; set; } = string.Empty;
        public string CatDesc { get; set; } = string.Empty;
        public string CatSlug { get; set; } = string.Empty;
        public string CatThumb { get; set; } = string.Empty;
    }

    public class CategoryResponseDto
    {
        public int CatId { get; set; }
        public string CatName { get; set; } = string.Empty;
        public string CatDesc { get; set; } = string.Empty;
        public string CatSlug { get; set; } = string.Empty;
        public string CatThumb { get; set; } = string.Empty;
        public int EventCount { get; set; }
        public int UpcomingEventCount { get; set; }
        public decimal TotalRevenue { get; set; }
    }
}
