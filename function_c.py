"""
Code Written By: Frentzen, Henock, Wilbur, Li YiXuan, Haobo, and Eden
"""

# IMPORT

from os import system, name
from time import sleep

# SUPPLEMENTARY PACKAGE

from random import choice
from termcolor import colored

# OWN PACKAGE

from function_log import mod_log as m_log
from unit_function import *
from function_import_export import file_load_game as f_load_game, file_save_game as f_save_game

def clear_screen():

    if name == 'nt':
        _ = system('cls')   # CHECK FOR WINDOWS SYSTEM
    else:
        _ = system('clear') # CHECK FOR LINUX AND MAC SYSTEM

def load_screen():
    num = 0
    num_percentage = 0
    while num<=5:
        clear_screen()
        print(m_log(""))
        print(colored(m_log("||    =====     =    ===\  ( )  =====  =====       "),"green"))
        print(colored(m_log("||    || ||    = =   |  |  | |  || ||  || ==       "),"green"))
        print(colored(m_log("====  =====  =     = ===/  | |  || ||  ===== ..... "),"green"))
        print(m_log(""))
        print(colored(m_log("===================================================="),"green"))
        print(colored(str(m_log("[0][0][0]")*num) + " | " + str(num_percentage) + "%","yellow"))
        print(colored(m_log("===================================================="),"green"))
        num+=1
        num_percentage +=20
        sleep(1)


def game_rule(default_value=4): # GAME RULE SET
    game_max_number = default_value
    return game_max_number

def master_start(): # BASE START OF THE GAME

    load_screen() # LOADING SCREEN

    main_choice()

def game_start(): # GAME START

    print(colored(m_log("Welcome to the RPG game"),"green"))
    print(m_log(""))
    print(colored(m_log("Please enter [1] to load save file"),"green"))
    print(colored(m_log("Please enter [0] to start a new game"),"green"))
    print(colored(m_log("Please enter [Q] to exit"),"green"))
    print(m_log(""))

def main_choice(): # START MENU

    while True:
        sleep(1) # DELAY SYSTEM RUN
        clear_screen() # CLEAR SCREEN
        game_start() # DISPLAY INSTRUCTION

        user_choice = m_log(input(m_log("Please enter your choice: ")))

        if user_choice in ["Q","q","1","0"]:
            break
        else:
            print(colored(m_log("Please enter the correct value"),"red"))

    if user_choice == "1": # LOAD AND CONTINUE GAME

        # LOAD FUNCTION TO CONTINUE
        load_file_to_system()

        continue_game()

    if user_choice == "0": # CREATE NEW GAME
        new_game()

    if user_choice == "Q" or user_choice == "q": # EXIT GAME
        function_exit()

def load_file_to_system():
    while True:
        try:
            player_unit,player_coin,ai_unit,ai_coin = f_load_game()
            U.data_loader_function(player_unit,player_coin,ai_unit,ai_coin)
            print(colored(m_log("DATA LOADED"),"red"))
            break
        except:
            print(colored(m_log("No data found | game forced to exit"),"red"))
            exit()

def new_game():
    print(m_log(""))
    user_name = str(m_log(input(m_log("Please enter your name: "))))
    print(m_log(""))
    print(colored(m_log("welcome %s to the game" % user_name),"green"))

    all_unit_init() # INITIALIZE NUMBER OF UNIT TO BE PLAYED

    continue_game()


def continue_game():


    while True:
        
        status,user = final_checker() # CHECK IF ALL THE UNIT ELIMINATED
        if status == True:
            print(m_log(""))
            print(colored(m_log("%s has won the game, congratulations!" % user),"green"))
            break

        player_unit,ai_unit = call_player(),call_ai()
        # player attack
        key_p = [i for i in player_unit.keys()]
        key_a = [i for i in ai_unit.keys()]

        menu_select = p_menu() # USER CHOICE
        sleep(1)

        if menu_select == 1: attack_function("p",key_p,key_a) # player to attack
        if menu_select == 0 and U.return_a_len() <= game_rule():
            if coin_eater("p") :
                add_unit(1,"p") # MAX 1 AND PLAYER

        status,user = final_checker() # CHECK IF ALL THE UNIT ELIMINATED
        if status == True:
            print(m_log(""))
            print(colored(m_log("%s has won the game, congratulations!" % user),"green"))
            break

        menu_select = a_menu() # AI CHOICE
        sleep(1)

        if menu_select == 1: attack_function("a",key_p,key_a) # ai to attack
        if menu_select == 0 and U.return_a_len() <= game_rule():
            if coin_eater("a") :
                add_unit(1,"a")
        
        # save ALL THE GAME DATA

        f_save_game(U.return_player_unit(),U.return_coin("p"),U.return_ai_unit(),U.return_coin("a"))

def a_menu():
    if U.return_coin("a") >=20:
        return 0
    else: return 1

def p_menu():
    while True:
        clear_screen()
        print(colored(m_log("PLAYER CHOICE"),"green"))
        print(m_log(""))
        print(colored(m_log("Please enter [1] to Attack!"),"green"))
        print(colored(m_log("Please enter [0] to add troops!"),"green"))
        print(m_log(""))
        try:
            user_select = int(m_log(input()))
            break
        except:
            error_call()

    return user_select

def coin_eater(state):
    AI_coin = U.return_coin("a")
    Player_coin = U.return_coin("p")

    if state == "a":
        if AI_coin >=20:
            U.coin_sub("a")
            print(colored(m_log("Coin succesfully deducted!"),"red"))
            return True

    if state == "p":
        if Player_coin >=20:
            U.coin_sub("p")
            print(colored(m_log("Coin succesfully deducted!"),"red"))
            return True
    print(colored(m_log("Coin insufficient !"),"red"))
    return False

def function_exit():
    print(m_log(""))
    print(colored(m_log("Game is force endded by user"),"blue","on_red"))
    exit()

def error_call():
    print(colored(m_log("VALUE INPUTED IS INVALID, PLEASE TRY AGAIN! "),"red"))