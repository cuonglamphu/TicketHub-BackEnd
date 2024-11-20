using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using TicketHub_BackEnd.Models;

namespace TicketHub_BackEnd.Models
{
    public class Event
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int EveId { get; set; }
        public string EveName { get; set; } = string.Empty;
        public string EveDesc { get; set; } = string.Empty;
        public string EveCity { get; set; } = string.Empty;
        public DateTime EveTimestart { get; set; }
        public DateTime? EveTimeend { get; set; }
        public string EveThumb { get; set; } = string.Empty;

        [ForeignKey("Category")]
        public int CatId { get; set; }

        public Category? Category { get; set; }

        public ICollection<Ticket> Tickets { get; set; } = new List<Ticket>();
    }
}
