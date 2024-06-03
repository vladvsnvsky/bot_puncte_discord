
Discord Points Bot
==================

A Discord bot to manage and display points for server members. This bot allows you to add, reset, and list points for server members, and it can generate a graph showing the points distribution. Additionally, it supports adding points to multiple members at once and resetting points for everyone.

Features
--------

- Add points to server members
- Add points to multiple server members at once
- Check points of individual members
- Reset points of individual members
- Reset points for all members
- List all members and their points
- Generate and send a graph of points distribution

Prerequisites
-------------

- Python 3.8 or higher
- `discord.py` library
- `matplotlib` library
- A Discord bot token

Installation
------------

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/discord-points-bot.git
   cd discord-points-bot
   ```

2. Install dependencies:

   ```
   pip install discord.py matplotlib
   ```

3. Create the `points.json` file:

   Create an empty `points.json` file in the project directory with the following content:

   ```
   {}
   ```

4. Configure the bot token:

   Create a `keys.py` file in the project directory and add your bot token:

   ```python
   token = 'YOUR_BOT_TOKEN'
   ```

Usage
-----

1. Run the bot:

   ```
   python bot.py
   ```

2. Invite the bot to your Discord server:

   Generate an invite link from the Discord Developer Portal with the necessary permissions and invite the bot to your server.

3. Use the bot commands:

   - `!addpoints @member amount` - Add points to a member
   - `!multipleaddpoints amount @member1 @member2 ...` - Add points to multiple members
   - `!points [@member]` - Check points of a member (or yourself if no member is mentioned)
   - `!resetpoints @member` - Reset points of a member
   - `!resetpointseverybody` - Reset points of all members
   - `!listpoints` - List all members and their points
   - `!graphpoints` - Generate and send a graph of points distribution

Bot Commands
------------

### Add Points

Add points to a server member.

```
!addpoints @member amount
```

### Add Points to Multiple Members

Add points to multiple server members at once.

```
!multipleaddpoints amount @member1 @member2 ...
```

### Check Points

Check the points of a server member or yourself.

```
!points [@member]
```

### Reset Points

Reset the points of a server member.

```
!resetpoints @member
```

### Reset Points for All Members

Reset the points of all server members.

```
!resetpointseverybody
```

### List Points

List all server members and their points.

```
!listpoints
```

### Graph Points

Generate and send a graph of points distribution among members.

```
!graphpoints
```

Enabling Privileged Intents
---------------------------

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Select your application.
3. Navigate to the "Bot" section.
4. Enable the "SERVER MEMBERS INTENT" and "MESSAGE CONTENT INTENT".
5. Save the changes.


Acknowledgements
----------------

- [discord.py](https://github.com/Rapptz/discord.py) - Python library for interacting with the Discord API
- [matplotlib](https://github.com/matplotlib/matplotlib) - Comprehensive library for creating static, animated, and interactive visualizations in Python
