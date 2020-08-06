using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Horror.Data;
using Horror.Models;

namespace Horror.Controllers
{
    [ApiController]
    [Route("v1/locations")]
    public class LocationController : ControllerBase
    {

        [HttpGet]
        [Route("")]
        public async Task<ActionResult<List<Location>>> Get([FromServices] DataContext context)
        {
            var locations = await context.Locations.ToListAsync();
            return locations;
        }

        [HttpPost]
        [Route("")]
        public async Task<ActionResult<Location>> Post([FromServices] DataContext context, [FromBody] Location location)
        {
            if (ModelState.IsValid)
            {
                context.Locations.Add(location);
                await context.SaveChangesAsync();
                return location;
            }
            else
            {
                return BadRequest(ModelState);
            }

        }

    }

}