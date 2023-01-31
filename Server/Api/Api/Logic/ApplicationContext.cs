using Microsoft.EntityFrameworkCore;
using Models;

namespace Api.Logic
{
    public class ApplicationContext : DbContext
    {
        public DbSet<User> Users { get; set; } = null!;
        public ApplicationContext(DbContextOptions<ApplicationContext> options) : base(options)
        {
            Database.EnsureCreated();
        }
    }

    public static class ApplicationContextGetter
    {
        public static ApplicationContext GetContext()
        {
            var builder = new ConfigurationBuilder();
            builder.SetBasePath(Directory.GetCurrentDirectory());
            builder.AddJsonFile("appsettings.json");
            var config = builder.Build();
            string? connectionString = config.GetConnectionString("DefaultConnection");

            var optionsBuilder = new DbContextOptionsBuilder<ApplicationContext>();
            if (connectionString != null)
            {
                var options = optionsBuilder.UseNpgsql(connectionString).Options;

                return new ApplicationContext(options);
            }

            throw new Exception("GetContext: connection string is null");
        }
    }
}
