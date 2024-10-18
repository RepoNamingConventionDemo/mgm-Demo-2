# vulnerable.py

import os

# Command Injection vulnerability
def run_command(cmd):
    os.system(cmd)

# Example of how this vulnerability could be exploited
user_input = input("Enter a command to run: ")
run_command(user_input)
