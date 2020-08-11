import discord
import requests
from discord.ext import commands
from discord_webhook import DiscordWebhook

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    print('BOT Started')

@client.command()
async def deletewebhook(ctx, webhook, times, *, msg):
    output = requests.get(webhook).text
    if 'Unknown Webhook' in output: 
        await ctx.send(f'Webhook doesnt exist')
    elif 'token' in output:
        webhookSend = DiscordWebhook(avatar_url='https://ixware.co/img/logo.png', username=ctx.author.name, url=webhook, content=msg)
        for loop in range(int(times)):
            webhookSend.execute()
            
        requests.delete(webhook)
        await ctx.send(f'Successfully removed the webhook `{webhook}` and spammed it `{times}` times')
    else:
        await ctx.send(f'Invalid webhook URL')
    
@client.command()
async def checkhook(ctx, webhook):
    output = requests.get(webhook).text
    if 'Unknown Webhook' in output: 
        await ctx.send(f'Webhook doesnt exist')
    elif 'token' in output:
        await ctx.send(f'`{output}`')
    else:
        await ctx.send(f'Invalid webhook URL')


client.run('TOKEN')