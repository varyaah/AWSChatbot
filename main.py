'''Import of the class libaries to interact with discord, import the token file, interact with operating system and 
randomly generate something.
'''
import discord
import os
from ec2_metadata import ec2_metadata 

# on first connection, these three statements output information about the ec2 server it is running on
# we include error handling for whether or not the script is running on an ec2 instance and whether the ec2_metadata lib has been installed
try:
    print(ec2_metadata.public_ipv4)
    print(ec2_metadata.region)
    print(ec2_metadata.availability_zone)
except:
    print("Please install ec2_metadata via pip install, or ensure this is running on a valid ec2 instance to proceed")
    os._exit(1)

# here we create a discord client with our discord token, stored in our ec2 instance as an env var
# we include robust error handling of both libraries and env vars
try:
    client = discord.Bot() # client
except:
    print("Please install the discord library via pip install")
    os._exit(1)

try:
    token = os.getenv('TOKEN') # stored as an env var
except:
    print("The discord token is not set as an env var. Please set TOKEN to the retrieved discord token value")
    os._exit(1)

# here, we retrieve the discord channel to listen to. This allows us to scale out to multiple ec2 instances
# all we would need to do is set the env var for the discord token, and the new channel to listen to
# and multiple bots could be listening to our discord server from multiple ec2 instances
try:
    discordChannel = os.getenv('DISCORD_CHANNEL')
except:
    print("The discord channel is not set as an env var. Please set DISCORD_CHANNEL")
    os._exit(1)


'''Event Driven programming initiating the function when the client event connects to discord.
Formatting of the string into the argument parameter with the brackets.
Creation of an output to the terminal window formatting a string.'''

# an even triggered by successful connection of the client to discord (auth with token)
@client.event
async def on_ready():
    # this print statement will retrieve the username of our client(aka the bot)
    print("Logged in as a bot: {0.user}".format(client))

'''Event driven by the client passing information needed to process. 
#Creation of 3 objects first outputting a message in a string.
Convert the objects with the string function, data type, indexing and splitting the string bc of #.'''

@client.event
async def on_message(message):
    # retrieve information from the message (who wrote it, which channel, what the message is)
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    # output that for ec2 logs
    print(f'Message {user_message} by {username} on {channel}')

    # ensures we dont read in our own messages, which could infinite loop us
    if username == str(client.user).split("#")[0]:
        return 
    
    '''If the channel name is random run a bunch of conditional
    statements that checks the string indexes and lower case values of several different strings.
    You can now just make any logic you want to. Remember, Case statements.
    '''
    
    # we are only concerned with the general channel right now. We might expand this
    if channel == discordChannel:
        if user_message.lower() == "tell me about my server!": # the string match must be in lower case
            await message.channel.send(f"The ec2 server ip is {ec2_metadata.public_ipv4}, the region is {ec2_metadata.region}, and the availability zone is {ec2_metadata.availability_zone}")       
        elif user_message.lower() == "hello world":
            await message.channel.send(f'Hello')
        elif user_message.lower() == "what should my grade on this project be": # an additional question
            await message.channel.send("An A+!")
        else:
            # handling a catch-all case
            await message.channel.send("I'm sorry, I dont understand that.")
            
#Start execution by passing the token object. Perpetually listening until killed
client.run(token)
