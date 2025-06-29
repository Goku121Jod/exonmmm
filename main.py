import discord
from discord.ext import commands
from discord.ui import View, Button
import json

# Load configuration
with open("config.json") as f:
    config = json.load(f)

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Needed to process text commands
intents.members = True  # Optional: future use for member data

# Bot setup
bot = commands.Bot(command_prefix="$", intents=intents)

# Button view class
class VerifyView(View):
    def __init__(self, link: str):
        super().__init__()
        self.add_item(Button(label="Verify now", style=discord.ButtonStyle.link, url=link))

@bot.command()
@commands.is_owner()
async def verify(ctx, link: str):
    print("Verify command triggered")  # Debug in terminal
    await ctx.send("Verification message sent!")  # Confirm bot is working

    embed = discord.Embed(
        title="Exon Verification required",
        description="To gain access to 🌱 **Skyleaf** you need to prove you are a human by completing verification. Click the button below to get started!",
        color=discord.Color.from_rgb(98, 0, 255)
    )
    embed.set_author(name="Exon", icon_url=config["thumbnail_url"])
    embed.set_thumbnail(url=config["thumbnail_url"])
    embed.set_image(url=config["main_image_url"])

    await ctx.send(embed=embed, view=VerifyView(link))

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

bot.run(config["token"])
