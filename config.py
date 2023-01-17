from datetime import datetime

import yaml
import os
import time
from datetime import datetime

from aiohttp import request


def load_config():
    with open("config.yaml", "r") as stream:
        return yaml.safe_load(stream)


def harvest_supported_coin():
    path = "token_list.yaml"
    if os.path.exists(path):
        if os.path.getmtime(path) - time.localtime() < 3600 * 24:
            return
    resp = request("GET", "https://api.coingecko.com/api/v3/coins/list")
    yaml.safe_dump(resp, "token_list.yaml")



