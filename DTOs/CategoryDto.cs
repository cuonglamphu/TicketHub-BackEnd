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
}
