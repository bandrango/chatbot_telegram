"""
This is the Load configurations from application.yaml.

@autor: Byron Andrango
@since: 2023 - Jan
@version: 1.0
"""

import yaml

from yaml.loader import SafeLoader

# Load configuration
def loadConfig():
    # Open the file and load the file
    with open('config/application.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)
    return config