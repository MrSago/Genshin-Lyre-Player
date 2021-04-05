
from pynput import keyboard
from os import system
from sys import exit
from ctypes import windll
from time import sleep
from re import findall

startDelay = 5
keyDelay = 0.2

def readNotes(filename):
    try:
        with open(filename, "r") as f:
            return findall(r"\w+", f.read().lower())
    except IOError:
        exit("Error read notes.txt")

def startPlaying(notes):
    kb = keyboard.Controller()
    print(f"Lyre playing will start in {startDelay} seconds! Open the game and enjoy!")
    print("To stop script press Ctrl+C in console")
    sleep(startDelay)
    for i in notes:
        for j in i:
            kb.press(j)
        sleep(keyDelay)
        for j in i:
            kb.release(j)
        sleep(keyDelay)

def main():
    if not windll.shell32.IsUserAnAdmin():
        print("Please restart the script with Admin rights!")
        system("pause")
        return
    notes = readNotes("notes.txt")
    startPlaying(notes)
    
if __name__ == "__main__":
    main()

