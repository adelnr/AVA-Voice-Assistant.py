import threading

import pyttsx3 #convert text to voice
import pyaudio
import speech_recognition as sr
import os
import beepy
import webbrowser
import datetime
import pyautogui #control computer by click and move
import time  # download current time for sleep function
import pygame  # Library for running graphical interface

#########gui Face #############

class imageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile(self, filename, id=None):
        if id == None: id = filename
        self.pics[id] = pygame.image.load(filename).convert()

    def loadFromSurface(self, surface, id):
        self.pics[id] = surface.convert_alpha()

    def render(self, surface, id, position=None, clear=False, size=None):
        if clear == True:
            surface.fill((5, 2, 23))  #

        if position == None:
            picX = int(surface.get_width() / 2 - self.pics[id].get_width() / 2)
        else:
            picX = position[0]
            picY = position[1]

        if size == None:
            surface.blit(self.pics[id], (picX, picY))  #

        else:
            surface.blit(pygame.transform.smoothscale(self.pics[id], size), (picX, picY))


# Initialises the display-------------------------------------------------------
pygame.display.init()  # Initiates the display pygame
# pygame.display.set_caption(AVA)# screen = pygame.display.set_mode((400,400), pygame.RESIZABLE) #uncomment this line for smaller window
screen = pygame.display.set_mode((700, 600),
                                 pygame.RESIZABLE)  # allows fullscreen #comment this line out for smaller window
handler = imageHandler()


def display():
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/0.gif", "0")
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/1.gif", "1")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/2.gif", "2")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/3.gif", "3")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/4.gif", "4")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/5.gif", "5")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/6.gif", "6")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/7.gif", "7")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/8.gif", "8")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/9.gif", "9")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/10.gif", "10")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/11.gif", "11")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/12.gif", "12")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/13.gif", "13")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/14.gif", "14")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/15.gif", "15")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/16.gif", "16")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/17.gif", "17")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/18.gif", "18")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/19.gif", "19")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/20.gif", "20")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/21.gif", "21")  # add your own file location here

    ##########talking Image############
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/22.gif", "22")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/23.gif", "23")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/24.gif", "24")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/25.gif", "25")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/26.gif", "26")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/27.gif", "27")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/28.gif", "28")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/29.gif", "29")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/30.gif", "30")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/31.gif", "31")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/32.gif", "32")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/33.gif", "33")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/34.gif", "34")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/35.gif", "35")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/36.gif", "36")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/37.gif", "37")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/38.gif", "38")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/39.gif", "39")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/40.gif", "40")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/41.gif", "41")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/42.gif", "42")  # add your own file location here
    handler.loadFromFile("/Users/geny/Desktop/Jarvis/sphere/43.gif", "43")  # add your own file location here





def face():
    A = 0  # left and right on screen
    B = 0  # up and down on screen
    x = 700  # siz width
    y = 550  # siz High

    count = 0
    global talking
    while True:
        if talking == False:
            if count >= 21:
                count = count - 22
            img = str(count)
            handler.rander(screen, img, (A, B), True, (x, y))
            pygame.display.update(A, B, x, y)
            time.sleep(.03)
            count = count + 1
            if count == 21:
                count = 0

        elif talking == True:
            if count <= 21:
                count = count + 21
            img = str(count)
            handler.rander(screen, img, (A, B), True, (x, y))
            pygame.display.update(A, B, x, y)
            time.sleep(.03)
            count = count + 1
            if count == 43:
                count = 22

############### END GUI FACE AVA#####################

######USER#########
user = "Adel "
bot = "AVA"

#######Greeting########
def greeting_by_time():
    current_time = datetime.datetime.now().time()
    if current_time >= datetime.time(hour=0) and current_time < datetime.time(hour=12):
        speak("Good morning "+ user + "how can i help you")
    elif current_time >= datetime.time(hour=12) and current_time < datetime.time(hour=17):
        speak("Good afternoon " + user + "how can i help you")
    elif current_time >= datetime.time(hour=17) and current_time < datetime.time(hour=24):
        speak("Good evening " + user + "how can i help you")

######## before stop#########

def ask_for_more():
    speak("Is there anything else I can do for you sir?")


#######web browser######
def google_search():
    # Open the web browser to the Google search page with the query
    speak("What do you want to search for sir?")
    google_text = takecommand()
    webbrowser.open(f'https://www.google.com/search?q={google_text}')
    time.sleep(1)
    pyautogui.typewrite(google_text)
    speak("searching for...." + google_text )




#######open notes######
def open_notes_and_write():
    speak("What would you like to write in the note?")
    note_text = takecommand()
    os.system("open -a Notes")
    time.sleep(1)
    pyautogui.typewrite(note_text)
    speak("Note has been created and saved.")


####### Speak Function########
def speak(text):
    global talking
    engine = pyttsx3.init("nsss")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[33].id)
    engine.setProperty("rate", 45)
    talking = True
    print("AVA " + text + "\n")
    engine.say(text)
    engine.runAndWait()
    talking = False

#########command function#########
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        beepy.beep(sound=3)
        print("Listening...",end="")
        audio = r.listen(mic)
        beepy.beep(sound=3)
        query = ''

        try:
            print("Recognizing...",end="")
            query = r.recognize_google(audio,language='en-US')
            print(f'User said:{query}')
        except Exception as e:
            print("Exception:" + str(e))

    return query.lower()


def conversationflow():
    while True:
        said = takecommand()
        # take command
        if "hello" in said or "hi" in said or "hey" in said:
            speak("hello")
        if "how are you" in said:
            speak("am doing well, how about you?")
        if "ok" in said or "fine" in said:
            speak("great to hear that")
            speak("how can i help you today?")
        if "stop" in said:
            speak("stopping sir")
            break
        if "bye" in said or "goodbye" in said:
            speak("goodbye sir")

        if "thank you" in said:
            speak("you are welcome sir")

        if "photoshop" in said:
            speak("opening photoshop")
            os.system("open -a Adobe\ Photoshop\ 2022")
            ask_for_more()

        if "python" in said:
            speak("Opening PyCharm CE")
            os.system("open -a PyCharm\ CE")
            ask_for_more()

        if "volume up" in said:
            speak("Ok sir")
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
            ask_for_more()

        if "volume down" in said:
            speak("Ok sir")
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
            ask_for_more()

        if "sleep" in said:
            speak("Are you sure you want to put the computer to sleep?")
            confirm = takecommand()
            if "yes" in confirm:
                speak("Putting the computer to sleep")
                os.system("shutdown /s /t 0")

        if "play music" in said:
            speak("Ok sir, opening Spotify")
            webbrowser.open(f'https://open.spotify.com/playlist/1rcQW7Uoun2rQFyqutyQ3d')
            ask_for_more()



        if "mute" in said:
            speak("Ok sir")
            os.system("osascript -e 'set volume output muted true'")

        if "unmute" in said:
            speak("Ok sir")
            os.system("osascript -e 'set volume output muted false'")

        if "search" in said:
            google_search()
            ask_for_more()

        if "open notes" in said or "write note" in said:
            open_notes_and_write()
            ask_for_more()








        time.sleep(1)

def main():
    t1= threading.Thread(target=face)

    display()
    #greeting_by_time()
    conversationflow()

main()
