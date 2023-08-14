import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime

# API key from open AI
openai.api_key = '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'

chatStr = ""

def chat(query):
    global chatStr
    chatStr += f"Haridas: {query}\n Jarvis:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use a different engine if needed
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response.choices[0].text)
    return response.choices[0].text


def ai(prompt):
    content = f"OpenAI response for Prompt: {prompt} \n ********************************************************************** \n\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    content += response.choices[0].text

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt)}.txt", "w") as f:
        f.write(content)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"Haridas said: {query}")
            return query
        except Exception as e:
            return "some error occurred, sorry from Jarvis"


if __name__ == '__main__':
    print("pycharm")
    say("hello, I am Jarvis AI")
    while True:
        print("Listening.....")
        query = takecommand()
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["leetcode", "https://www.leetcode.com"],
            ["github", "https://www.github.com"],
            ["portfolio", "https://haridas-pawar-portfolio.netlify.app/"]
        ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])

        if "play music" in query:
            musicPath = "C:/Users/User/Downloads/Got The Man With The Plan Right Here ! Master Movie Song.mp3"
            os.startfile(musicPath)

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")

        if "write" in query.lower():
            ai(prompt=query)

        if "jarvis" in query.lower():
            chat(query)