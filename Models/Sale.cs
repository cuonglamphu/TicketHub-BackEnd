using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TicketHub_BackEnd.Models
{
    public class Sale
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int SaleId { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal SaleTotal { get; set; }

        public DateTime SaleDate { get; set; }

        [ForeignKey("User")]
        public int UserId { get; set; }
        public User? User { get; set; }

        public ICollection<Purchase> Purchases { get; set; } = new List<Purchase>();

        public string? IpAddress { get; set; }

        public string? DeviceInfo { get; set; }

        public string? BrowserInfo { get; set; }
    }
}