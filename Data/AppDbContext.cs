using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Models;

namespace TicketHub_BackEnd.Data;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<Category> Categories { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Category>()
            .HasKey(c => c.CatId);

        modelBuilder.Entity<Category>()
            .Property(c => c.CatId)
            .ValueGeneratedOnAdd();
    }
}
