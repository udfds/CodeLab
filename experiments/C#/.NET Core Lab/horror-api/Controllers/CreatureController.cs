using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Horror.Data;
using Horror.Models;

namespace Horror.Controllers
{
    [ApiController]
    [Route("v1/creatures")]
    public class CreatureController : ControllerBase
    {

        [HttpGet]
        [Route("")]
        public async Task<ActionResult<List<Creature>>> Get([FromServices] DataContext context)
        {
            var creatures = await context.Creatures.ToListAsync();
            return creatures;
        }

        [HttpPost]
        [Route("")]
        public async Task<ActionResult<Creature>> Post([FromServices] DataContext context, [FromBody] Creature creature)
        {
            if (ModelState.IsValid)
            {
                context.Creatures.Add(creature);
                await context.SaveChangesAsync();
                return creature;
            }
            else
            {
                return BadRequest(ModelState);
            }

        }

    }

}