#!/usr/bin/env python3

import discord
import asyncio
import subprocess
import json

cfgData=json.loads(open("config.json").read()) # Load config

client = discord.Client()

def runScript(args):
    def del_char(string, indexes):
        return ''.join((char for idx, char in enumerate(string) if idx not in indexes))
    botCmd = args[1:]
    cmd = botCmd.split(' ', 1)[0]
    if (len(botCmd.split())==1):
        params=" "
    else:
        params = botCmd.split(' ', 1)[1]
    return(subprocess.check_output("./scripts/%s/run.py %s" % (cmd, params), shell=True).decode('utf-8'))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        await client.send_message(message.channel,runScript(message.content))
    else:
        return(0)

client.run(cfgData["discord_email"],cfgData["discord_password"])