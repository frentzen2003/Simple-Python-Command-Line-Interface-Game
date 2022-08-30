"""
Code Written By: Frentzen, Henock, Wilbur, Li YiXuan, Haobo, and Eden
"""

# IMPORT

import random

from termcolor import colored

# OWN PACKAGE

from function_log import mod_log as m_log

class Units: # CLASS FOR PLAYER

    def __init__(self,Player,Player_Coin,AI,AI_Coin):
        self.__Player = Player
        self.__Player_Coin = Player_Coin
        self.__AI = AI
        self.__AI_Coin = AI_Coin

    def append_player(self,unit_name,mode):
        self.__Player[unit_name] = mode

    def return_player_unit(self):
        return self.__Player

    def return_coin(self,type):
        if type == "p": return self.__Player_Coin
        if type == "a": return self.__AI_Coin

    def coin_sub(self,state):
        if state == "p": self.__Player_Coin = self.__Player_Coin - 20
        if state == "a": self.__AI_Coin = self.__AI_Coin - 20

    def append_ai(self,unit_name,mode):
        self.__AI[unit_name] = mode

    def return_ai_unit(self):
        return self.__AI

    def logic_attack(self,type,atk,enemy):
        bonus = 0

        if type == "p": # PLAYER TO ATTACK
            Damage = self.__Player[atk]['ATK'] - self.__AI[enemy]['DF'] + random.randint(-5,10)
            self.__AI[enemy]["HP"] = self.__AI[enemy]["HP"] - Damage
            self.__Player[atk]['EXP'] = self.__Player[atk]['EXP'] + abs(Damage)
            self.__AI[enemy]["EXP"] = self.__AI[enemy]["EXP"] + self.__AI[enemy]["DF"]

            if Damage > 10:
                bonus = int(self.__AI[enemy]["EXP"] * 20 / 100)
                self.__AI[enemy]["EXP"] = self.__AI[enemy]["EXP"] + bonus

            if Damage <= 0:
                bonus = int(self.__AI[enemy]["EXP"] * 50 / 100)
                self.__AI[enemy]["EXP"] = self.__AI[enemy]["EXP"] + bonus


        if type == "a": # AI TO ATTACK
            Damage = self.__AI[atk]['ATK'] - self.__Player[enemy]['DF'] + random.randint(-5,10)
            self.__Player[enemy]["HP"] = self.__Player[enemy]["HP"] - Damage
            self.__AI[atk]['EXP'] = self.__AI[atk]['EXP'] + abs(Damage)
            self.__Player[enemy]["EXP"] = self.__Player[enemy]["EXP"] + self.__Player[enemy]["DF"]

            if Damage > 10:
                bonus = int(self.__Player[enemy]["EXP"] * 20 / 100)
                self.__Player[enemy]["EXP"] = self.__Player[enemy]["EXP"] + bonus

            if Damage <= 0:
                bonus = int(self.__Player[enemy]["EXP"] * 50 / 100)
                self.__Player[enemy]["EXP"] = self.__Player[enemy]["EXP"] + bonus


        if type == "p": self.units_exp_checker(atk,enemy) # for player exp
        if type == "a": self.units_exp_checker(enemy,atk) # for ai exp

        if type == "p": self.bound_check(atk,enemy) # for player upper lower bound check
        if type == "a": self.bound_check(enemy,atk) # for ai upper lower bound check

        if type == "p": coin = self.add_coin("p",Damage) # add coin
        if type == "a": coin = self.add_coin("a",Damage) # add coin

        if type == "p": dead = self.partial_check("p",enemy) # for player partial check check
        if type == "a": dead = self.partial_check("a",enemy) # for ai partial check


        if dead == None:
            if type == "p" : attack_result(atk,enemy,Damage,self.__AI[enemy]["HP"],self.__Player[atk]['EXP'],self.__AI[enemy]['EXP'],bonus,"AI selected unit",coin) # print result
            if type == "a" : attack_result(atk,enemy,Damage,self.__Player[enemy]["HP"],self.__AI[atk]['EXP'],self.__Player[enemy]['EXP'],bonus,"Player selected unit",coin) # print result

    def units_exp_checker(self,atk,enemy):

        if self.__Player[atk]["EXP"] >= 100:
            self.__Player[atk]["LVL"] +=1
            self.__Player[atk]["EXP"] = self.__Player[atk]["EXP"] - 100
            print(colored(m_log("Player level up %s " % self.__Player[atk]["LVL"]),"green"))

        if self.__AI[enemy]["EXP"] >= 100:
            self.__AI[enemy]["LVL"] +=1
            self.__AI[enemy]["EXP"] = self.__AI[enemy]["EXP"] - 100
            print(colored(m_log("AI level up %s" % self.__AI[enemy]["LVL"]),"green"))

    def bound_check(self,atk,enemy):
        #CHECK UPPER BOUNDS

        if self.__AI[enemy]["EXP"] <= 0:
            self.__AI[enemy]["EXP"] = 0
        if self.__Player[atk]["EXP"] <= 0:
            self.__Player[atk]["EXP"] = 0

        if self.__AI[enemy]["HP"] >= 100:
            self.__AI[enemy]["HP"] = 100
        if self.__Player[atk]["HP"] >= 100:
            self.__Player[atk]["HP"] = 100

    def add_coin(self,type,Damage):

        bonus = abs(Damage) % 2 + 5

        if type == "p":
            self.__Player_Coin = bonus + self.__Player_Coin

        if type == "a":
            self.__AI_Coin = bonus + self.__AI_Coin

        return bonus

    def partial_check(self,type,enemy):
        if type == "p":
            if self.__AI[enemy]["HP"] <= 0:
                print(colored(m_log("AI unit with the name %s is destroyed" % enemy),"red"))
                tmp_file = self.__AI[enemy]
                del self.__AI[enemy]
                return tmp_file

        if type == "a":
            if self.__Player[enemy]["HP"] <= 0:
                print(colored(m_log("Player unit with the name %s is destroyed" % enemy),"red"))
                tmp_file = self.__Player[enemy].copy()
                del self.__Player[enemy]
                return tmp_file


    def whole_check(self):
        if len(self.__Player) == 0:
            return (True,"AI")
        if len(self.__AI) == 0:
            return (True,"Player")
        else: return (False,"None")
    
    def return_p_len(self):
        return len(self.__Player)

    def return_a_len(self):
        return len(self.__AI)
    
    def data_loader_function(self,player_unit,player_coin,ai_unit,ai_coin):
        self.__Player = player_unit
        self.__Player_Coin = player_coin
        self.__AI = ai_unit
        self.__AI_Coin = ai_coin

U = Units({},0,{},0)


def call_player():
    player_unit = U.return_player_unit()
    player_coin = U.return_coin("p")
    print(colored(m_log("**********************"),"red"))
    print(colored(m_log("PLAYER UNIT"),"red"))
    for k,x in player_unit.items():
        print(colored(m_log(str(k) + " : " +  str(x)),"blue")) # just to test the code

    print(m_log(""))
    print(colored(m_log("Player has %i coin" % player_coin),"green"))
    print(colored(m_log("**********************"),"red"))
    print(m_log(""))

    return player_unit

def call_ai():
    ai_unit = U.return_ai_unit()
    ai_coin = U.return_coin("a")
    print(colored(m_log("**********************"),"red"))
    print(colored(m_log("AI UNIT"),"red"))
    for k,x in ai_unit.items():
        print(colored(m_log(str(k) + " : " +  str(x)),"blue")) # just to test the code

    print(m_log(""))
    print(colored(m_log("AI has %i coin" % ai_coin),"green"))
    print(colored(m_log("**********************"),"red"))
    print(m_log(""))

    return ai_unit

def return_generate_unit(): # GENERATE RANDOM CHARACTER UNIT

    Warrior = {'HP':100,'ATK':int(random.randint(5,20)),'DF':int(random.randint(1,10)),'EXP':0,'LVL':1}
    Tanker  = {'HP':100,'ATK':int(random.randint(1,10)),'DF':int(random.randint(5,15)),'EXP':0,'LVL':1}
    return (Warrior,Tanker)

def all_unit_init():

    from function_c import clear_screen,error_call,game_rule # IMPORT PACKAGE
    from time import sleep
    while True:

        clear_screen() # TOO CLEAR SCREEN

        print(colored(m_log("Please enter the number of unit to be played | Max unit is %s" % game_rule()),"green"))
        try:
            unit_number_input = int(m_log(input())) # GET INPUT FOR TOTAL NUMBER OF UNIT TO START THE GAME
            if unit_number_input <= game_rule(): break
        except:
            error_call()
        error_call()

        sleep(2)

    print(colored(m_log("Value succesful to be added, Player and AI will start with %i in battle" % unit_number_input),"green"))

    player_init(unit_number_input) # PLAYER INIT FUNCTION

    clear_screen()

def instruction_init(warrior,tanker): # PRINT INSTRUCTION

    print(colored(m_log("**********************"),"red"))
    print(colored(m_log("Character List"),"green"))
    print(colored(m_log("WARRIOR [0] = " + str(warrior)),"yellow"))
    print(colored(m_log("TANKER  [1] = " + str(tanker)),"yellow"))
    print(colored(m_log("**********************"),"red"))

def player_init(unit_number_input): # INIT START ADDING UNIT

    from function_c import clear_screen # IMPORT PACKAGE

    clear_screen() # CLEAR SCREEN

    add_unit(unit_number_input,"p") # ADD UNIT (FOR PLAYER)
    add_unit(unit_number_input,"a") # ADD UNIT (FOR AI)

def add_unit(total,user):
    if user == "a": # FOR AI TO ADD UNIT
        ai_add_unit(total)

    if user == "p": # FOR PLAYER TO ADD UNIT
        player_add_unit(total)

def ai_name_generator():
    import random
    AI_name = ""
    AI_number = random.randint(0,99)
    if AI_number < 10 : AI_name = "AI0" + str(AI_number)
    else: AI_name = "AI" + str(AI_number)
    return AI_name

def ai_unit_generate():

    import random

    AI_selection = random.randint(0,1)
    return AI_selection

def ai_add_unit(total):

    from function_c import clear_screen
    from time import sleep

    number = 0
    unit_mode_desc = ""
    
    for i in range(total):
        number+=1
        tmp_warrior, tmp_tanker = return_generate_unit() # RETURN THE CHARACTER DATA FOR EACH LOOP SESSION

        while True:

            sleep(1)
            clear_screen() # TO CLEAR SCREEN
            
            warrior,tanker = tmp_warrior.copy(),tmp_tanker.copy() # COPY TMP FILE TO PERMANENT
            instruction_init(warrior,tanker)

            print(colored(m_log("AI turns to add unit"),"green"))
            print(m_log(""))

            print(colored(m_log("Please enter the name for your unit %i" % number),"green"))
            unit_name = m_log(ai_name_generator())
            print(colored(m_log("Unit %i with the name %s is confimed!" % (number,unit_name)),"green"))
            print(m_log(""))
            print(colored(m_log("Please enter the ('0' as warrior / '1' as tanker) for your unit %i" % number),"green"))

            unit_mode = ai_unit_generate()
            if unit_mode == 0: unit_mode_desc = "WARRIOR"
            else: unit_mode_desc = "TANKER"

            print(colored(m_log("Unit %i with the character %s is confimed!" % (number,unit_mode_desc)),"green"))
            append_unit("a",unit_name,unit_mode,warrior,tanker)
            break

def player_add_unit(total): # APPEND UNIT IN THE GAME

    # IMPORT PACKAGE

    from function_c import clear_screen,function_exit,error_call
    from time import sleep

    number = 0
    unit_name = ""
    unit_mode = 0
    unit_mode_desc = ""

    for i in range(total):

        number+=1
        tmp_warrior, tmp_tanker = return_generate_unit() # RETURN THE CHARACTER DATA FOR EACH LOOP SESSION

        while True:

            sleep(1)
            clear_screen() # TO CLEAR SCREEN

            warrior,tanker = tmp_warrior.copy(),tmp_tanker.copy() # COPY TMP FILE TO PERMANENT
            instruction_init(warrior,tanker)

            print(colored(m_log("Player turns to add unit"),"green"))
            print(m_log(""))

            print(colored(m_log("Please enter the name for your unit %i or enter 'Q' or 'q' to exit the game" % number),"green"))
            unit_name = str(m_log(input()))

            if unit_name == "Q" or unit_name == "q": function_exit()

            print(colored(m_log("Unit %i with the name %s is confimed!" % (number,unit_name)),"green"))
            print(m_log(""))
            print(colored(m_log("Please enter the ('0' as warrior / '1' as tanker) for your unit %i" % number),"green"))


            try:
                unit_mode = int(m_log(input()))
                if unit_mode in [0,1]:
                    if unit_mode == 0: unit_mode_desc = "WARRIOR"
                    else: unit_mode_desc = "TANKER"
                    print(colored(m_log("Unit %i with the character %s is confimed!" % (number,unit_mode_desc)),"green"))
                    append_unit("p",unit_name,unit_mode,warrior,tanker)
                    break
                else: error_call()
            except ValueError:
                error_call()

def append_unit(user,unit_name,unit_mode,warrior,tanker): # INPUTED TO THE DICTIONARY FOR BOTH PLAYER AND AI

    if user == "a":

        if unit_mode == 1: U.append_ai(unit_name,tanker)
        if unit_mode == 0: U.append_ai(unit_name,warrior)

    if user == "p":

        if unit_mode == 1: U.append_player(unit_name,tanker)
        if unit_mode == 0: U.append_player(unit_name,warrior)

def attack_function(user,key_p,key_a):
    if user == "p": function_attack("p",key_p,key_a)
    if user == "a": function_attack("a",key_a,key_p)

num = 1

def function_attack(usr,key_p,key_a):

    global num

    from function_c import clear_screen,function_exit,error_call
    from time import sleep
    clear_screen()
    print(colored(m_log("ROUND %s" % num),"green"))
    print(m_log(""))
    if usr == "p": # PLAYER TO ATTACK
        while True: # CHOOSE UNIT TO ATTACK
            sleep(3)
            clear_screen()
            call_player()
            call_ai()
            print(colored(m_log("Please enter your unit to attack or enter 'Q' or 'q' to exit"),"green"))
            try:
                attacker_unit = m_log(input())
                print(m_log(""))
                if attacker_unit == "Q" or attacker_unit == "q": function_exit()
                if attacker_unit in key_p:
                    print(colored(m_log("Player have choose %s to attack" % attacker_unit),"green"))
                    print(m_log(""))
                    break
                else: error_call()
            except ValueError:
                error_call()
            
        while True: #CHOOSE UNIT TO BE DESTROYED
            sleep(1)
            clear_screen()
            call_player()
            call_ai()

            print(colored(m_log("Please enter the enemy unit to be attacked or enter 'Q' or 'q' to exit"),"green"))
            try:
                enemy_unit = m_log(input())
                print(m_log(""))
                if enemy_unit == "Q" or enemy_unit == "q": function_exit()
                if enemy_unit in key_a:
                    print(colored(m_log("Player have choose %s to be attacked" % enemy_unit),"green"))
                    print(m_log(""))
                    break
                else: error_call()
            except ValueError:
                error_call()
        U.logic_attack("p",attacker_unit,enemy_unit)


    if usr == "a": # AI TO ATTACK   key_a , key_p == key_p (ai), key_a (player)

        while True: # CHOOSE UNIT TO ATTACK

            clear_screen()
            call_player()
            call_ai()

            print(colored(m_log("Please enter your unit to attack or enter 'Q' or 'q' to exit"),"green"))
            attacker_unit = ai_attack_unit_picker() # AI CHOOSE THEIR UNIT
            print(m_log(""))
            if attacker_unit in key_p: # KEY_P HERE IS BELONGS TO AI | AS THERE WAS A SWITCH SYSTEM
                print(colored(m_log("AI have choose %s to attack" % attacker_unit),"green"))
                print(m_log(""))
                break # here
            print("error here")
            sleep(3)
            clear_screen()
            call_player()
            call_ai()
        while True: #CHOOSE UNIT TO BE DESTROYED

            sleep(3)
            clear_screen()
            call_player()
            call_ai()

            print(colored(m_log("Please enter the enemy unit to be attacked or enter 'Q' or 'q' to exit"),"green"))
            enemy_unit = ai_enemy_retrieve_picker()
            print(m_log(""))
            if enemy_unit in key_a:
                print(colored(m_log("AI have choose %s to be attacked" % enemy_unit),"green"))
                print(m_log(""))
                break
            sleep(3)
            clear_screen()
        num = num + 1
        U.logic_attack("a",attacker_unit,enemy_unit)

def ai_attack_unit_picker():
    ai_units = list(U.return_ai_unit().keys())
    ai_selected_num = random.randint(0,len(ai_units)-1)
    ai_selected = ai_units[ai_selected_num]
    return ai_selected

def ai_enemy_retrieve_picker():
        lowest = ""
        unit_list = U.return_player_unit()
        for i in unit_list.keys():
            for j in unit_list.keys():
                if unit_list[i]['HP'] <= unit_list[j]['HP']:
                    lowest = i
        return lowest

def attack_result(atk,enemy,Damage,enemy_health,atk_exp,enemy_exp,bonus,type,gain_coin):

    from function_c import clear_screen
    from time import sleep

    sleep(2)

    clear_screen()

    call_player()
    call_ai()

    print(colored(m_log("***************"),"red"))

    print(colored(m_log("%s has attack %s" % (atk,enemy)),"green"))
    print(colored(m_log("with a damage of %i" % Damage),"green"))
    print(colored(m_log("%s health point fall to %i hp" % (enemy,enemy_health)),"green"))
    print(colored(m_log("%s exp increase into %i xp" % (atk,atk_exp)),"green"))
    print(colored(m_log("%s exp increase into %i xp" % (enemy,enemy_exp)),"green"))
    print(colored(m_log("%s get bonus exp as much as %i xp" % (type,bonus)),"green"))
    print(colored(m_log("%s gain %i coins" % (atk,gain_coin)),"green"))

    print(colored(m_log("***************"),"red"))

    sleep(1)
    print(colored(m_log("Please press enter to continue..."),"green"))
    print(m_log(input()))
    clear_screen()

def final_checker():
    return U.whole_check()
