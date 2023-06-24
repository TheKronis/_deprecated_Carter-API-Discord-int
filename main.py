#   Important Imports
import nextcord
from nextcord.ext import commands
import requests
import dotenv
import os
import json

#   Loads everything important from .env file
dotenv.load_dotenv()

#   Intents allows bots to access certain data like Members or Content of Messages
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

#   Setting up the bot, setting the prefix for commands and loading Intents
client = commands.Bot(command_prefix = commands.when_mentioned_or(os.getenv("BOT_PREFIX")), intents=intents)

#   Get rid of the default Help Command
client.remove_command("help")

#   This event is triggered when the bot is ready and connected to the Discord API
@client.event
async def on_ready():
    print("Bot is ready!")
    
#   This event is triggered whenever a message is sent where the bot can read it
@client.event
async def on_message(message):
        channel = message.channel
        #   Check if the message was sent in Direct Messages, not sent by the bot itself, and does not start with the command prefix
        if isinstance(channel, nextcord.DMChannel) and message.author != client.user and not message.content.startswith(os.getenv("BOT_PREFIX")):
            try: 
                #   Display typing effect while the bot is preparing a response
                async with channel.typing():
                    #   This sends the request to the Carter API and wait for a response
                    response = requests.post(
                        "https://api.carterlabs.ai/api/chat",
                        headers={
                            "Content-Type": "application/json"
                        },
                        #   Provide necessary information to the Carter API
                        data=json.dumps({
                            #   User Input
                            "text": message.content,
                            #   Your Carter API Key
                            "key": os.getenv("CARTER_TOKEN"),
                            #   User Identifier, used to remember information about the user
                            "user_id": message.author.id
                        })
                    )

                    #   Load the response data from Carter API
                    response_data = response.json()

                    #   Extract the response from Carter's output
                    response_text = response_data['output']['text']

                    #   Send Carter's response as a reply to the original message, without mentioning the author
                    await message.reply(response_text, mention_author=False)

            #   Handle any exceptions that occur
            except Exception as err:
                await channel.send(f"There was an Error: {err}")

        #   Continue processing predefined Discord Bot commands after handling the message from Carter API
        await client.process_commands(message)

#   Just an example command that responds to the "ping" command with the bot's latency
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency, 1)}ms") 

#   Run the bot using the Discord token from the environment variables
client.run(os.getenv("DISCORD_TOKEN"))