namespace DbMIgrator.Models
{
    public class Links
    {
        public int Id { get; set; }
        public string? Url { get; set; }
        public double CurrentPrice { get; set; }
        public bool DiscountStatus { get; set; }
    }
}
