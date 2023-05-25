
# Carter Discord Bot - Python

The Carter Discord Bot is a simple template integration that allows you to easily add AI conversation capabilities to your Discord bot using the Carter API.

## Features

- Seamless integration with the Carter API for AI-driven conversations.
- Supports Direct Messages for personalized interactions.
- Customizable command prefix to fit your server's needs.
- Easy setup and deployment using Nextcord library.


## Installation

To use this template, follow these steps:

1. Clone the repository:
```shell
  git clone https://github.com/TheKronis/Carter-API-Discord-Bot-Template.git
```

2. Go to the project directory:
```shell
  cd Carter-API-Discord-Bot-Template
```

3. Install Dependencies
```shell
  pip install -r requirements.txt
```

4. Obtain a Carter API key:
    - Sign up to [Carter Labs]("https://controller.carterlabs.ai/")
    - Create your Agent and go thru the set up process
    - Generate an API key from the Agent Dashboard

5. Obtain a Discord bot API key:
    - Go to [Discord Developers](https://discord.com/developers/applications/)
    - Click on "New Application"
    - Click on "Bot" on the left panel
    - Click "Reset Token" (Should show you your bot API key)

6. Set up enviroment variables: 
    - Open .env file
    - Add the following variables:
        ```txt
        DISCORD_TOKEN = Your Discord Token
        BOT_PREFIX = Your Desired Prefix
        CARTER_TOKEN = Your Carter Token
        ```

7. Run the bot
    ```shell
    python3 main.py
    ```
## Author

- [@TheKronis](https://www.github.com/TheKronis)

