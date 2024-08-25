from mdbb import Bot, EventLogger, EventBus

import sys
from discord.ext import commands

#add cogs here ⬇️
from . import (example)
COGS = [example.Example] 

@Bot.event
async def on_ready():
    EventLogger.success(f"Connected to Discord Gateway as {Bot.user}")

    #cogs injection
    for cog in COGS:
        await Bot.add_cog(cog())

    EventBus.signal("ready")

@Bot.event
async def on_error(event, *args, **kwargs):
    exception = sys.exc_info()[0]
    EventBus.signal("error", exception, "Cogs", f"Error in event {event} (args: {args}, kwargs: {kwargs})")

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    EventBus.signal("error", error, "Cogs", f"Error in command {ctx.command.name} (ctx: {ctx})")