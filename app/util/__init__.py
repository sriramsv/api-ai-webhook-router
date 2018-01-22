import yaml
import pkgutil
import sys
from botschema import BotFactory,Bot

host=None
port=None


class Server():
    def __init__(self,host="127.0.0.1",port=8080):
        self.host=host
        self.port=port





def readConfig(config):
    with open(config, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    if 'host' in cfg.keys():
            host=cfg['host']
    if 'port' in cfg.keys():
            port=cfg['port']

    if not "bots" in cfg.keys():
        sys.exit("No bots found")
    bf=BotFactory()
    server=Server(host,port)
    for b in cfg['bots']:
        bot=Bot(**b)
        bf.addBot(bot)
    return bf,server
