import asyncio
import discord
from discord.ext import commands
from diffusers import StableDiffusionPipeline
from dotenv import dotenv_values
import torch
from threading import Thread
import io

class StableDiffusionGenerator(Thread):
    def __init__(
        self,
        prompt: str,
        model: str,
        cuda: str,
        height: int = 512,
        width: int = 512,
        iter: int = 50,
    ):
        super().__init__()
        self.prompt = prompt
        self.model = model
        self.cuda = cuda
        self.height = height
        self.width = width
        self.iter = iter

    def run(self):
        print("Loading model")
        pipe = StableDiffusionPipeline.from_pretrained(
            self.model, torch_dtype=torch.float16
        )
        pipe.enable_xformers_memory_efficient_attention()
        pipe = pipe.to(self.cuda)
        print("Generating image")
        self.image = pipe(
            self.prompt,
            height=self.height,
            width=self.width,
            num_inference_steps=self.iter,
        ).images[0]

config = dotenv_values(".env")

description = """A little Stable Diffusion bot"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry, you cannot use that command in this channel. Go to #imagine-dream instead.")
    else:
        await ctx.send(f"An error occurred: {error}")

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
@commands.check(lambda ctx: ctx.channel.id == int(config["CHANNEL_ID"]))
async def generate(
    ctx, prompt: str, width: int = 512, height: int = 512, iter: int = 50
):
    """Stable diffusion generate"""
    await ctx.send("Ok")
    thread = StableDiffusionGenerator(
        prompt=prompt,
        # model="prompthero/openjourney",  # "andite/anything-v4.0",
        # model="dreamlike-art/dreamlike-photoreal-2.0",
        # model="prompthero/openjourney-v4",
        model="MirageML/lowpoly-world",
        cuda="cuda:0",
        # cuda="cpu",
        width=width,
        height=height,
        iter=iter,
    )
    thread.start()
    while thread.is_alive():
        await asyncio.sleep(2)
    image = thread.image
    with io.BytesIO() as image_binary:
        image.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))
    thread.join()

bot.run(config["DISCORD_TOKEN"])
