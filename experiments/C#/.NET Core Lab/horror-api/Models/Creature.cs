using System.ComponentModel.DataAnnotations;

namespace Horror.Models
{
    public class Creature
    {
        [Key]
        public int Id { get; set; }

        [Required]
        [MaxLength(60)]
        [MinLength(2)]
        public string Name { get; set; }

        [Required]
        [MaxLength(60)]
        [MinLength(2)]
        public string Type { get; set; }

        [Required]
        [Range(1, int.MaxValue)]
        public int LocationId { get; set; }
        public Location Location { get; set; }
    }

}