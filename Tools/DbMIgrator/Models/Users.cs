namespace DbMIgrator.Models
{
    public class Users
    {
        public int Id { get; set; }
        public string UserName { get; set; }
        public string Password { get; set; }
        public string? Token { get; set; }
        public DateTime? TokenExpiration { get; set; }

        public UserSettings UserSettings { get; set; }
    }
}
