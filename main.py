class Puzzle():
    def __init__(self):
        self.user_name = "Blank"
    def welcome_player(self):
        print("Welcome user before we begin what would you like your name to be? Please enter it below.")
        self.user_name = str(input())
        print("The answer to a lock could be a word or number but it will be specified at the begining of the problem!")
        print("Let's begin with the first lock!")
        print("------------------------------")
        self.present_lock_one()
    def present_lock_one(self):
        print("To open the lock solve the riddle:\nI am the number of virtues that guide the soul,\nAnd the sins that take their toll.\nI am the wonders the ancient world once knew,\nAnd the colors in a drop of morning dew.\nI am the sisters in the winter sky,\nAnd the pillars on which wisdom’s house does lie.\nI am the day the Creator finally chose to rest,\nThe perfect score, the ultimate test.")
        while True:
            print("------------------------------")
            x = int(input("What is your answer?  "))
            if x == 7:
                print("Congrats you passed the first challenge now onto the next puzzle!")
                self.present_lock_twolockTwo()
                break
            else:
                print("YOU ARE WRONG TRY AGAIN!!!")
    def present_lock_two(self):
        pass



escapeRoom = Puzzle()
escapeRoom.welcome_player()