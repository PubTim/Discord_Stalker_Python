import discord
import asyncio
from discord.ext import commands

print('Stalker V1.0 is starting up')
intents = discord.Intents.all()
client = commands.Bot(command_prefix='e!',intents=intents)

@client.event
async def on_ready():
    global target
    gilds = client.guilds
    for guild in gilds:
        print()
        try:
            target = discord.utils.get(guild.members, name="target", discriminator="0000")
            print('Target found: ', end= '')
            print(target)
            print(type(target))
        except:
            print(guild, " failed")
        
        print('Logged on as {0}!'.format(client.user))



@client.event
async def on_member_update(before, after):
    global target
    what_changed(before,after)
    # if before == target:
    #     print("error")
    # if after == target:
    #     print("error")
    # print(before.name)
    # if before.activity == None:
    #     print("no activity")
    # else:
    #     for x in before.activities:
    #         try:
    #             print("Name: {0.name} | Details: {0.details}".format(x))
    #         except:
    #             print("Name: {0.name}".format(x))
    # if after.activity == None:
    #     print("no activity")
    # else:
    #     for y in after.activities:
    #         try:
    #             print("Name: {0.name} | Details: {0.details}".format(y))
    #         except:
    #             print("Name: {0.name}".format(y))

def what_changed(before,after):
    if before.status != after.status:
        print(f"{before.name}'s status is different")
        print(before.status)
        print(after.status)
    if before.activities != after.activities:
        print(f"{before.name}'s activity is different")
        for x in before.activities:
            print("Before: ", x)
        for y in after.activities:
            print("After: ", y)
    if before.nick != after.nick:
        print(f"{before.name}'s nickname is different")
        print(before.nick)
        print(after.nick)
    if before.roles != after.roles:
        print(f"{before.name}'s roles are different")
        print(before.roles)
        print(after.roles)
    if before.pending != after.pending:
        print(f"{before.name}'s pending is different")
        print(before.pending)
        print(after.pending)

# @client.event
# async def on_user_update(before, after):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_voice_state_update(member, before, after):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_typing(channel, user, when):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_voice_state_update(member, before, after):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_invite_create(invite):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_invite_delete(invite):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_message_edit(before, after):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_message_delete():
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_reaction_add(reaction, user):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

# @client.event
# async def on_reaction_remove(reaction, user):
#     await message.channel.send("Name: {0.name} | Details: {0.details}".format(activ))

token = ''

client.run(token)