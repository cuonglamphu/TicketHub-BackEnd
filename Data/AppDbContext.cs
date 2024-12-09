using Microsoft.EntityFrameworkCore;
using TicketHub_BackEnd.Models;
using Microsoft.EntityFrameworkCore.Query.SqlExpressions;
namespace TicketHub_BackEnd.Data;


public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<Category> Categories { get; set; }

    public DbSet<Event> Events { get; set; }

    public DbSet<Ticket> Tickets { get; set; }

    public DbSet<Models.Type> Types { get; set; }

    public DbSet<Sale> Sales { get; set; }

    public DbSet<Purchase> Purchases { get; set; }

    public DbSet<User> Users { get; set; }

    public DbSet<Fraud> Frauds { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        if (Database.IsSqlite())
        {
            var methodInfo = typeof(DbFunctions).GetMethod("DateDiffDay", new[] { typeof(DateTime?), typeof(DateTime?) });
            if (methodInfo != null)
            {
                modelBuilder.HasDbFunction(methodInfo)
                    .HasTranslation(args =>
                        new SqlFunctionExpression(
                            "julianday",
                            new[] {
                                args[1],  // end date
                                new SqlFragmentExpression("-"),
                                args[0]   // start date
                            },
                            nullable: true,
                            argumentsPropagateNullability: new[] { true, true, true },
                            typeof(int?),
                            typeMapping: null));
            }
        }

        modelBuilder.Entity<Category>()
            .HasKey(c => c.CatId);

        modelBuilder.Entity<Category>()
            .Property(c => c.CatId)
            .ValueGeneratedOnAdd();

        modelBuilder.Entity<Event>()
            .HasOne(e => e.Category)
            .WithMany()
            .HasForeignKey(e => e.CatId)
            .OnDelete(DeleteBehavior.Cascade);

        modelBuilder.Entity<Purchase>()
            .HasKey(p => new { p.TicketId, p.SaleId });

        modelBuilder.Entity<Purchase>()
            .HasOne(p => p.Ticket)
            .WithMany()
            .HasForeignKey(p => p.TicketId);

        modelBuilder.Entity<Purchase>()
            .HasOne(p => p.Sale)
            .WithMany(s => s.Purchases)
            .HasForeignKey(p => p.SaleId);

        modelBuilder.Entity<Models.Type>(entity =>
        {
            entity.ToTable("Types");
            entity.HasKey(t => t.TypeId);
        });

        modelBuilder.Entity<Ticket>()
            .HasOne(t => t.Event)
            .WithMany(e => e.Tickets)
            .HasForeignKey(t => t.EveId);

        modelBuilder.Entity<Ticket>()
            .HasOne(t => t.Type)
            .WithMany()
            .HasForeignKey(t => t.TypeId);

        modelBuilder.Entity<Sale>()
            .HasMany(s => s.Purchases)
            .WithOne(p => p.Sale)
            .HasForeignKey(p => p.SaleId);

        // Seed Categories
        modelBuilder.Entity<Category>().HasData(
            new Category
            {
                CatId = 1,
                CatName = "Concerts",
                CatSlug = "concerts",
                CatDesc = "Live music performances",
                CatThumb = "https://salt.tkbcdn.com/ts/ds/9e/ab/87/cf3513a86027d31026f5be1e866895c3.png"
            },
            new Category
            {
                CatId = 2,
                CatName = "Sports",
                CatSlug = "sports",
                CatDesc = "Sporting events",
                CatThumb = "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/4d368a40fbbe70184a6278a0f3361506.jpg"
            }
        );

        // Seed Events
        modelBuilder.Entity<Event>().HasData(
            new Event
            {
                EveId = 1,
                EveName = "Taylor Swift Concert",
                EveDesc = "The Eras Tour",
                EveCity = "New York",
                EveTimestart = new DateTime(2024, 7, 15, 19, 0, 0),
                EveTimeend = new DateTime(2024, 7, 15, 23, 0, 0),
                EveThumb = "https://salt.tkbcdn.com/ts/ds/9e/ab/87/cf3513a86027d31026f5be1e866895c3.png",
                CatId = 1
            },
            new Event
            {
                EveId = 2,
                EveName = "NBA Finals 2024",
                EveDesc = "Championship Game",
                EveCity = "Los Angeles",
                EveTimestart = new DateTime(2024, 6, 10, 20, 0, 0),
                EveTimeend = new DateTime(2024, 6, 10, 23, 0, 0),
                EveThumb = "https://salt.tkbcdn.com/ts/ds/ed/d1/30/00f0fbc999f8a4dedf030f9e3c7b27db.jpg",
                CatId = 2
            }
        );

        // Seed Types
        modelBuilder.Entity<Models.Type>().HasData(
            new Models.Type
            {
                TypeId = 1,
                TypeName = "VIP",
                TypeDesc = "VIP Access with Meet & Greet",
                EventId = 1
            },
            new Models.Type
            {
                TypeId = 2,
                TypeName = "Regular",
                TypeDesc = "Standard Admission",
                EventId = 1
            },
            new Models.Type
            {
                TypeId = 3,
                TypeName = "Courtside",
                TypeDesc = "Courtside Seats",
                EventId = 2
            }
        );

        // Seed Users
        modelBuilder.Entity<User>().HasData(
            new User
            {
                UserId = 1,
                UserName = "admin",
                FirstName = "Admin",
                LastName = "System",
                UserEmail = "admin@tickethub.com",
                // Hash password admin123
                UserPassword = "$2a$12$nt/QKdSvcg2VXDfKptogKuwvd5lV8Tw0MfopvgHRRGcTgToIgDZjS",
                UserRole = "admin",
                UserJoinDate = new DateTime(2024, 1, 1)
            },
            new User
            {
                UserId = 2,
                UserName = "john_doe",
                FirstName = "John",
                LastName = "Doe",
                UserEmail = "john@example.com",
                // Hash password user123
                UserPassword = "$2a$12$tSzglqCkPC3HdsYCq36jfOumHrF/A1xP1DKPNhC2TzMBFhJmhNuuC",
                UserRole = "user",
                UserJoinDate = new DateTime(2024, 1, 1)
            }
        );

        // Seed Tickets
        modelBuilder.Entity<Ticket>().HasData(
            new Ticket
            {
                TicketId = 1,
                TicketPrice = 1000000,
                TicketQty = 100,
                EveId = 1,  // Taylor Swift Concert
                TypeId = 1  // VIP
            },
            new Ticket
            {
                TicketId = 2,
                TicketPrice = 500000,
                TicketQty = 200,
                EveId = 1,  // Taylor Swift Concert
                TypeId = 2  // Regular
            },
            new Ticket
            {
                TicketId = 3,
                TicketPrice = 2000000,
                TicketQty = 50,
                EveId = 2,  // NBA Finals
                TypeId = 3  // Courtside
            }
        );

        // Seed Sales for user 1
        modelBuilder.Entity<Sale>().HasData(
            new Sale
            {
                SaleId = 1,
                UserId = 1,  // admin user
                SaleTotal = 2000000,  // 2 VIP tickets for Taylor Swift
                SaleDate = new DateTime(2024, 1, 15, 10, 30, 0)
            },
            new Sale
            {
                SaleId = 2,
                UserId = 1,  // admin user
                SaleTotal = 4000000,  // 2 Courtside NBA tickets
                SaleDate = new DateTime(2024, 1, 20, 14, 45, 0)
            }
        );

        // Seed Purchases related to Sales
        modelBuilder.Entity<Purchase>().HasData(
            new Purchase
            {
                TicketId = 1,  // VIP Taylor Swift ticket
                SaleId = 1,    // First sale
                Quantity = 2   // 2 tickets
            },
            new Purchase
            {
                TicketId = 3,  // Courtside NBA ticket
                SaleId = 2,    // Second sale
                Quantity = 2   // 2 tickets
            }
        );

        base.OnModelCreating(modelBuilder);
    }
}
