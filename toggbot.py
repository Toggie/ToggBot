#!/usr/bin/env python3

import discord
import asyncio
import subprocess
import json
import os.path
import numpy
from time import sleep

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
        return(subprocess.check_output("./scripts/%s/runScript %s" % (cmd,params),shell=True).decode('utf-8').splitlines())
    else:
        return("$writeChannel$ No such command: \"%s\"" % cmd).splitlines()

def shiftList(data):
    list=numpy.roll(data,-1)
    return(list)

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
        for i in scriptReturn:
            action=scriptReturn[0].split(None, 1)[0]
            response=" ".join(scriptReturn[0].split()[1:])
            if (action=="$writeChannel$"):
                await client.send_message(message.channel,response)
            elif (action=="$tmpWriteChannel$"): # for writing messages to be edited later
                tmp=await client.send_message(message.channel,response)
            elif (action=="$editChannel$"):
                await client.edit_message(tmp,response)
                sleep(0.5) # for timing of silly things like animations
            else:
                print("Unrecognized command: %s %s" % (action, response))
            if len(scriptReturn)>1:
                scriptReturn=shiftList(scriptReturn) # shift elements if multi-line.
    else:
        return(0)
client.run(cfgData["discord_email"],cfgData["discord_password"])
