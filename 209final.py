from random import *

textBreak = '----------------------------------------------------------------------------\n'
shortBreak = '----------------\n'
class intro:
    def __init__(self):
        print('''
        ________
        \______ \   ____   _____   ____   ____
         |    |  \_/ __ \ /     \ /  _ \ /    \\
         |    `   \  ___/|  | |  (  |_| )   |  \\
        /_______  /\___  >__|_|  /\____/|___|  /
                \/     \/      \/            \/
        ________                          __
        \_____  \  __ __   ____   _______/  |_
         /  / \  \|  |  \_/ __ \ /  ___/\   __\\
        /   \_/.  \  |  /\  ___/ \___ \  |  |
        \_____\ \_/____/  \___/   ____/  |__|
               \__|
               
               by Rakib Ahamed''')
        x = input('\n\t\tpress any key to begin')

        print('''\n\n\n
----------------------------------------------------------------------------

A demon lurks in the forest...

The king has placed a bounty on its head.

Slay the demon and return its head to the king and collect your reward.''')

        x = input('\n\t\tPress any key to continue...')
        print('''
----MOVE COMMANDS----
w = move north on map
s = move south on map
d = move east on map
a = move west on map
m = show map
i = inventory
p = player Stats
''')
        x = input('\n\t\tPress any key to continue...')

#Map for player
class mapText:
    def show():
        print('''
0 1 2 3 4 5 
1 - H - X X 
2 C T F X X 
3 - S - X X 

H=Hospital
C=Castle
T=Town Center
F=Forest Entrance
X=Danger!
''')
        
#ITEM CLASS: general item class all items inherit from
class item:
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

    def __str__(self):
        return "{}\n-----\nDesc: {}\nValue: {}".format(self.name, self.desc, self.value)

#weapon class adds damage to ITEM super class
class weapon(item):
    def __init__(self, name, desc, value, damage):
        self.damage = damage
        super().__init__(name, desc, value)
    def __str__(self):
        return "{}\n-----\nDesc: {}\nValue: {}\nDamage: {}".format(self.name, self.desc, self.value, self.damage)

#weapon classes giving each attribute unique values.
class shortSword(weapon):
    def __init__(self):
        super().__init__(name = 'Short Sword', desc = 'Size isnt everything',value = 10,damage = 5)
class longSword(weapon):
    def __init__(self):
        super().__init__(name = 'Long Sword', desc = 'Big F*cking Sword', value=15,damage = 10)
class iSword(weapon):
    def __init__(self):
        super().__init__(name = 'iSword', desc = 'Great for cutting apples', value=20 , damage = 50)
class Gold(item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name = 'Gold', desc = 'Coin used to purchase things', value = self.amount)

#Potion subclass of item, adds Healing attribute         
class potion(item):
    def __init__(self, name, desc, value, healing):
        self.healing = healing
        super().__init__(name, desc, value)
#potion classes for different types of potions with different values.
class smallPotion(potion):
    def __init__(self):
        super().__init__(name = 'Small Potion' , desc = 'restores 25 missing health', value = 5, healing = 25)
class bigPotion(potion):
    def __init__(self):
        super().__init__(name = 'Big Potion' , desc = 'restores 50 missing health', value = 8, healing = 50)
#armor class inherits from item class, adds armor value
class armor(item):
    def __init__(self, name, desc, value, armor):
        self.armor = armor
        super().__init__(name, desc, value)
    def __str__(self):
        return "{}\n-----\nDesc: {}\nValue: {}\nArmor: {}".format(self.name, self.desc, self.value, self.armor)
#different classes of armor with unque values. 
class clothArmor(armor):
    def __init__(self):
        super().__init__(name='Cloth Armor' , desc = 'Wimpy Armor' , value = 100 , armor = 1 )
class leatherArmor(armor):
    def __init__(self):
        super().__init__(name='Leather Armor', desc= 'Pretty Good Protection', value= 20, armor = 3)
class metalArmor(armor):
    def __init__(self):
        super().__init__(name='Metal Armor', desc='Made of Iron', value = 30, armor = 5)

#char class used to create player and monster types
class char:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0
#monster classes that inherits from char.
class goblin(char):
    def __init__(self):
        super().__init__(name='Goblin', hp = 30, damage = 10)
class werewolf(char):
    def __init__(self):
        super().__init__(name='Werewolf', hp = 50, damage = 15)
class finalBoss(char):
    def __init__(self):
        super().__init__(name='Forest Demon', hp = 100, damage = 25)

#player lass that inherits from Char but ads and inventory and armor
class player(char):
    def __init__(self, name, hp):
        self.inventory = [Gold(200),shortSword(),clothArmor(), smallPotion(),bigPotion()]
        #pulls damage value from weapon in inventory
        d = self.inventory[1]
        #armor value is pulled from inventory I.e. cloth armor
        self.armor = self.inventory[2].armor
        #demon head win condition can finish game when True
        self.demonHead = False
        super().__init__(name, hp, damage = d.damage)
    #prints char attributes 
    def __str__(self):
        return "{}\n-----\nHP: {}\nDamage: {}\nArmor: {}\nObtained Demon Head?: {}".format(self.name, self.hp, self.damage, self.armor, self.demonHead)
    #prints inventory attributes
    def printInventory(self):
        for item in self.inventory:
            print(item, '\n')
    #method uses items in player inventory from battle input. then removes them from the inventory 
    def useItem(self, item):
        if item == 1:
            pot = smallPotion()
            for i in player.inventory:
                if isinstance(i, smallPotion):
                    player.inventory.remove(i)
                    break
        if item == 2:
            for i in player.inventory:
                if isinstance(i, bigPotion):
                    player.inventory.remove(i)
            pot = bigPotion()
        print("YOU DRANK A {}!".format(pot.name))
        print("{} HP has been restored!".format(pot.healing))
        player.hp = player.hp + pot.healing
        if player.hp >100:
            player.hp = 100
#following are Areas for the player to access. 
class castle():
    def zone(self):
        print(shortBreak+'CASTLE\n'+shortBreak)
        while True:
            command = input("Submit the Demons head to the king?\ny or n \n input: ")

            if command == 'y':
                if player.demonHead:
                    Victory.vicText()
                else:
                    print("\nKing: you have not obtained the demons head! DONT WASTE MY TIME!\n")
            elif command == 'n':
                print("\nwe should continue on with our quest")
                break
            else:
                print("\ninvalid command\n")
#shop where player can purchase things. sell function does not work.
class shop():
    def __init__(self):
        self.armorInven = [leatherArmor(),metalArmor()]
        self.weaponInven = [longSword(),iSword()]
        self.itemInven= [smallPotion(),bigPotion()]
        
    def zone(self):
        print(shortBreak+'SHOP\n'+shortBreak)
        self.shopCommand()
        
    def shopCommand(self):
        
        print('1=Buy 2=Sell 3=Quit')
        com = input('Input: ')
        
        if com == '1':
            self.buy()
        elif com == '2':
            self.sell()
        elif com == '3':
            print('\nquit\n')
        else:
            print('Invalid')
            self.shopCommand()
            
    def buy(self):
        print('Shop Keeper: what are ya buyin?')
        com = input('1=Armor 2=Weapons 3=Potions 4=Back\n input: ')
        if com == '1':
            self.showArmor()
            select = input("\nEnter Item Number \n input: ")
            if select == '1' or select == '2':
                select = int(select)
                if self.goldCheck(select, self.armorInven):
                    self.buyArmor(select)
            else:
                print("\ninvalid Input\n")
                self.buy()
        elif com =='2':
            self.showWeapon()
            select = input("\nEnter Item Number \n input: ")
            if select == '1' or select == '2':
                select = int(select)
                if self.goldCheck(select, self.weaponInven):
                    self.buyWeapon(select)
            else:
                print("\ninvalid Input\n")
                self.buy()
        elif com =='3':
            self.showPot()
            select = input("\nEnter Item Number \n input: ")
            if select == '1' or select == '2':
                select = int(select)
                if self.goldCheck(select, self.itemInven):
                    self.buyPot(select)
            else:
                print("\ninvalid Input\n")
                self.buy()
        elif com == '4':
            self.shopCommand()
        else:
            self.buy()
        
    
#checks if user has available funds     
    def goldCheck(self,select, inven):
        wallet = player.inventory[0].value
        cost = inven[select-1].value
        if wallet >= cost:
            player.inventory[0].value = wallet -cost
            print('\n{} gold has been spent from your inventory'.format(cost))
            return True
        print("\nShop Keeper:\nYou dont have enough gold!!!\n")
        return False
#prints armor inventory
    def showArmor(self):
        count = 1
        for item in self.armorInven:
            print('item number: ',count,'\n', item, '\n')
            count= count+1
#upgrades armor inventory
    def buyArmor(self, select):
        if player.inventory[2]:
            print("Armor Upgraded")
            s = self.armorInven[select-1]
            player.inventory[2] = s
            player.armor = s.armor
#prints weapon inventory
    def showWeapon(self):
        count =1 
        for item in self.weaponInven:
            print('item number: ',count,'\n', item, '\n')
            count= count+1
#upgrades weapon
    def buyWeapon(self, select):
        if player.inventory[2]:
            print("Weapon Upgraded")
            s = self.weaponInven[select-1]
            player.inventory[1] = s
            player.damage = s.damage
#prints Potion inventory
    def showPot(self):
        count =1
        for item in self.itemInven:
            print(count,'\n', item, '\n')
            count= count+1
#adds potions in inventory, does not replace existing 
    def buyPot(self,select):
        s = self.itemInven[select-1]
        player.inventory.append(s)
        print("\n{} has been added to your inventory!".format(s.name))
        
    def sell(self):
        print('Ill give ya a fair price!')

#hospital zone restores player back to full health
class hospital():
    def zone(self):
        print(shortBreak+'HOSPITAL\n'+shortBreak)
        self.health()
        
    def health(self):
        print('A nurse is healing your wounds')
        print('you are restored back to full health')
        player.hp = 100
#twon center zone, prints random statemens 
class townCenter():
    def zone(self):
        print(shortBreak+'TOWN CENTER\n'+shortBreak)
        chance = randint(1,5)
        if chance ==1:
            print("This town is very vibrant and diverse!")
        elif chance ==2:
            print("...Which direction should I head next...")
        elif chance ==3:
            print("I should get moving...")
        elif chance ==4:
            print("Nice weather today")
                  
#addition zones to access 
class forest():
    def zone(self):
        print(shortBreak+'FOREST\n'+shortBreak)
        print('nothing here... i should keep moving')
        
class forestEnt():
    def zone(self):
        print(shortBreak+'FOREST ENTRANCE\n'+shortBreak)
        print('this forest sure looks spooky')
#contains a battle
class wolfDen():
    def zone(self):
        print(shortBreak+'WOLF DEN\n'+shortBreak)
        Battle.event(werewolf)
#contains battle
class goblinCamp():
    def zone(self):
        print(shortBreak+'GOBLIN CAMP\n'+shortBreak)
        Battle.event(goblin)
#final boss battle
class Boss():
    def zone(self):
        print(shortBreak+'FINAL BOSS'+shortBreak)
        Battle.event(finalBoss)
        if not finalBoss.is_alive():
            if player.demonHead:
                print("\n\nYou have already Obtained the head! return to castle!!")
            else:
                print("\n\n You have Obtained the Demon Head!")
                player.demonHead = True
#battle squence        
class Battle():

    def event(monster):
        Battle.text(monster)
        Battle.battleEvent(monster)
    def battleEvent(monster):
        while monster.is_alive() and player.is_alive():
            print('{} HP: {}. You have {} HP remaining\n'.format(monster.name, monster.hp, player.hp))

            command = input('1 = attack  2 = inventory\n  command:')
            print(textBreak)

            if command == '1':
                Battle.playerAttack(monster)
            elif command == '2':
                Battle.playerInventory(monster)
            else:
                print('INVALID')
    #uses inventory 
    def playerInventory(monster):
            hasBPot = False
            hasSPot = False
            player.printInventory()
            for i in player.inventory:
                if isinstance(i,smallPotion):
                    print('1 = Use Small Potion')
                    hasSPot = True
                if isinstance(i,bigPotion):
                    print('2 = Use Bing Potion')
                    hasBPot = True
        
            if hasSPot and hasBPot:
                invSelect = input(" Input:")
                if invSelect == '1' or invSelect == '2':
                    player.useItem(int(invSelect))
                else:
                    Battle.battleEvent(monster)
            elif hasSPot:
                invSelect = input(" Input:")
                if invSelect == '1':
                    player.useItem(int(invSelect))
                else:
                    Battle.battleEvent(monster)
            elif hasBPot:
                invSelect = input(" Input:")
                if invSelect == '2':
                    player.useItem(int(invSelect))
                else:
                    Battle.battleEvent(monster)
            else:
                Battle.battleEvent(monster)
                
                    
    def playerAttack(monster):
        chance = randint(1,10)
        if chance == 9:
            print('\nYou missed your attack!\n')
        else:
            print('\nHIT! you have damaged the beast\n')
            monster.hp = monster.hp - player.damage
        if monster.hp <= 0:
            print('\nYou have slain the {} ...' .format(monster.name))
        if monster.is_alive():
            Battle.monsterAttack(monster)      
    def monsterAttack(monster):
            chance = randint(1,16)
            if chance == 1:
                print('You dodged the incoming attack!')
            elif chance == 2:
                print('The {} missed its attack!'.format(monster.name))
            else:
                print('The {} attacked you!\n'.format(monster.name))
                player.hp = player.hp - (monster.damage - player.armor)
                
                
        
    def text(monster):
        if monster.is_alive():
            print('--BATTLE--\n')
            print('A feirce {} has threatened your life!\n'.format(monster.name))
        else:
            print('It smells of rotting {} flesh'.format(monster.name))


class Victory():
    def vicText():
        print('\n\n\n\nYou Win\n\n\n\n\n')
        exit()
class Defeat():
    def defText():
        print('\n\n\n\nYou Died\n\n\n\n\n')

#HOW THE WORLD IS ARRANGED 
map = [[None,hospital(),None,forest(),wolfDen()],
       [castle(),townCenter(),forestEnt(),forest(),Boss()],
       [None,shop(),None,goblinCamp(),forest()]
       ]

intro()
name = input(textBreak+"\nenter player name: ")
player = player(name, 100)
werewolf = werewolf()
goblin = goblin()
finalBoss = finalBoss()

x=1
y=1

#WORLD MOVE COMMANDS, THAT PREVENT USER FROM ACCESSING UNDEFINED ZONES BASED ON MAP 
while player.is_alive():
    try:
        location = map[x][y]
        location.zone()
        if player.is_alive():
            move = input("Move: ")
            if move == 'w':
                x = x-1
            elif move == 's':
                x = x+1
            elif move == 'a':
                y = y-1
            elif move == 'd':
                y = y+1
            elif move == 'm':
                mapText.show()
            elif move == 'i':
                player.printInventory()
            elif move == 'p':
                print(player)
            else:
                print('Invalid move')
    except:
        print('\n\nLooks like you cant travel in this direction')
        print('Please enter M if you need to review the map\n\n')
        if move == 'w':
            x = x+1
        elif move == 's':
            x = x-1
        elif move == 'a':
            y = y+1
        elif move == 'd':
            y = y-1
        else:
            print('Invalid move')

Defeat.defText()
