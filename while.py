# i = 1
# while i <=5:
#     print(i)
#     i = i + 1
# print("Done ")


# i = 1
# while i <=5:
#     print('*' * i)
#     i = i + 1
# print("Done ")

# secret_num=9
# guess_count = 0
# while guess_count < 3:
#     guess=int(input("Guess: "))
#     guess_count +=1
#     if guess == secret_num:
#         print('you won!')
#         break
    
# else:
#     print("You didn't guess it correct mate!")



command = ""
started = False
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("The car is already running")
        else:
            started = True
            print("Car started......Let's grind")
    elif command.lower() == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car has stopped....")
    elif command.lower() == "help":
        print("Start: To start the car")
        print("Stop: To stop the car")
        print("quit: To quit the game")
    elif command.lower() == "quit":
        break
    else:
         print("I don't understand")

print("The game has been quited")

