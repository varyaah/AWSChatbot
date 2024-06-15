Customer success managers at my company have been pinging engineering often, enquiring about the status of a running ec2 instance. 
The inquiries come from a company discord server. In order to reduce the number of man-hours it would take to retrieve this information by hand,
a discord bot should be created and controlled via a python script running on the ec2 instance in question. 

Just such a thing has been created. The discord bot was given permission to send and read messages from within the channels of the discord server.
This bot’s token was then copied and stored as an environment variable in the running ec2 instance. SSHing into the instance,
I was able to copy my python script into the instance and run it. At this point the script listens constantly for discord messages.
I had difficulty using the AWS Run Command dialog – so I opted to SSH and VIM. This also allowed for quicker turnaround time when testing. 

The python script includes robust error handling – it makes sure that the necessary packages are installed by catching errors and printing out actionable feedback for future engineers.
It also checks to make sure I set the environment variables for the discord bot token and channel. Because the channel is set by an environment variable,
it means we can scale the number of ec2 instances we have and allow the discord bot to answer questions across multiple channels. 

The bot will respond to messages in the given channel from people that are not itself. It will respond to questions about the server,
a basic hello world, and an additional prompt. Any other questions will receive a generic response. 

If I were to redo the project, I would have spent more time reading and understanding the nuances of discord token management.
A critical error I made during development was pushing the token to github, resulting in discord revoking the token’s access.
Additionally, after forking a related github repository, I would have been more careful about my pr creation. This would have prevented me from opening a pr from my branch to the upstream repo! 
