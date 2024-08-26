from core.bot import Bot, Tree
from core.bot import Tree as Slash
from core import Config
from core.events import EventBus
from core.logging import LoggingManager
from .shell import ShellManager

import threading

CommandLogger = LoggingManager("MDBB.Commands")
EventLogger = LoggingManager("MDBB.Events")
Shell = ShellManager()

if not Config.get("BOT.DEFAULTHELP"):
    Bot.remove_command("help")

threading.Thread(target=Shell.run_loop).start()