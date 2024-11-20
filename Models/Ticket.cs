using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TicketHub_BackEnd.Models
{
    public class Ticket
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        // Ticket ID
        public int TicketId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        // Ticket Price
        public decimal TicketPrice { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        // Ticket Quantity
        public decimal TicketQty { get; set; }

        [ForeignKey("Event")]
        // Event ID
        public int EveId { get; set; }
        public Event? Event { get; set; }

        [ForeignKey("Type")]
        // Type ID
        public int TypeId { get; set; }
        public Type? Type { get; set; }

        // public ICollection<Purchase> Purchases { get; set; } = new List<Purchase>();
    }
}
