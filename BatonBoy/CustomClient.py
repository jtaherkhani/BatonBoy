import discord
from datetime import datetime
from ActionManager import ActionManager

class CustomClient(discord.Client):
    """Creates a custom client wrapping for events we want to subscribe to in discord"""
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.AcceptNewMessages == True:
            self.AcceptNewMessages = False
            await self.ActionManager.run(message.clean_content, message)
            self.AcceptNewMessages = True

    def __init__(self, *args, **kwargs):
        self.ActionManager = ActionManager(self)
        self.AcceptNewMessages = True
        return super().__init__(*args, **kwargs)
