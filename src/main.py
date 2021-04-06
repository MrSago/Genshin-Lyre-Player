
from pynput import keyboard
from sys import exit
from ctypes import windll
from time import sleep
from re import findall

startDelay = 5
keyDelay = 0.15

def readNotes(filename):
    try:
        with open(filename, "r") as f:
            return findall(r"\w+", f.read().lower())
    except IOError:
        exit(f"Error read file {filename}")

def startPlaying(notes):
    kb = keyboard.Controller()
    print(f"Lyre playing will start in {startDelay} seconds! Open the game window and enjoy!")
    print("To stop the script press Ctrl+C in console")
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
        print("Please restart the script with Administrative rights!")
        return
    notes = readNotes("notes.txt")
    startPlaying(notes)
    
if __name__ == "__main__":
    main()

