namespace TicketHub_BackEnd.DTOs
{
    public class CreatePurchaseDto
    {

        public int TicketId { get; set; }
        public int Quantity { get; set; }

        public string IpAddress { get; set; } = string.Empty;

        public string DeviceInfo { get; set; } = string.Empty;

        public string BrowserInfo { get; set; } = string.Empty;
    }

    public class PurchaseResponseDto
    {
        public int SaleId { get; set; }
        public decimal SaleTotal { get; set; }
        public DateTime SaleDate { get; set; }
        public List<PurchaseDetailDto> Purchases { get; set; } = new List<PurchaseDetailDto>();
    }

    public class PurchaseDetailDto
    {
        public int TicketId { get; set; }
        public string EventName { get; set; } = string.Empty;
        public string EventCity { get; set; } = string.Empty;
        public DateTime EventTimeStart { get; set; }
        public string EventThumb { get; set; } = string.Empty;
        public string TicketType { get; set; } = string.Empty;
        public int Quantity { get; set; }
        public decimal Price { get; set; }
        public decimal Total { get; set; }
    }
}