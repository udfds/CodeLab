import os

from twitchio.ext import commands

#----------------------------------------------------------------
# Setup for the bot
#----------------------------------------------------------------

bot = commands.Bot(
    irc_token = os.environ['TMI_TOKEN'],
    client_id = os.environ['CLIENT_ID'],
    nick = os.environ['BOT_NICK'],
    prefix = os.environ['BOT_PREFIX'],
    initial_channels = [os.environ['CHANNEL']]
)

#----------------------------------------------------------------
# Events
#----------------------------------------------------------------

@bot.event
async def event_ready():
    message = os.environ['BOT_NICK'] + 'is online!'
    print(message)
    #ws = bot._ws
    #await ws.send_privmsg(message)


@bot.event
async def event_message(context):
    if context.author.name.lower() == os.environ['BOT_NICK'].lower():
        # Ignore the message of itself
        return

    # Check for commands
    await bot.handle_commands(context)
    
    # Response the message
    if not context.content.startswith('!'): 
        await context.channel.send(' -' + context.content)
    

@bot.command(name='join')
async def command_join(context):
    await context.channel.send('Command join works')


#----------------------------------------------------------------
# Start
#----------------------------------------------------------------
if __name__ == "__main__":
    bot.run()