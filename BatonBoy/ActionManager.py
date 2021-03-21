import cmd
import math
import sys
from Cultist import Cultist

class ActionManager(object):
    """Manages the actions that the baton boy can make"""

    #Action Keys
    whoami_key = "!who"
    summon_key = "!summon"
    summon_shortKey = "!sum41"
    pass_key = "!pass"
    destroy_key = "!destroy"

    #Known Channels
    wiz_pig_text = 678829459759038484
    wiz_pig_voice = 499817104422207523
    sandbox_text = 823129504452182061
    sandbox_voice = 823129504904904784

    def __init__(self, client):
        self.client = client
        self.cultists = {}
        self.cultistsOrder = []
        self.summoned = False

    async def run(self, actionKey, message):
        if actionKey == self.summon_key or actionKey == self.summon_shortKey:
            await self.summonBatton(message)
            return
        if actionKey == self.whoami_key:
            await self.whoami(message)
            return
        if actionKey == self.pass_key:
            await self.passBatton(message)
            return
        if actionKey == self.destroy_key:
            await self.destroyBatton(message)
            return

    async def whoami(self, message):
        await message.channel.send("WHO AM I? WHO AM I, YOU DARE TO ASK! \n SUCH FOOLISH MORTALS, YOUR MEMORIES HAVE ALWAYS BEEN SO SHORT. \n\n\n **I AM THE BATON BOY** \n\n\n THE HERALD OF CONDUCTIVE SPEECH, OF TURN TAKING, AND SWEET AERIAL TRICKS AT THE FRONT OF PARADES.\n I AM AN OLD GOD WITH GREAT POWER, THAT I AM WILLING TO LEND TO YOU TODAY. \nIN EXCHANGE FOR MY POWER I ASK YOU FOLLOW MY THREE TENANTS: \n\n 1. MY BATON MUST BE SUMMONED(!summon) FROM THE BEYOND \n 2. THE POWER OF MY BATON MUST BE TRANSFERED(!pass) BETWEEN THOSE WHO SUMMONED IT \n 3. THE BATON MUST BE RETURNED(!destroy) FROM WHENCE IT CAME WHEN THE DEED IS DONE. \n\nEACH OF THESE TENANTS COME WITH TRIALS OF THEIR OWN, STEEL YOURSELF AND THE POWER OF THE BATON WILL BE YOURS. \n\n*shabalagoo*")

    async def summonBatton(self, message):
        self.refreshCultists()
        
        if not self.cultists:
            return

        if self.summoned == True:
            await message.channel.send("THE BATON HAS ALREADY BEEN SUMMONED!")

        if message.author.display_name not in self.cultists.keys():
            await message.channel.send("ONLY THOSE THAT JOIN THE SUMMONING CIRCLE IN THE EYES OF THE PIG WIZARD CAN PARTAKE OF THE RITUAL")
            return

        if len(self.cultists.keys()) %2 == 0:
            await message.channel.send("THE SUMMONING CAN ONLY BEGIN WHEN THE CIRCLE HAS BECOME TRULY ODD")
            return

        if message.author.display_name != self.cultistsOrder[0]:
            await message.channel.send("THE ONE WHO HAS REACHED THE TRUE MIDDLE IS THE CHOSEN. NO OTHERS CAN BEGIN THE SUMMONING")
            return

        await message.channel.send("YOUR RITUAL PLEASES ME, HOW DO YOU CHOOSE TO BRING THE BATON INTO YOUR REALM? SPEAK IT OUT LOUD SO THE OLD GODS CAN HEAR!")
        while(True):
            text = input("Y will accept. All others will allow the bot to speak\n")
            if (text == "Y"):
                break
            if (len(text) > 0):
                await message.channel.send(text)

        self.summoned = True
        self.currentCultist = message.author.display_name
        await message.channel.send("THE BATON HAS JOINED WITH YOU, {0}, YOU WILL BE ABLE TO SPEAK YOUR TRUTH. \n BUT REMEMBER THE BATON IS NOT OF THIS WORLD AND MUST BE RETURNED FROM WHENCE IT CAME, OTHERWISE MY WRATH IS A CERTAINTY".format(message.author.display_name))

    async def passBatton(self, message):
        self.refreshCultists()

        if self.summoned == False:
            await message.channel.send("THE BATON MUST BE SUMMONED TO BE PASSED, TOTAL JABRONI MOVE MORTAL")
            return

        if self.currentCultist != message.author.display_name:
            await message.channel.send("HOW CAN YOU PASS THAT WHICH YOU DON'T POSSESS? ALL POOPS NO HOOPS, THIS ONE")
            return

        cultistIndex = self.cultistsOrder.index(message.author.display_name)

        if cultistIndex >= len(self.cultistsOrder)-1:
            await message.channel.send("THE BATON HAS REACHED THE END AND MUST BE RETURNED! \n COMPLETE THE RITUAL OR FACE MY WRATH")
            return

        nextCultistIndex = cultistIndex+1
        nextCultistName = self.cultistsOrder[nextCultistIndex]

        nextCultist = self.cultists[nextCultistName]

        while(nextCultist.hasSpoken == True):
            nextCultistIndex = nextCultistIndex + 1
            nextCultist = self.cultistsOrder[nextCultistIndex]
        
        #allow for the wait before the pass message is accepted
        while(True):
            text = input("Y will accept. All others will allow the bot to speak\n")
            if (text == "Y"):
                break
            if (len(text) > 0):
                await message.channel.send(text)

        await message.channel.send("YOU MUST PASS THE BATON TO {0}, HOW WILL YOU COMPLETE THIS FEAT? \n SPEAK IT ALOUD OR JEOPARDIZE MY POWER!".format(nextCultist.name))
        while(True):
            text = input("Y will accept. All others will allow the bot to speak\n")
            if (text == "Y"):
                break
            if (len(text) > 0):
                await message.channel.send(text)

        nextCultist.hasSpoken = True
        self.cultists[nextCultist.name] = nextCultist
        self.currentCultist = nextCultist.name

        await message.channel.send("THE BATON IS YOURS {0}, USE IT'S POWER WISELY".format(nextCultist.name))

    async def destroyBatton(self, message):
        if self.currentCultist != message.author.display_name:
            await message.channel.send("HOW CAN YOU DESTROY THAT WHICH YOU DON'T POSSESS? SOMEONE SHOULD OFFER YOU A SWIFT PUNCH IN THE GUT")
            return

        await message.channel.send("SO THE TIME HAS COME FOR THE END. RETURN THE BATON TO ME AND THE POWER THAT COMES WITH IT. HOW WILL YOU DO IT, {0}?".format(message.author.display_name)) 

        while(True):
            text = input("Y will accept. All others will allow the bot to speak\n")
            if (text == "Y"):
                break
            if (len(text) > 0):
                await message.channel.send(text)
        
        await message.channel.send("AND SO IT ENDS FOR ANOTHER WEEK... \n REMEMBER THIS POWER MORTALS \n THE NEXT TIME YOU ARE TALKING OVER EACH OTHER IN YOUR 10TH ZOOM CALL OF THE DAY, OR WHEN YOUR ANNOYING FRIEND ONE-UPS ALL OF YOUR STORIES, OR YOUR FAMILY INTERRUPTS YOU FOR THE 100TH TIME TO ASK TO PESTER YOU ON SOME INANE CHORE. \n\n**THERE IS A BETTER WAY** \n\nSACRIFICE THE OFFENDERS TO THE BATON IN BLOODY JUSTICE AND WITH THAT POWER I, THE BATON BOY, WILL BRING UPON A WORLD OF ELABORATE PARADE WORTHY TWIRLS. \n\n**zawaaaaaaa**")
        sys.exit()

    def refreshCultists(self):
        refreshedCultists = {}
        refreshedCultistOrder = []

        channel = self.client.get_channel(self.wiz_pig_voice)
        for member in channel.members:
            if (member.bot == False):
                refreshedCultistOrder.append(member.display_name)
            if member.name in self.cultists.keys():
                refreshedCultists[member.display_name] = Cultist(member.display_name, self.cultists[member.display_name])
            else:
                refreshedCultists[member.display_name] = Cultist(member.display_name)
        
        self.cultists = refreshedCultists
        self.sortCultists(sorted(refreshedCultistOrder))
        
    def sortCultists(self, refreshedCultistOrder):
        self.cultistsOrder = []
        
        length = len(refreshedCultistOrder)
        for i in range(math.floor(length/2), -1, -1):
            self.cultistsOrder.append(refreshedCultistOrder[i])

        for i in range(math.ceil(length/2), length, 1):
            self.cultistsOrder.append(refreshedCultistOrder[i])

    