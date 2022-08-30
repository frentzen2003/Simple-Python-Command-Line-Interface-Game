"""
Code Written By: Frentzen, Henock, Wilbur, Li YiXuan, Haobo, and Eden
"""

# MAIN PACKAGE

import time
import os


# SUPPLEMENTARY PACKAGE

from colorama import init
from termcolor import colored

# OWN PACKAGE

import function_c as FC
from function_log import create_log as c_log
from function_log import mod_log as m_log

def end_program(start_time):

    time_exc_total = (time.time() - start_time)
    abs(time_exc_total)
    path = os.path.dirname(os.path.realpath(__file__))

    print(m_log(""))
    print(colored(m_log("* * * * * * * * * * * * * * * * * * * * *"),"red"))
    print(colored(m_log("Total runtime: %0.2f seconds" % time_exc_total),"green"))
    print(colored(m_log("Total Absolute runtime: %d seconds" % abs(time_exc_total)),"green"))
    print(colored(m_log("File directory: %s" % path),"green"))
    print(colored(m_log("Current directory: %s" % (os.getcwd())),"green"))
    print(colored(m_log("* * * * * * * * * * * * * * * * * * * * *"),"red"))
    print(colored(m_log("CODE WRITTEN BY FRENTZEN, HENOCK, WILBUR, EDEN, YIXUAN, HAOBO"),"red"))
    print(colored(m_log("* * * * * * * * * * * * * * * * * * * * *"),"red"))

def main():
    start_time = time.time() # START TIME

    c_log() # CREATE LOG FILE

    init() # INITIALIZE COLOR

    # CORE CODE START HERE

    FC.master_start() # MAIN TRIGGER

    end_program(start_time) # END PROGRAM | WITH DISPLAYING STATS

if __name__ == "__main__":
    main()