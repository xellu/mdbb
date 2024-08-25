from .templates.ConfigTemplate import ConfigTemplate
from .config import ConfigManager

Config = ConfigManager("config.json", template=ConfigTemplate)
