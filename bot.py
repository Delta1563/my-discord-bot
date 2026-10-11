import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Your personal user ID lock
MY_DISCORD_ID = 895210494833598535

# Your server ID lock for instant command syncing
MY_SERVER_ID = 1555107765712723968  

@bot.event
async def on_ready():
    # This forces the bot to update the command menu in your server instantly!
    guild = discord.Object(id=MY_SERVER_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    print(f"Logged in as {bot.user.name} and synced instantly to your server!")

@bot.tree.command(name="echo", description="Private announcement echo bot")
@app_commands.describe(message="The message you want the bot to say")
async def echo(interaction: discord.Interaction, message: str):
    # Security lock: checks if the person using it is you
    if interaction.user.id != MY_DISCORD_ID:
        await interaction.response.send_message("You are not authorized to use this bot.", ephemeral=True)
        return

    # Instantly tells Discord we received the command, then posts your message cleanly
    await interaction.response.send_message("Sending...", ephemeral=True)
    await interaction.channel.send(message)

# ⚠️ REMEMBER TO PASTE YOUR NEW SECRET BOT TOKEN INSIDE THE QUOTES BELOW
bot.run('DISCORD_TOKEN')

