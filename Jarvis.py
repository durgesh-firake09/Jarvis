import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me_initiating():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif 12 <= hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("This is JARVIS. Ready to help you, Sir !!")
    speak("This is jarvis Ready to help you Sir !!")


def wish_me_ending():
    print("\nGoing Offline...\nThanks for using me!!\nHave a Nice Day, Sir\nSee you soon...")
    speak("Going Offline... Thanks for using me!! Have a nice day sir See you soon...")


def take_command():
    # Microphone Input and string output
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        audio = rec.listen(source)

    try:
        print("Recognising...\n")
        query = rec.recognize_google(audio, language='en-in')
        print(f"User Said : {query}")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@something.com', password='your-password')
    server.sendmail('your-email@something.com', to, content)


if __name__ == '__main__':
    wish_me_initiating()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    firefox_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
    while True:
        query = take_command().lower()

        # Logic for executing tasks

        # Formalities with JARVIS

        if ('hi jarvis' in query) or ('hello jarvis' in query):
            if 'hello jarvis' in query:
                speak("Hello Sir. I am Here to help you...")

            elif 'hi jarvis' in query:
                speak("Hii Sir. I am Here to help you...")

            continue

        elif 'how are you' in query:
            speak("I am always fine. How about you Sir?")
            condition = take_command().lower()
            if 'fine' in condition:
                speak("Ohh! That's nice")
            else:
                speak("OK!!")

            speak("Then how can I help you sir?")
            continue

        elif 'who are you' in query:
            speak("I am jarvis. Your Personal Assistant. I am always ready to help you.")
            continue

        elif 'what is your name' in query:
            speak("My name is jarvis. How can I help you sir?")
            continue

        # COMMANDS FOR JARVIS START HERE

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(f"According to wikipedia")
                speak(results)

            except Exception as e:
                print(e)
                print("Sorry! Couldn't search")
                speak("Sorry! couldn't search")

        elif 'open youtube' in query:
            print("Opening YouTube...")
            speak("Opening YouTube")
            webbrowser.get(chrome_path).open_new_tab("youtube.com")

        elif 'open whatsapp' in query:
            print("In which browser should I open WhatsApp?")
            speak("In which browser should I open WhatsApp?")
            browser_name = take_command().lower()
            if 'firefox' in browser_name:
                print("Opening WhatsApp...")
                speak(f"Opening WhatsApp in {browser_name}")
                webbrowser.get(firefox_path).open_new_tab("web.whatsapp.com")
            elif 'google chrome' in browser_name:
                print("Opening WhatsApp...")
                speak(f"Opening WhatsApp in {browser_name}")
                webbrowser.get(chrome_path).open_new_tab("web.whatsapp.com")
            else:
                speak("This type of browser is not set")

        elif 'open website' in query:
            speak("Which Website Should I Open?")
            website_name = take_command().lower().replace(" ", "")
            print(f"Opening {website_name}")
            speak(f"Opening {website_name}")
            webbrowser.get(chrome_path).open_new_tab(f"{website_name}.com")

        elif 'search on chrome' in query:
            speak("What should I search?")
            search_this = take_command().lower()
            searching = search_this.replace(" ", "+")
            print("Searching...")
            speak(f"searching {search_this} on Google Chrome")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={searching}")

        elif 'play music' in query:
            try:
                music_dir = 'E:\\Favourites'
                songs = os.listdir(music_dir)
                print(songs)
                music_number = random.randint(0, len(songs)-1)
                # Random should be added here
                os.startfile(os.path.join(music_dir, songs[music_number]))

            except Exception as e:
                print(e)
                speak("Enter The correct Music Directory in the code")

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The time is {str_time}")
            speak(f"Sir, The time is {str_time}")

        elif 'open code' in query:
            try:
                print("Opening Code...")
                speak("Opening Code...")
                code_path = "C:\\Users\\user pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            except Exception as e:
                print(e)
                speak("Enter The correct Directory in the code")

        elif 'email to someone' in query:
            try:
                speak("What Should I say?")
                content = take_command()
                to = "someone@something.com"
                send_email(to, content)
                print("Email has been sent successfully")
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
                speak("sorry! I am unable to send email")

        elif 'take a break' in query:
            if '30 seconds' in query:
                print("Taking Break of 30 seconds...")
                speak("Taking Break of 30 seconds...")
                time.sleep(30)
                print("30 seconds Break Finished...")
                speak("30 seconds Break Finished...")

            elif '1 minute' in query:
                print("Taking Break of 1 minute...")
                speak("Taking Break of 1 minute...")
                time.sleep(60)
                print("1 minute Break Finished...")
                speak("1 minute Break Finished...")

            else:
                print("Taking Break...")
                speak("Taking Break...")
                time.sleep(20)
                print("Break Finished...")
                speak("Break Finished...")

            speak("Ready to help you, sir")

        elif 'open pycharm' in query:
            os.startfile(
                "D:\\PyCharm Community Edition 2020.3.4\\bin\\pycharm64.exe")
            print("Opening Pycharm...")
            speak("Opening Pycharm")

        elif 'write in a file' in query:
            try:
                speak("OK Tell me the file name to be created")
                file_name = take_command().lower()
                with open(f"{file_name}.txt", 'a+') as file:
                    speak("What Should I write in file")
                    msg = take_command()
                    print("Writing in file...")
                    speak("Writing in file...")
                    file.write(f"{msg}\n")
                    print("Successfully written in the file")
                    speak("Successfully Written in the file")
                    file.close()
                print(f"File saved in following directory\n{os.getcwd()}")
                speak("File saved in this directory")

            except Exception as e:
                speak("Sorry!! I am unable to open file")

        elif 'search a song' in query:
            speak("OK! Tell me the song")
            song_name = take_command().lower()
            input_song_name = song_name.replace(" ", "+")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.google.com/search?q={input_song_name}")
            print("Searching your song...")
            speak(f"searching the song{song_name}")

        elif 'search on youtube' in query:
            speak("What should I search in youtube?")
            yt_search = take_command().lower()
            input_yt_search = yt_search.replace(" ", "+")
            print("Searching on YouTube...")
            speak(f"searching {yt_search}")
            webbrowser.get(chrome_path).open_new_tab(
                f"https://www.youtube.com/results?search_query={input_yt_search}")

        elif ('open command prompt' in query) or ('open cmd' in query):
            print("Opening Command Prompt...")
            speak("Opening Command Prompt...")
            os.startfile("C:\\Windows\\System32\\cmd.exe")

        elif 'open powershell' in query:
            print("Opening PowerShell...")
            speak("Opening PowerShell...")
            os.startfile(
                "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")

        elif 'none' in query:
            continue

        elif 'go offline' in query:
            wish_me_ending()
            exit()

        else:
            print("Sorry!! I don't Understand")
            speak("Sorry!! I don't Understand")
            continue

        print("\nNext Order Please...")
        speak("Next Order Please...")
        time.sleep(1)
