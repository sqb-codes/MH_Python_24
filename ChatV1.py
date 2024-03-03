chat = True

while chat:
    message = input("Enter your message : ")
    # print("Welcome :",message)

    message = message.lower()

    # 4 spaces are standard
    if message == "hi" or message == "hello" or message == "hey":
        print("Hello User")
    elif message == "bye":
        print("Bye User...")
        break
    else:
        print("I don't understand")