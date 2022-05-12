import os
import discord
import constant


class LocalizationManagementBot(discord.Client):
    def __init__(self):
        try:
            intents = discord.Intents.all()
            discord.Client(intents=intents)
            super().__init__()
        except Exception as err:
            print(f"> Error:\n{err}")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.id != self.user.id:
            channel = self.get_channel(constant.TEST_CHANNEL)
            await channel.send(message.content)

        print('Message from {0.author}: {0.content}'.format(message))

    class CommandHandler:
        # TODO: u sure this is a good idea
        pass


if __name__ == '__main__':
    client = LocalizationManagementBot()
    client.run(os.environ['BOT_TOKEN'])
