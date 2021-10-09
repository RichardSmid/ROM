import discord
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Connected as {0.user}'.format(client))
    print("If you don't see any errors, {0.user} is ready".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/calc'):
        nums = message.content[5:].split()
        nums.append(str(int(nums[0]) + int(nums[1])))
        g=open(str(message.author) + ".py","w")
        g.write('from manim import * \n \nclass SlantsExample(Scene): \n     def construct(self): \n         nums = ' + str(nums))
        g.write('\n         a = Text(nums[0] + "+" + nums[1] + "=" + nums[2]), font_size=90) \n         for i in range (len(a) - len(nums[2]), len(a)):\n           print(i)\n          self.play(Create(a))')
        g.close()
        os.system("manim -pqh " + str(message.author) + ".py Output")
        await message.channel.send("done")
        time.sleep(3)
        print("/root/mount/Manim/calcbot/Media/videos/" + str(message.author) + "/1080p60/SlantsExample.mp4")
        await message.channel.send('Result: ', file =discord.File( "/root/mount/Manim/calcbot/Media/videos/" + str(message.author) + "/1080p60/SlantsExample.mp4"))
        # os.rmdir("/root/mount/manim/calcbot/media/videos/" + str(message.author))
        time.sleep(1)
        os.system("rm -rf /root/mount/Manim/calcbot/Media/videos/" + str(message.author))
        os.system("rm -rf /root/mount/Manim/calcbot/" + str(message.author) + ".py")

client.run('ODAyOTk0Mzc4OTQ3NjkwNTg2.YA3Uyg.BKELipsMKOoRbtZrHxRVrSP0--k')


# zivot s tebou je fakt vyhra 
# Ondrej Matysek 2021
