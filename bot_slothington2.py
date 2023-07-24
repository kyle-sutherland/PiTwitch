import twitchio
import asyncio
import color
import random
import OPi.GPIO as GPIO
from alerts import led
from twitchio.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(
            token="t2j5s2axyqeis59ck9fq5r4i9ds2sb",
            prefix="?",
            initial_channels=["#Imposter_Sloth"],
        )

    spicyBizCount = 0
    spookyBizCount = 0

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def fetch_chatters_colors(
        self, user_ids: list[int], token: str | None = None
    ):
        return await super().fetch_chatters_colors(user_ids, token)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command()
    async def spicycount(self, ctx: commands.Context):
        await ctx.send(f"Spicy business count: {Bot.spicyBizCount}")

    @commands.command()
    async def spookycount(self, ctx: commands.Context):
        await ctx.send(f"Spooky business count: {Bot.spookyBizCount}")

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Call fetch_chatters_colors to get the list of colors for the chatters...
        user_ids = [message.author.id]

        colors = [
            "#0000FF",  # Blue
            "#FF7F50",  # Coral
            "#1E90FF",  # DodgerBlue
            "#00FF7F",  # SpringGreen
            "#9ACD32",  # YellowGreen
            "#008000",  # Green
            "#FF4500",  # OrangeRed
            "#FF0000",  # Red
            "#DAA520",  # GoldenRod
            "#FF69B4",  # HotPink
            "#5F9EA0",  # CadetBlue
            "#2E8B57",  # SeaGreen
            "#D2691E",  # Chocolate
            "#8A2BE2",  # BlueViolet
            "#B22222",  # Firebrick
        ]

        # get the chatters color and convert it to 16bit int format
        chatter_color_obj = []
        chatter_color_obj = await self.fetch_chatters_colors(user_ids)

        if chatter_color_obj[0].color is None or chatter_color_obj[0].color == "":
            chatter_color_obj[0].color = colors[random.randint(0, len(colors)) - 1]

        chatter_color_int = color.convert(chatter_color_obj[0].color)
        colorint_r = chatter_color_int["r"]
        colorint_g = chatter_color_int["g"]
        colorint_b = chatter_color_int["b"]
        chatterNameStyle = f"\x1b[38;2;{colorint_r};{colorint_g};{colorint_b}m\033[01m"

        # Print the contents of our message to console...
        print(chatterNameStyle + f"{message.author.name}\033[0m: {message.content}")
        # flash led purple
        led.alertPurple(3, 0.1)

        # if "loot" in message.content.casefold() and "?" not in message.content:
        #     response = "GIVE ME THE LOOT!!"
        #     await message.channel.send(response)

        # spicy_biz = ["spicy", "spicy business", "piquante"]

        # for i in spicy_biz:
        #     if i in message.content.casefold() and "?" not in message.content:
        #         Bot.spicyBizCount += 1
        #         response = "smells like some spicy business"
        #         await message.channel.send(response)

        # spooky_biz = ["spooky", "spooooky", "spoopy", "spook", "scary", "frightening"]

        # for i in spooky_biz:
        #     if i in message.content.casefold() and "?" not in message.content:
        #         Bot.spookyBizCount += 1
        #         response = "spoooooky!"
        #         await message.channel.send(response)

        # greeting = [
        #     "hello",
        #     "hi ",
        #     "hey",
        #     "what's up",
        #     "whats up",
        #     "sup",
        #     "yo ",
        #     "yoyo",
        # ]

        # for i in greeting:
        #     if i in message.content.casefold() and "?" not in message.content:
        #         response = (
        #             f"Hello {message.author.name}! Follow if you like this content"
        #         )
        #         await message.channel.send(response)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    async def cleanup(self):
        await self.logout()
        await self.close()


bot = Bot()


def main():
    try:
        bot.run()
    except KeyboardInterrupt:
        asyncio.run(bot.cleanup())
        GPIO.cleanup()


if __name__ == "__main__":
    main()

# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
# impostersloth access token: avo7vzzasmdwle1aecdkatk2zzlb8h
