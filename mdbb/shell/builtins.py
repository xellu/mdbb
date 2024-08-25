from .. import Shell
from . import CommandResponse
from core.events import EventBus

import os
import time

@Shell.command("help", "Show this help message", "help [command]", [{"name": "command", "description": "The command to show help for", "required": False}])
def help_command(ctx, command):
    if command is None:
        messages = ["[] - Optional  /  <> - Required", "Available commands:"]

        for command in Shell.commands:
            messages.append(f"{command['id']}: {command['description']}")

        return CommandResponse(messages)
    else:
        command = Shell.get_command(command)
        if command is None:
            return f"Command {command} not found"
        else:
            return CommandResponse([
                f"Showing help for {command['id']}:",
                command['description'], "",
                
                f"Usage: {command['usage']}", 
                "[] - Optional  /  <> - Required",
                
                "", "Arguments:",
                *[f"{arg['name']} - {arg['description']} {'(required)' if arg['required'] else '(optional)'}" for arg in command['arguments']]
            ])
        
@Shell.command("stop", "Stop the mdbb service", "stop [--force]")
def stop_command(ctx, *args, **kwargs):
    if kwargs.get("force", False):
        ctx.logger.warning("Issuing force shutdown")
        EventBus.signal("shutdown.force", "Requested by operator")
        return

    ctx.logger.warning("Shutdown procedure initiated, use --force if needed")
    EventBus.signal("shutdown", "Requested by operator")

@Shell.command("clear", "Clear the console", "clear")
def clear_command(ctx):
    os.system("cls" if os.name == "nt" else "clear")
    return "Console was cleared, log file was not affected"

@Shell.command("sync", "Sync the slash commands", "sync")
def sync_command(ctx):
    EventBus.signal("mdbb.sync")
    ctx.logger.info("Command synchronization requested")