import logging
import logging.config
import yaml
import os


def get_logger(name:str)->logging:

    directoryPath = os.getenv("LOGGINGDEMOHOME", "./")

    with open(f"{directoryPath}logging.yaml", "r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    return logging.getLogger(name)