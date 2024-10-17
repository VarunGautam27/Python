command=""
started = False

while command != "quit":
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("car has been already started")
        else:
            started = True
            print(" Car has been started")
    elif command.lower() == "help":
        print('''
            start: to start the car
            stop: to stop the car
            quit: to quit the car
              ''')
    elif command.lower() == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("the car has been stopped")
     
    elif command.lower() == "quit":
        break
    else:
        print("i dont understand that")
        
print("the game has been quitted!!!!")

     


