using System.ComponentModel.DataAnnotations;

namespace Horror.Models
{
    public class Location
    {
        [Key]
        public int Id { get; set; }

        [Required]
        [MaxLength(60)]
        [MinLength(2)]
        public string Name { get; set; }

        public string Requirement { get; set; }

    }
}