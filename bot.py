import discord

from config_reader import ConfigReader

TOKEN = ConfigReader.get_config("Tokens", "bot-token")

class LocalizationManagementBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        

    class CommandHandler:
        # TODO: u sure this is a good idea
        pass
        

client = LocalizationManagementBot()
client.run(TOKEN)