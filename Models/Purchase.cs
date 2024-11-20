using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TicketHub_BackEnd.Models
{
    public class Purchase
    {
        [ForeignKey("Ticket")]
        public int TicketId { get; set; }
        public Ticket? Ticket { get; set; }

        [ForeignKey("Sale")]
        public int SaleId { get; set; }
        public Sale? Sale { get; set; }

        public int Quantity { get; set; } = 1;
    }
}