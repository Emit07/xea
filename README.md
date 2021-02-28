# SlimBot

**NOTE TO SELF DO NOT I REPEAT DO NOT PUSH BOT TOKEN**

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

## DOCUMENTATION

**NOTE the documentation is not complete**

The default prefix for slimbot is `?`. Square brackets indicate that a parameter is needed and curly brackets indicate that the parameter is optional.

### Moderation commands

* `?mute [user] {reason}`
This command disables the ability for a user to talk in a text channel. To use this command you need manage messages permission, you cannot mute an administrator.
* `?unmute [user]`
This will restore the ability for a user to send messages in text channels, just like the mute command you need the manage message permission to use this command.
* `?warn [user] {reason}`
The warn command does not have an inventory system of warns but is just a neatly formatted warn. Similar to the mute and unmute command you require the manage messages permission to use this command.
* `?clear {amount}`
The clear command will delete a specified amount of messages, if not specified a single message will be deleted. Like all the other moderation commands you require the manage messages permission to use this command.

### Polls

* `?poll [message]`
This poll command will generate a poll that staticly has three options which are, yes, no, shrug.

* `?pollx "[message]" "{option one}" "{option two}" "{option three}"`
This poll command will make a more complex poll with poll options that are entered by the user. Pollx does require a manage messages role to prevent spam. I will add a config command that will allow moderators to allow and disable certain commands for people.

## TODO

* [ ] fix bot avatar not allowing help commands to show up
* [ ] add a config command to allow and disable certain commands
* [ ] add role on join command
* [ ] add self role command
