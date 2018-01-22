from flask_assistant import ask,tell
from settings import botfactory
assist=botfactory.getAssistant('tasker')
@assist.action("hello")
def hello():
    return tell("Oh Hi")
