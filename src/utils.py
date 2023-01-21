import yaml
from pathlib import Path

# Folder to load config file
CONFIG_PATH = "src/config/"

#%% Function to load yaml configuration file
def load_config(config_name):
    with open(Path(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config
