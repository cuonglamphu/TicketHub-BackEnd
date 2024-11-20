namespace TicketHub_BackEnd.Models;
public class Category
{
    public int CatId { get; set; }
    public string CatName { get; set; } = string.Empty;
    public string CatSlug { get; set; } = string.Empty;
    public string CatDesc { get; set; } = string.Empty;
    public string CatThumb { get; set; } = string.Empty;
}