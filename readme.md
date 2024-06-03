# Discord Points Bot

A Discord bot to manage and display points for server members. This bot allows you to add, reset, and list points for server members, and it can generate a graph showing the points distribution.

## Features

- Add points to server members
- Check points of individual members
- Reset points of individual members
- List all members and their points
- Generate and send a graph of points distribution

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `matplotlib` library
- A Discord bot token

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-points-bot.git
   cd discord-points-bot

2. **Install dependencies**
   pip install discord.py matplotlib

3. **Create the 'points.json' file**
    Create an empty points.json file in the project directory. The initial content will be '{}'.

4. **Configure the bot token**
    Replace 'YOUR_BOT_TOKEN' in the bot.py file with your actual Discord bot token.

## Usage
1. **Run the bot**
2. **Invite the bot on discord server**
3. **Use the bot commands:**
    !addpoints @member amount - Add points to a member
    !points [@member] - Check points of a member (or yourself if no member is mentioned)
    !resetpoints @member - Reset points of a member
    !listpoints - List all members and their points
    !graphpoints - Generate and send a graph of points distribution

**Enabling Privileged Intents**
1. Go to the Discord Developer Portal.
2. Select your application.
3. Navigate to the "Bot" section.
4. Enable the "SERVER MEMBERS INTENT" and "MESSAGE CONTENT INTENT".
5. Save the changes.




