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
        nums = message.content[5:]
        g=open(str(message.author) + ".py","w")
        g.write("\nfrom manim import * \n \nclass SlantsExample(Scene): \n     def construct(self): \n            result =  " + nums + "\n            if result.is_integer(): \n                  result = int(result)\n            a = Text('" + nums + "' + '=' + str(result), font_size=90)\n            for i in range (len(a) - len(str(result)), len(a)):\n                  a[i].set_color(TEAL)\n            self.play(Create(a))")
        g.close()
        os.system("manim -pqh " + str(message.author) + ".py Output")

        time.sleep(3)
        print("/root/mount/Manim/calcbot/Media/videos/" + str(message.author) + "/1080p60/SlantsExample.mp4")
        await message.channel.send('', file =discord.File( "/root/mount/Manim/calcbot/Media/videos/" + str(message.author) + "/1080p60/SlantsExample.mp4"))
        # os.rmdir("/root/mount/manim/calcbot/media/videos/" + str(message.author))
        time.sleep(1)
        os.system("rm -rf /root/mount/Manim/calcbot/Media/videos/" + str(message.author))
        os.system("rm -rf /root/mount/Manim/calcbot/" + str(message.author) + ".py")

client.run('ODAyOTk0Mzc4OTQ3NjkwNTg2.YA3Uyg.BKELipsMKOoRbtZrHxRVrSP0--k')


# zivot s tebou je fakt vyhra 
# Ondrej Matysek 2021 nekdy v rijnu