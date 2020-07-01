import discord

# server id = 727418594157133824
# NTG server id = 561069488238231552

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
gmTime = "TBD"
boardMeetingTime = "TBD"
eventMeetingTime = "TBD"
PRMeetingTime = "TBD"
marketingMeetingTime = "TBD"

client = discord.Client()


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "memeing":
            await channel.send(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(727418594157133824)

    if message.content == "!help":
        embed = discord.Embed(title="BOT functinos", description="I am ur best fren")
        embed.add_field(name="!hello", value="Greets the user.")
        embed.add_field(name="!users", value="Prints number of users.")
        embed.add_field(name="!meeting", value="Show all meeting times.")
        await message.channel.send(content=None, embed=embed)

    elif message.content.find("!hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi
    elif message.content == "!users":
        await message.channel.send(f""" # of Members: {id.member_count}""")
    elif message.content == "!meeting":
        await message.channel.send(f""" General meeeting: {gmTime}""")
        await message.channel.send(f""" Board meeeting: {boardMeetingTime}""")
        await message.channel.send(f""" Event meeeting: {eventMeetingTime}""")
        await message.channel.send(f""" PR meeeting: {PRMeetingTime}""")
        await message.channel.send(f""" Marketing meeeting: {marketingMeetingTime}""")


client.run(token)