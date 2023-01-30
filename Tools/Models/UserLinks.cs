namespace Models
{
    public class UserLinks
    {
        public int Id { get; set; }
        public string? LinkName { get; set; }

        public int UserId { get; set; }
        public User User { get; set; }

        public int LinkId { get; set; }
        public Links Link { get; set; }
    }
}
