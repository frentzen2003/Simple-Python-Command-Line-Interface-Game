"""
Code Written By: Frentzen, Henock, Wilbur, Li YiXuan, Haobo, and Eden
"""

import pickle
from function_log import mod_log as m_log

def file_load_game():
    player_unit = pickle.load(open("player_unit.bin","rb"))
    player_coin = pickle.load(open("player_coin.bin","rb"))
    ai_unit = pickle.load(open("ai_unit.bin","rb"))
    ai_coin = pickle.load(open("ai_coin.bin","rb"))
    m_log("--------- GAME LOADED ---------")
    return (player_unit,player_coin,ai_unit,ai_coin)


def file_save_game(player_unit,player_coin,ai_unit,ai_coin):
    pickle.dump(player_unit,open("player_unit.bin","wb"))
    pickle.dump(player_coin,open("player_coin.bin","wb"))
    pickle.dump(ai_unit,open("ai_unit.bin","wb"))
    pickle.dump(ai_coin,open("ai_coin.bin","wb"))
    m_log("--------- GAME SAVED ---------")