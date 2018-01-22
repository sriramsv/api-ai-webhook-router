from flask import Flask
import settings
import bots

flaskapp=Flask(__name__)
for bot in settings.botfactory.allBots():
    flaskapp.register_blueprint(bot.blueprint)
flaskapp.host=settings.server.host
flaskapp.port=settings.server.port 
