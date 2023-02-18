import discord
from mcrcon import MCRcon
from mcstatus import JavaServer


# discord client
intents = discord.Intents.default()  
intents.message_content = True
client = discord.Client(intents=intents)


def process_message(message):
    args = message.content.split(" ")

    return args

# create a new event
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))


# listen for specific messages
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'{username}: {user_message}')

    if message.author == client.user:
        return

    if channel == "minecraft" and user_message.startswith('!whitelist'):
        mc_username = user_message.split(' ')[1]
        print(mc_username)
        #replace port
        with MCRcon(host="put-server-ip-here", password="put-rcon-password-here", port=12345) as mcr:
            command = f'whitelist add {mc_username}'
            resp = mcr.command(command)
            print(resp)
            await message.channel.send(resp)

# run the bot
bot = "put-auth-key-here"
client.run(bot)
