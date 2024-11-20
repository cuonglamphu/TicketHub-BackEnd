namespace TicketHub_BackEnd.DTOs
{
    public class CreateTicketDto
    {

        public int EveId { get; set; }
        public decimal TicketQty { get; set; }

        public decimal TicketPrice { get; set; }
        public int TypeId { get; set; }
    }

    public class PurchaseTicketDto
    {
        public int TicketId { get; set; }
        public int TypeId { get; set; }
        public int Quantity { get; set; }
    }

    public class UpdateTicketDto
    {
        public int EveId { get; set; }
        public int TypeId { get; set; }
        public int TicketQty { get; set; }
        public decimal TicketPrice { get; set; }

    }
}