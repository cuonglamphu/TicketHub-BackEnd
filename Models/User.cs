using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TicketHub_BackEnd.Models
{
    public class User
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int UserId { get; set; }
        
        [Required]
        [StringLength(100)]
        public string UserName { get; set; } = string.Empty;
        
        [Required]
        [StringLength(100)]
        public string FirstName { get; set; } = string.Empty;
        
        [Required]
        [StringLength(100)]
        public string LastName { get; set; } = string.Empty;
        
        [Required]
        [EmailAddress]
        [StringLength(100)]
        public string UserEmail { get; set; } = string.Empty;
        
        [Required]
        public string UserPassword { get; set; } = string.Empty;
        
        [Required]
        public string UserRole { get; set; } = "user";
        
        public DateTime UserJoinDate { get; set; } = DateTime.Now;

        public ICollection<Sale> Sales { get; set; } = new List<Sale>();
        public ICollection<Fraud> Frauds { get; set; } = new List<Fraud>();
    }
}