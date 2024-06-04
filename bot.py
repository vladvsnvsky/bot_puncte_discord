import discord
from discord.ext import commands
import json
import os
import matplotlib.pyplot as plt
import numpy as np

# Intents setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable member intent to fetch server nicknames

bot = commands.Bot(command_prefix='!', intents=intents)

# Function to generate the points file name based on the server name
def getPointsFileName(guild):
    return f"{guild.name.replace(' ', '_').replace('/', '_')}.json"

# Function to load points from file
def loadPoints(guild):
    points_file = getPointsFileName(guild)
    if os.path.exists(points_file):
        with open(points_file, 'r') as f:
            try:
                points = json.load(f)
            except json.JSONDecodeError:
                points = {}
    else:
        points = {}
    return points, points_file

# Function to save points to file
def savePoints(points, points_file):
    with open(points_file, 'w') as f:
        json.dump(points, f)

# Command to display help information about all commands
@bot.command(name='statshelp')
async def statsHelp(ctx):
    help_message = """
    **Available Commands:**
    - `!addpoints @member amount` - Add points to a member
    - `!multipleaddpoints amount @member1 @member2 ...` - Add points to multiple members
    - `!points [@member]` - Check points of a member (or yourself if no member is mentioned)
    - `!resetpoints @member` - Reset points of a member
    - `!resetpointseverybody` - Reset points of all members
    - `!listpoints` - List all members and their points
    - `!graphpoints` - Generate and send a graph of points distribution
    """
    await ctx.send(help_message)


# Command to add points
@bot.command(name='addpoints')
async def addPoints(ctx, member: discord.Member, amount: int):
    points, points_file = loadPoints(ctx.guild)
    print(f"Command received: addpoints {member} {amount}")
    if str(member.id) in points:
        points[str(member.id)] += amount
    else:
        points[str(member.id)] = amount
    savePoints(points, points_file)
    await ctx.send(f"Added {amount} points to {member.display_name}. They now have {points[str(member.id)]} points.")
    print(f"Updated points: {points}")

@bot.command(name='multipleaddpoints')
async def multyAddPoints(ctx, amount: int, *members: discord.Member):
    points, points_file = loadPoints(ctx.guild)
    print(f"Command received: addpoints {members} {amount}")
    for member in members:
        if str(member.id) in points:
            points[str(member.id)] += amount
        else:
            points[str(member.id)] = amount
    savePoints(points, points_file)
    member_names = ", ".join([member.display_name for member in members])
    await ctx.send(f"Added {amount} points to {member_names}.")
    print(f"Updated points: {points}")

# Command to check points
@bot.command(name='points')
async def checkPoints(ctx, member: discord.Member = None):
    points, _ = loadPoints(ctx.guild)
    if member is None:
        member = ctx.author
    if str(member.id) in points:
        await ctx.send(f"{member.display_name} has {points[str(member.id)]} points.")
    else:
        await ctx.send(f"{member.display_name} has no points.")

# Command to reset points
@bot.command(name='resetpoints')
async def resetPoints(ctx, member: discord.Member):
    points, points_file = loadPoints(ctx.guild)
    points[str(member.id)] = 0
    savePoints(points, points_file)
    await ctx.send(f"{member.display_name}'s points have been reset to 0.")

# Command to reset points for everyone
@bot.command(name='resetpointseverybody')
async def resetPointsEverybody(ctx):
    points, points_file = loadPoints(ctx.guild)
    for member_id in points.keys():
        points[member_id] = 0
    savePoints(points, points_file)
    await ctx.send("All members' points have been reset to 0.")

# Command to list all points
@bot.command(name='listpoints')
async def listPoints(ctx):
    points, _ = loadPoints(ctx.guild)
    if points:
        msg = "Points leaderboard:\n"
        for member_id, pts in points.items():
            member = await bot.fetch_user(int(member_id))
            msg += f"{member.display_name}: {pts} points\n"
        await ctx.send(msg)
    else:
        await ctx.send("No points to display.")

# Command to generate and send points graph
@bot.command(name='graphpoints')
async def graphPoints(ctx):
    points, _ = loadPoints(ctx.guild)
    if not points:
        await ctx.send("No points to display.")
        return

    # Generate the graph
    member_names = []
    member_points = []

    for member_id, pts in points.items():
        member = ctx.guild.get_member(int(member_id))
        if member:
            member_names.append(member.display_name)
            member_points.append(pts)

    # Create color map
    cmap = plt.get_cmap('tab20')
    colors = cmap(np.linspace(0, 1, len(member_names)))

    plt.figure(figsize=(10, 5))
    bars = plt.bar(member_names, member_points, color=colors)
    plt.xlabel('Members')
    plt.ylabel('Points')
    plt.title('Points of Members')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save the graph as an image
    graph_path = 'points_graph.png'
    plt.savefig(graph_path)
    plt.close()

    # Send the image
    await ctx.send(file=discord.File(graph_path))

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

from keys import token
bot.run(token)
