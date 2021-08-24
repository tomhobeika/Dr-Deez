'''
tomjedi9 Deez Bot

Annoys people on your Discord by baiting them into deez nuts jokes
'''
import discord
import re
import random
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return        

        baited = False
        # Dragon
        rere = re.search('(?i)dragon' , message.content)
        if rere:
            await message.channel.send('DRAGON DEEZ NUTS ON YOUR FACE')
            baited = True

        # Bofa
        rere = re.search('(?i)bofa' , message.content)
        if rere:
           await message.channel.send('BOFA DEEZ NUTS')
           baited = True
        
        # Pudding
        rere = re.search('(?i)pudding' , message.content)
        if rere:
            await message.channel.send('PUDDING DEEZ NUTS IN YOUR MOUTH')
            baited = True

        # CD
        rere = re.search('(?i)cd' , message.content)
        if rere:
            await message.channel.send('C DEEZ NUTS')
            baited = True

        # Kenya
        rere = re.search('(?i)kenya' , message.content)
        if rere:
            await message.channel.send('KENYA FIT DEEZ NUTS IN YOUR MOUTH?')
            baited = True

        # Sea of theives
        rere = re.search('(?i)sea of theieves' , message.content)
        if rere:
            await message.channel.send('SEA OF THEIVES NUTS FIT IN YOUR MOUTH')
            baited = True

        # Candice
        rere = re.search('(?i)candice' , message.content)
        if rere:
            await message.channel.send('CANDICE DICK FIT IN YOUR MOUTH?')
            baited = True

        # Ligma
        rere = re.search('(?i)ligma' , message.content)
        if rere:
            await message.channel.send('LIGMA NUTS')
            baited = True

        # sugma
        rere = re.search('(?i)sugma' , message.content)
        if rere:
            await message.channel.send('SUGMA DICK')
            baited = True

        # Saigon
        rere = re.search('(?i)saigon' , message.content)
        if rere:
            await message.channel.send('SAIGON DEEZ NUTS')
            baited = True

        # Help
        rere = re.search('(?i)!deezHelp' , message.content)
        if rere:
            await message.channel.send('HELP ME FIT DEEZ NUTS IN YOUR MOUTH')
            baited = True

        # Phil
        rere = re.search('(?i)phil' , message.content)
        if rere:
            await message.channel.send('PHIL UP DEEZ NUTZ')
            baited = True

        # Crisis
        rand = random.randint(1, 50) # Generates a number between 1 and 50 every time a discord message is sent
        easterEgg = 0
        if rand == 10:
        	easterEgg = easterEgg + 1
        if baited == True:
        	easterEgg = easterEgg + 1

        print("Rand: "+str(rand)+"\nBaited: "+str(baited)+"\nTest Code: "+str(easterEgg)+"\n")

        if easterEgg == 2: # 1 in 1000 messages on discord 
        	await message.channel.send('What? Did you expect a deez joke? Did you expect for me to take what you\'ve said and turn it into some juvenile pun? I am a fucking DOCTOR for Christ\'s sake. I have a PHD. And you expect me, an esteemed medical professional to say \"deez nuts\". Shut up.')
        	

            
client = MyClient()
client.run('')
