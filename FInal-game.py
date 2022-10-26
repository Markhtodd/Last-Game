from random import randint, random

class Actors:
    list_enemies = ['troll','orc berserker','minotaur','ghoul''goblin king']
    list_bosses =['demon','dragon','hydra']
    enemy = {'goblin king':{'stamina':1,'strength':1},
    'ghoul':{'stamina':1,'strength':1},
    'troll':{'stamina':1,'strength':1},
    'orc berserker':{'stamina':1,'strength':1},
    'ogre':{'stamina':1,'strength':1},
    'minotaur':{'stamina':1,'strength':1}}
    boss = {'demon':{'stamina':3,'strength':2},
    'dragon':{'stamina':3,'strength':3},
    'hydra':{'stamina':3,'strength':1}}
   
    player = {'stamina':3,'strength':1}

    def get_enemy(self):
        return self.list_enemies[randint(0,len(self.list_enemies)-1)]

    def get_boss(self):
        return self.list_bosses[randint(0,len(self.list_bosses)-1)]

    def get_stamina_player(self):
        return self.player['stamina']

    def set_stamina_player(self,stamina):
         self.player['stamina'] = stamina

    def increase_stamina(self):
        self.player['stamina']= self.player['stamina'] + 1

    def deduct_stamina(self,character):
        if character == 'player':
            stamina = self.get_stamina_player()
            stamina = stamina - 1
            if stamina == 0:
                return False
            else:
                self.set_stamina_player(stamina)
                return True
        else:
            stamina = self.enemy[character]['stamina']
            stamina = stamina - 1
            if stamina == 0:
                return False
            else:
                self.enemy[character]['stamina']=stamina
                return True

class Boss(Actors):

    def __init__(self) -> None:
        super().__init__()

    def deduct_stamina(self,character):
        if character == 'player':
            stamina = self.player['stamina']
            stamina = stamina - 1
            if stamina == 0:
                return False
            else:
                self.player['stamina'] = stamina
                return True
        else:
            stamina = self.boss[character]['stamina']
            stamina = stamina - 1
            print(f"Boss stamina is {stamina}")
            if stamina == 0:
                return False
            else:
                self.boss[character]['stamina'] = stamina
                return True
        

class Encounters(Actors):

    cast_boss = Boss()

    def __init__(self) -> None:
        super().__init__()

    mountain_encounters = ['You come to a bridge that you must cross. \nHowever, you also come across something guarding the bridge!',
     'You have been walking for days and it has been oddly quiet... \nbut it could not last Your mountain path has been blocked!',
    'You are caught in rain and lightning when you are ambushed while running for cover!','A villager asked you for help defeating a monster that has been attacking the town.',
     'You sit on a mountain peak over looking the valley. \nIt is calm and quiet and you start to take a nap. \nOnly to find that something is waiting for you to close your eyes... \nthe nape will have to wait!',
     'The sound of crashing water has brought you to a magnificent waterfall. \nAs you stop to admire it and get a drink you see you are not the only one who has come to the water.']

    forrest_encounters = ['You are in the woods at night when you here something approaching!',
    'While walking through a forrest you find two travelers being attacked!', 'A village has been built in the tree tops. \nYou are invited to stay the night. \nAs you sleep you hear someone scream and look out to see something the in darkness attacking!',
    'You are hunting a deer for your dinner when you hear branches breaking.\nA familiar groaning sound follows! \nYou better defend yourself, or you will be dinner!']
    
    boss_encounters = ['You have arrived at the castle... \nan ominous chill runs through your spine. \nIt is dark and the air is filled with a stench that you do not know. \nYou make your way inside and the gate drops shut behind you! \nThere is no escape, win or die!']

    def decide(self):
        return random.choice(self.mountain_encounters)


    def fight(self,enemy):
        while True:
            resp = input(f'The {enemy} is making his move! \n\nYou know that it all rides on your next move. \nA side jump will go around a shield. \nA sword is too fast for a side jump, \nand shield will block a sword for an easy counter.\n\nDo you want - sword, side jump, or shield?\n')
            computer_choice = random.choice(['sword', 'side jump', 'shield'])
            if computer_choice == resp:
                print("\n\nYou both make the same move and recover!\nWhat is your next move?\n'sword', 'side jump', 'shield'")
            else:
                if resp == 'side jump' and computer_choice == 'shield':
                    print(f"\n\nHe brings up his shield but now doesn't see you jump to the side of him as your blow come down on the {enemy}!\n\n")
                    self.increase_stamina()
                    return True
                elif resp == 'shield' and computer_choice == 'sword':
                    print("\n\nHe attacks with a wide swinging blow, you shield it and counterstrike bringing him down with a crash!\n\n")
                    self.increase_stamina()
                    return True
                elif resp == 'sword' and computer_choice == 'side jump':
                    print("\n\nHe attempts to side jump" + computer_choice,f"\nyou swing your sword wide slaying the {enemy}!\n\n")
                    self.increase_stamina()
                    return True
                else:
                    print("\n\nYou attempt to " + resp + f"\nBut the {enemy} uses " + computer_choice,"\nYou have lost.\n\n")
                    not_dead = self.deduct_stamina("player")
                    if not_dead:
                        resp = input('Do you wish to fight again? y/n ')
                        if resp == 'n':
                            return True
                    else:
                        print('Game over')
                        return False


    # boss level
    def fight_boss(self,boss):
        print(f'You have arrived at the castle... \nan ominous chill runs through your spine. \nIt is dark and the air is filled with a stench that you do not know. \nYou make your way inside and the gate drops shut behind you! \nThere is no escape, win or die!.  The {boss} is attacking! \n\nThis fight is to the end... and that end could be now!')
        while True:
            resp = input(f'\nA side jump will go around a shield. \nA sword is too fast for a side jump, \nand shield will block a sword for an easy counter.\n' 'Do you want - sword, side jump, or shield?\n\n')
            computer_choice = random.choice(['sword', 'side jump', 'shield'])
            if computer_choice == resp:
                print("You both make the same move and recover!\n\nWhat is your next move?\n'sword', 'side jump', 'shield'")
            else:
                if resp == 'side jump' and computer_choice == 'shield':
                    print(f"\n\nHe brings up his shield but now doesn't see you jump to the side of him as your blow come down on the {boss}!")
                    if self.cast_boss.deduct_stamina(boss) == False: 
                        print('You win!!!!')
                        return True
                elif resp == 'shield' and computer_choice == 'sword':
                    print("\n\nHe attacks with a wide swinging blow, you shield it and counterstrike!")
                    if self.cast_boss.deduct_stamina(boss)  == False: 
                        print('You win!!!!')
                        return True
                elif resp == 'sword' and computer_choice == 'side jump':
                    print("\n\nHe attempts to side jump" + computer_choice,f"\nyou swing your sword wide hitting the {boss}!")
                    if self.cast_boss.deduct_stamina(boss) == False: 
                        print('You win!!!!')
                        return True
                else:
                    print("\n\nYou attempt to " + resp + f"\nBut the {boss} uses " + computer_choice,"\nYou have lost.")
                    if self.cast_boss.deduct_stamina("player"):
                        resp = input('Do you wish to fight again? y/n ')
                        if resp == 'n':
                            return True
                    else:
                        print('Game over')
                        return False

import random
action = Encounters()
cast = Actors()
print("Our adventurer is here! we have been waiting for you, let's get started!")

option1 = input('You are walking on a trail when you come to a fork in the road with a sign that says. \n\n"MOUNTAIN to the right and FOREST to the left." ').lower()
if option1.lower() == 'mountain':
    path = random.choice(action.mountain_encounters)
    print(path)
else:
    print(random.choice(action.forrest_encounters))
   

cnt = 0
while cnt < 4:
    will_fight=input(action.decide() + '\nDo you FIGHT? Go to the CASTLE? Or try to RUN away? ')
    if will_fight.lower()=='fight':
        enemy =cast.get_enemy()
        if action.fight(enemy)==False:
            exit(0)
        cnt = cnt + 1
    elif will_fight.lower()=='castle':
        enemy =cast.get_boss()
        if action.fight_boss(enemy)==False:
            exit(0)
        else:
            print('You have saved the kingdom!!!!')
            exit(0)
    else:
        if cast.deduct_stamina("player"):
            print("\n\nYou run away, losing one stamina.  You continue on your journey.\n")
        else:
            print("You die.  Game over")
            exit(0)



        
        

               
   
    