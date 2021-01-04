
class Map:
    def __init__(self):
        pass

class Player:
    def __init__(self,name):
        self.name = name

def print_help(p,m):
    print(Commands.keys())

def quit_game(p,m):
    exit(0)

def pickup(p,m):
    pass

def forward(p,m):
    pass

def right(p,m):
    pass

def left(p,m):
    pass

def backwards(p,m):
    pass

def fight(p,m):
    pass

def save(p,m):
    pass

def load(p,m):
    pass

def rest(p,m):
    pass

Commands = {
    'help' : print_help,
    'quit' : quit_game,
    'pickup' : pickup,
    'forward' : forward,
    'right' : right,
    'left' : left,
    'backwards' : backwards,
    'fight' : fight,
    'save' : save,
    'load' : load,
    'rest' : rest
}

if  __name__ =='__main__':
    print("*"*20 + "Textadventure" + "*"*20)
    name = input("Enter your name: ")

    p = Player(name)
    mmap = Map()
    print("(type help to list all available commands)\n")

    while True:
        command = input(">").lower().split(" ")
        if command[0] in Commands:
            Commands[command[0]](p, mmap)
        else:
            print("You run around in circles and don't know what to do...")