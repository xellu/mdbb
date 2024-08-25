from core.bot import Bot, Slash
from core import Config
from core.events import EventBus
from core.logging import LoggingManager
from .shell import ShellManager

import threading

CommandLogger = LoggingManager("MDBB.Commands")
EventLogger = LoggingManager("MDBB.Events")
Shell = ShellManager()

threading.Thread(target=Shell.run_loop).start()