"""
Code Written By: Frentzen, Henock, Wilbur, Li YiXuan, Haobo, and Eden
"""

# IMPORT

from datetime import datetime

def create_log():
    f = open("GAME_LOG.txt","w")
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    f.writelines(date + " - LOG FILE CREATED"+ "\n")
    f.close()

def mod_log(txt):
    f = open("GAME_LOG.txt","a")
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    f.writelines(date + " | " + str(txt) + "\n")
    f.close()
    return txt

def load_log():
    f = open("GAME_LOG","r")
    str = f.read()
    return str

def delete_log():
    pass