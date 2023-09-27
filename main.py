import discord
from bot_logic import  gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('!deleteme'):
        msg = await message.channel.send('I will delete myself now...')
        await msg.delete()
    elif message.content.startswith('$createpass'):
        await message.channel.send(gen_pass(8))
    else:
        await message.channel.send(message.content)

@client.event
async def on_message_delete(message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)

client.run("MTE1MTUwMDQ4OTc4NDA0NTY2MQ.GIfVsr.SEjp0Fv8HvE3w_a1ANQx_8YCQGtdz8jL-ZLwqQ")
