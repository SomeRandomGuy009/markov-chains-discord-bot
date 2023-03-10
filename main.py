import discord
import markovify
import os
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.mentions and message.mentions[0] == client.user:
        text = ""
        async for msg in message.channel.history(limit=1500):
            if not msg.author.bot and 'http' not in msg.content:
                text += msg.content + "\n"
        
        model = markovify.Text(text)
        response = model.make_sentence()
        await message.channel.send(response)

client.run(os.getenv(token))
