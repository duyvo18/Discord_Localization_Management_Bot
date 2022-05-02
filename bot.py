import discord

from config_reader import ConfigReader


class LocalizationManagementBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        discord.Client(intents=intents)
        super().__init__()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.id != self.user.id:
            channel = self.get_channel(968450197581598723)
            await channel.send(message.content)
        
        print('Message from {0.author}: {0.content}'.format(message))
        

    class CommandHandler:
        # TODO: u sure this is a good idea
        pass
        
if __name__ == '__main__':
    client = LocalizationManagementBot()
    client.run(ConfigReader.get_config("Tokens", "bot-token"))