#!/usr/bin/env python3

import httplib2 as http
import discord
import asyncio

def fuckOff(args): # foaas functionality
    def mkPath(args): # creates REST path from arguments
        s=""
        for i in range (1,len(args)):
            s+="/%s"%args[i]
        s+="/"
        return s
    if(len(args) == 1 or args[1] == "help"):
        return("Usage: !fuckoff $args - For info visit http://www.foaas.com")
    else:
            try:
                from urlparse import urlparse
            except ImportError:
                from urllib.parse import urlparse
            headers={
                'Accept':'text/plain'
            }
            uri='http://www.foaas.com'
            path=mkPath(args)
            target=urlparse(uri+path)
            method='GET'
            body=''
            h=http.Http()
            response,content=h.request(
                    target.geturl(),
                    method,
                    body,
                    headers)
            return(content.decode('utf-8'))

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter=0
        tmp=await client.send_message(message.channel,'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author==message.author:
                counter+=1
        await client.edit_message(tmp,'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel,'Done sleeping')
    elif message.content.startswith('!fuckoff'):
        await client.send_message(message.channel,
        fuckOff(message.content.split(' ')))

client.run('email','password')
