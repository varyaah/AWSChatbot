'''Import of the clas libaries to interact with discord, import the token file, interact with operating system and 
randomly generate something.
'''
import discord
import os
import random
import requests
from os.path import join, dirname
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata 

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#Call the module. 
dotenv_path = join(dirname("__file__"), '.env')
load_dotenv(dotenv_path)

#Creation of a client object from the discord class, Bot subclass.
#Insert the token for OAuth2. wow at my improvement! clap it up.

client = discord.Bot() # client
token = os.getenv('TOKEN')

'''Event Driven programming initiating the function when the client event connects to discord.
Formatting of the string into the argument parameter with the brackets.
Creation of an output to the terminal window formatting a string.'''

@client.event #<--Fix
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

'''Event driven by the client passing information needed to process. 
#Creation of 3 objects first outputting a message in a string.
Convert the objects with the string function, data type, indexing and splitting the string bc of #.'''

@client.event
async def on_message(message):#<--Passing info into function.
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    #output, format(f) with brackets.
    print(f'Message {user_message} by {username} on {channel}')

    #Client user is the bot right? if the user is the bot.
    if username == client.user:
        print("Ignoring")
        return 
    
    '''If the channel name is random run a bunch of conditional
    statements that checks the string indexes and lower case values of several different strings.
    You can now just make any logic you want to. Remember, Case statements.
    '''
    
    if channel == "general":
        if user_message.lower() == "boomer?" or user_message.lower() == "boomer?":
            print("responding 1")
            await message.channel.send(f"Sooner! {username}") #format of string
            return #<--Fix: Returning values passed into the function.
        
        #other string options
        elif user_message.lower() == "hello world":
            print("responding 2")
            await message.channel.send(f'Sooner! {username}')
        elif user_message.lower() == "tell me a joke":
            print("responding 3")
            #3 String array, await and randomly choose index of the array. 
            jokes = ["Can someone please shed more light on how my lamp got stolen?",
                     "Why is she called llene? She stands on equal legs.",
                     "What do you call a gazelle in a lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))
            
#Start execution by passing the token object. 
client.run(token)

