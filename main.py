import time #I got time so i can have "load time" so that way players have a buffer to read everything
riddle_one = "To open the first lock solve this riddle (The answer is a whole number):\nI am the number of virtues that guide the soul,\nAnd the sins that take their toll.\nAnd the colors in a drop of morning dew.\nI am the sisters in the winter sky,\nAnd the pillars on which wisdom’s house does lie.\nI am the day the Creator finally chose to rest,\nThe perfect score, the ultimate test."

riddle_two = ""
riddle_three = ""

class Puzzle():
    def __init__(self):
        self.user_name = "Blank"
        self.room_states = {"Room One" :False,
                            "Room Two" : False,
                            "Room Three": False}
        self.start_time = 0
        self.end_time = 0
    def welcome_player(self):
        print("Welcome player before we begin what would you like your username to be? \nPlease enter it below.")
        self.user_name = str(input())
        print("Your username has been set!")
        make_linebreak()
        print("Now make sure to read the instructions carefully!")
        time.sleep(2)
        print("The answer to a lock could be a word or number but it will be specified at the begining of the problem!")
        time.sleep(2)
        print("If the answer is a number make it a whole number not the word (ex. 2 not two)")
        time.sleep(2)
        print("If you get stuck you can acsess a hint!")
        time.sleep(2)
        print("Good luck!")
        print("Let's begin with the first lock!")
        make_linebreak()
        print("Loading...")
        time.sleep(3)
        self.start_time = time.perf_counter()
        self.present_lock_one()
    def present_lock_one(self):
        make_blankspace()
        print(riddle_one)
        while True:
            dont_show = False
            make_linebreak()
            print("     1.|Hint")
            print("     2.|Answer")
            print("     3.|Reset Puzzle")
            make_linebreak()
            x = int(input("     "))
            if x == 1:
                print("This answer is greater than 5 but less than 12")
            elif x == 2:
                make_linebreak()
                print("What is your answer?")
                try:
                    x = int(input("     "))
                except:
                    print("Your answer should be a number (ex. 23) not a word!")
                    dont_show = True
                if x == 7:
                    make_linebreak()
                    print("Congrats you passed the first challenge now onto the next puzzle!")
                    self.room_states["Room One"] = True
                    make_linebreak()
                    print("Loading...")
                    self.end_time = time.perf_counter()
                    print(f"lock one took {self.end_time - self.start_time:.3f} seconds") #This will be used at the end of the escape room so that way they can know final time taken and its ascociated score which will be 0 - 500 
                    time.sleep(10.0)
                    self.present_lock_two()
                    break
                elif x != 7 and dont_show == False:
                    print("YOU ARE WRONG TRY AGAIN!!!")
            elif x == 3:
                print("Reseting...")
                time.sleep(5.0)
                self.present_lock_one()
                break
            else:
                print("Invalid Input")
    def present_lock_two(self):
        pass
    def present_lock_three(self):
        pass
def make_blankspace(): #makes some blank room on the terminal so it looks nice
    for i in range(50):
        print()
def make_linebreak(): #It makes a very fun linebreak
    print("---------------------------------------------")



escape_room = Puzzle()
escape_room.welcome_player()