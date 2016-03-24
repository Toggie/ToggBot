#!/usr/bin/env python3

import discord
import asyncio
import subprocess
import json
import os.path

cfgData=json.loads(open("../learnpython/ToggBot_Working/config.json").read()) # Load config

client=discord.Client()

def runScript(args):
    botCmd=args[1:]
    cmd=botCmd.split(' ',1)[0]
    if (os.path.isfile("./scripts/%s/runScript" % cmd)==True):
        if (len(botCmd.split())==1):
            params=" " # So that params is not null
        else: # The below quotes the arguments passed for shell sanitation
            params=' '.join('"{}"'.format(word) for word in botCmd.split(' ',1)[1].split(' '))
        return(subprocess.check_output("./scripts/%s/runScript %s" % (cmd,params),shell=True).decode('utf-8'))
    else:
        return("No such command.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        scriptReturn=runScript(message.content)
        action=scriptReturn.split(None, 1)[0]
        response=" ".join(scriptReturn.split()[1:])
        if (action=="writeChannel^_^"):
            await client.send_message(message.channel,response)
        else:
            print("Unrecognized command: %s %s" % (action, response))
    else:
        return(0)
client.run(cfgData["discord_email"],cfgData["discord_password"])
