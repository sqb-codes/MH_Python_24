from datetime import datetime as dt

# Intents
greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["date", "tell me date", "what's the date", "today's date"]
timeIntent = ["time", "tell me time", "what's the time", "current time"]

chat = True

while chat:
    message = input("Enter your message : ")
    message = message.lower()

    if message in greetIntent:
        print("Hello User")
    elif message in dateIntent:
        date = dt.now().date()
        current_date = date.strftime("%a %d %B, %Y")
        print("Today's Date :",current_date)
    elif message in timeIntent:
        time = dt.now().time()
        current_time = time.strftime("%H:%M:%S, %p")
        print("Current Time is :",current_time)
    elif message == "bye":
        print("Bye User...")
        break
    else:
        print("I don't understand")
