import yaml


def load_config():
    with open("config.yaml", 'r') as stream:
        return yaml.safe_load(stream)
