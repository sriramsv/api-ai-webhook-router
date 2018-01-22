

from flask import Blueprint
import logging,os
from flask import Blueprint
from flask_assistant import Assistant


class Bot():
    def __init__(self,name,client_access_token=None,dev_access_token=None):
        self.name=name
        self.client_access_token=client_access_token
        self.dev_access_token=dev_access_token
        self.blueprint=Blueprint(self.name.lower(),__name__,url_prefix="/{}".format(self.name.lower()))
        self.assist=Assistant(blueprint=self.blueprint,dev_token=self.dev_access_token,client_token=self.client_access_token)

class BotFactory():
    def __init__(self):
        self.bots={}

    def allBots(self):
        return self.bots.values()

    def addBot(self,bot):
        self.bots[bot.name.lower()]=bot

    def isBot(self,botname):
        return botname in self.bots

    def getBot(self,botname):
        try:
            bot=self.bots[botname]
            return bot
        except:
            return None

    def getBlueprint(self,botname):
        try:
            bot=self.bots[botname]
            return bot.blueprint
        except:
            return None

    def getAssistant(self,botname):
        try:
            bot=self.bots[botname]
            return bot.assist
        except:
            return None
