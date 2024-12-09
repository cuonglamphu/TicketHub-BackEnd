using System.ComponentModel.DataAnnotations;

namespace TicketHub_BackEnd.Models;

public class Fraud
{
    [Key]
    public int FraudId { get; set; }

    public int UserId { get; set; }
    public DateTime FraudDate { get; set; }
}