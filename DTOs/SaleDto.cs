namespace TicketHub_BackEnd.DTOs
{
    public class SaleResponseDto
    {
        public int SaleId { get; set; }
        public int UserId { get; set; }
        public string UserName { get; set; } = string.Empty;
        public string UserEmail { get; set; } = string.Empty;
        public DateTime SaleDate { get; set; }
        public decimal SaleTotal { get; set; }
        public List<PurchaseDetailDto> Purchases { get; set; } = new();
    }
}