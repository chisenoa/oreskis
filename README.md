<p align = "center">
  <img title = "Banner" src = "https://i.hizliresim.com/r8g1cg8.png" onclick="return false width = "750px">
</p>

If you need help you can contact me [here](https://github.com/chisenoa/oreskis/issues) 🪐

## Requirements
- Python 3.6 and up - https://www.python.org/downloads/
- git - https://git-scm.com/download/

## Useful to always have
Keep [this](https://discordpy.readthedocs.io/en/latest/) saved somewhere, as this is the docs to discord.py@rewrite.
All you need to know about the library is defined inside here, even code that I don't use in this example is here.

## How to setup
1. Make a bot [here](https://discordapp.com/developers/applications/me) and grab the token

![Image_Example1](https://i.hizliresim.com/5grlh84.png)

2. Rename the TOKEN in **oreskis.py**, then fill in the required spots, such as token, prefix and game

3. To install what you need, do **pip install -r requirements.txt**<br>
(If that doesn't work, do **python -m pip install -r requirements.txt**)<br>
`NOTE: Use pip install with Administrator/sudo`

4. Start the bot by having the cmd/terminal inside the bot folder and type **python oreskis.py**

5. You're done, enjoy your bot!

## FAQ
Q: I don't see my bot on my server!<br>
A: Invite it by using this URL: https://discordapp.com/oauth2/authorize?client_id={CLIENT_ID}&scope=bot<br>
Remember to replace **CLIENT_ID** with your bot client ID

Q: There aren't that many commands here...<br>
A: Yes, I will only provide a few commands to get you started, maybe adding more later.

# Optional tools
### Flake8
Flake8 is a tool that helps you keep your code clean. Most coding softwares will have a plugin that supports this Python module so it can be integrated with your IDE. To install it, simply do `pip install flake8`. If you're using python 3.7, install by doing `pip install -e git+https://gitlab.com/pycqa/flake8#egg=flake8`

### PM2
PM2 is an alternative script provided by NodeJS, which will reboot your bot whenever it crashes and keep it up with a nice status. You can install it by doing `npm install -g pm2` and you should be done.
```
# Start the bot
pm2 start pm2.json

# Tips on common commands
pm2 <command> [name]
  start oreskis.py    # Run the bot again if it's offline
  list                    # Get a full list of all available services
  stop oreskis.py     # Stop the bot
  reboot oreskis.py   # Reboot the bot
```

### Docker
Docker is an alternative to run the bot 24/7 and always reboot again whenever it crashed. You can find the install manual [here](https://docs.docker.com/install/). You don't *have* to get it, but if you're used to having Docker, it's available at least.
```
# Build and run the Dockerfile
docker-compose up -d --build

# Tips on common commands
docker-compose <command>
  ps       # Check if bot is online or not (list)
  down     # Shut down the bot
  reboot   # Reboot the bot without shutting it down or rebuilding
  logs     # Check the logs made by the bot.
```

### Repl.it
You can run this on [Repl.it](https://repl.it/)! Make sure to setup **oreskis.py** in the way stated above.
