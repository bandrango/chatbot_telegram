import yaml

from yaml.loader import SafeLoader

# Load configuration
def loadConfig():
    # Open the file and load the file
    with open('config/application.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)
    return config