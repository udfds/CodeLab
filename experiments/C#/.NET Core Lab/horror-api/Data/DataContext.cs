using Microsoft.EntityFrameworkCore;
using Horror.Models;

namespace Horror.Data
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions<DataContext> options) : base(options)
        {
        }

        public DbSet<Creature> Creatures { get; set; }
        public DbSet<Location> Locations { get; set; }
    }
}