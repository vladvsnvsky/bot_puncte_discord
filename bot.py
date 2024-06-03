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

# File to store points data
POINTS_FILE = 'points.json'

# Function to load points from file
def loadPoints():
    if os.path.exists(POINTS_FILE):
        with open(POINTS_FILE, 'r') as f:
            try:
                points = json.load(f)
            except json.JSONDecodeError:
                points = {}
    else:
        points = {}
    return points

# Function to save points to file
def savePoints():
    with open(POINTS_FILE, 'w') as f:
        json.dump(points, f)

# Load points from file
points = loadPoints()
print(f"Loaded points: {points}")

# Command to add points
@bot.command(name='addpoints')
async def addPoints(ctx, member: discord.Member, amount: int):
    print(f"Command received: addpoints {member} {amount}")
    if str(member.id) in points:
        points[str(member.id)] += amount
    else:
        points[str(member.id)] = amount
    savePoints()
    await ctx.send(f"Added {amount} points to {member.display_name}. They now have {points[str(member.id)]} points.")
    print(f"Updated points: {points}")

# Command to check points
@bot.command(name='points')
async def checkPoints(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    if str(member.id) in points:
        await ctx.send(f"{member.display_name} has {points[str(member.id)]} points.")
    else:
        await ctx.send(f"{member.display_name} has no points.")

# Command to reset points
@bot.command(name='resetpoints')
async def resetPoints(ctx, member: discord.Member):
    points[str(member.id)] = 0
    savePoints()
    await ctx.send(f"{member.display_name}'s points have been reset to 0.")

# Command to list all points
@bot.command(name='listpoints')
async def listPoints(ctx):
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

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
from keys import token
bot.run(token)
