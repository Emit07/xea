# SlimBot

## Version 0.0.2 beta

This is SlimBot (or xea) an open source discord bot that is lightweight in nature and easy to modify. Further documentation will be provided later on. Please feel free to make a pull request and improve SlimBot.

**You can add SlimBot to your own server with [this](https://bit.ly/3jQsMBN "Add SlimBot") link.**

https://bit.ly/3jQsMBN

## Running the Bot

### Creating your Discord Bot

#### Creating the application
1. Go to the [discord developer portal](https://discord.com/developers/applications/ "discord dev portal") and click on "New Application" and Give it the name of your discord bot, this application will house the discord bot. 

#### Adding the bot

2. After you create a new application go to the "Bot" section and click on the "Add Bot" button, clicking on the add bot button will give you a warning and click on "Yes, do it!" if you have made a fresh new app for this bot. From there you can change its name and profile picture if you want.

#### Getting the Token

3. Next to the profile picture there will be buttons, you will want to copy the token and make sure that no one else knows what the token is because the will have access to the bot and possibly even the server with administrator. You will want to put this token in the environment variables. You can now run the bot however it will not be on any discord servers. 

#### Adding the bot to Servers

4. To add the bot to discord servers you will need to go to the "OAuth2" tab on the left. On the "scopes" section click on "bot", then scroll down and give the bot administrator permissions. Copy the given link and put it into a new tab of your web browser of choice. Make sure you are signed into your discord account, you can add the bot to any discord servers where you are either the owner or have administrator permissions. You are now ready to set up the rest.

### Installing dependencies 

If your global python version is not 3.x use pip3 instead of pip while following along below.

Install the follwing libraries. 

`pip install {library}`

* [x] `discord.py`
* [x] `requests`
* [x] `spongebobcase`

#### Setting up The Token

Set your environment variable to the bot token

## Features

* [x] mute and unmute users on text channels
* [x] clear text command
* [x] command to turn input text into sPoNgEbOB case
* [x] hug command that returns a gif of an anime hug to hug other user
* [x] command that pulls posts from reddit with webscraping
* [x] uptime command
* [ ] Role on join
* [ ] Self role (using reactions)
* [ ] ban and kick commands
* [ ] levels
* [ ] statistics on messages sent
* [ ] statistics for every user
* [ ] integrated discordgames
* [ ] other integrations (not sure which ones)  