# MDBB
MDBB Is a Base for Discord Bots, It's a simple and fast way to create a bot for discord, using the discord.py library.

## Features
- Event System
- Event Handlers
- Shell Commands
- Config Manager
- Logging Manager

## Installation
1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt`

## Usage
When you run the bot for the first time, it will create a `config.json` file in the project root. You can edit this file to add your bot token and other configurations.

To run the bot, use the following command:
```bash
python main.py
```

## Events
Events are the core of MDBB. They are used to trigger actions in response to certain events. You can create custom events and event handlers to extend the functionality of your bot.

### Built-In Events
- `error` - Is emitted when an error is detected.
- `warn` - A Warning message event
- `shutdown` - Call to shutdown the bot
- `shutdown.force` - Call to force shutdown the bot
- `shutdown.crash` - Will cause the bot to crash shutdown
- `start` - Called when the bot is starting up
- `ready` - Called when the bot is fully loaded and ready to accept commands
> You can find more information about events in the `events.md` file.

### Examples
#### Creating a Custom Event
```py
from mdbb import EventBus

#Event Handler
@EventBus.on("hello")
def on_hello_event(name):
    print(f"Hello, {name}!")

#Emitting the Event
EventBus.signal("Hello", "John")
#                ^      ^
#                |      |
#                |      +-- Arguments
#                +-- Event ID

#Output: Hello, John!
```
You can find more examples in `core/events/builtins.py`

## Shell Commands
MDBB comes with a built-in shell command system that allows you to interact with the bot using commands in the terminal. You can create custom shell commands to extend the functionality of your bot.

### Built-In Shell Commands
- `help` - Displays a list of available commands
- `about` - Displays information about the bot
- `stop` - Shutdowns the service
- `clear` - Clears the terminal screen
- `sync` - Synchronizes slash commands with Discord
- `threads` - Lists all active threads
> You can find more information about shell commands using the `help` command.

You can also create custom shell commands using the `@Shell.command` decorator

#### Example:
```py
from mdbb.shell import Shell

@Shell.command("hello", "Prints Hello World!", usage="hello")
def hello_command(ctx):
    return "Hello World!"
```
More examples can be found in `mdbb/shell/builtins.py`

## Config Manager
MDBB comes with a built-in configuration manager that allows you to manage your bot's configuration settings. You can create custom configuration templates to store and retrieve data from the configuration file.

### Example
```py
from mdbb import Config

bot_prefix = Config.get("BOT.PREFIX") 
print(bot_prefix)
```