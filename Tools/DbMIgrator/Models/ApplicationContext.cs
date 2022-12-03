using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;

namespace DbMIgrator.Models
{
    public class ApplicationContext : DbContext
    {
        public ApplicationContext()
        {
        }

        DbSet<Users> Users { get; set; } = null!;
        DbSet<Links> Links { get; set; } = null!;
        DbSet<UserLinks> UserLinks { get; set; } = null!;
        DbSet<LinkPriceHistory> LinkPriceHistory { get; set; } = null!;
        DbSet<UserSettings> UserSettings { get; set; } = null!;

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql("Host=localhost;Port=5432;Database=DiscountChecker;Username=postgres;Password=C0laC0la");
        }
    }
}
