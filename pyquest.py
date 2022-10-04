# PyQuest:
# This is a text-adventure game with code "spell-casting" effects that
# I made for MLH GHW Sept 2022.
#
# Features:
# - explore the world and help the MLH mascots in their troubles
# - save the world from the tyranical clutches of dr lambda
# - gain the power to rewrite the world with the Pythonic staff of power

# plan:
# add an eval statement if the player has the staff (so they can call different functions/spells), and even edit the code of the game as it's running maybe
# add an inventory list
# add items
# add a world and map
# add commands (look, spell, talk, etc)
# add characters and dialogue

# MOST IMPORTANTLY keep things simple and short, this is a 3 hour project with 10 minute break

# post:
# after the initial hack period the following was accomplished:
# 
# Features:
# - explore the world
# - look at things
# - use the pythonic staff (spell command) to inspect the program itself and modify it (may crash the program)
# 
# plan (accomplished):
# add commands dict
# add locations dict
# add people dict
# add items dict
# add description dict
# add functions to carry out commands
# game loop with semi-sanitized input


commands = {
  "end": ["quit", "exit", "fin", "end"],
  "spell": ["spell", "cast", "magic", "staff"],
  "whereami": ["whereami", "where", "place", "location"],
  "look": ["look", "examine", "investigate"],
  "go": ["move", "go", "goto"],
  "help": ["help", "helpme", "what", "?"],
}

locations = {
  # current location : adjacent location(s)
  "home": ["mountain", "hacktopia"],
  "mountain": ["home", "lab"],
  "lab": ["mountain"],
  "hacktopia": ["home"],
}

people = {
  # location : people
  "home": ["python"],
  "mountain": ["bird girl"],
  "lab": ["lambda"],
  "hacktopia": ["blahaj", "octocat"],
}

items = {
  # location : items
  "home": [],
  "mountain": [],
  "lab": ["lambda tesseract", "monad"],
  "hacktopia": ["time machine", "linux"],
}

description = {
  # locations
  "home": """Home is where the heart is. All your hacks are safely here, cozy by the fire. Your pet Python is also here.""",
  "mountain": """This is the mountain. They say if you listen carefully you can hear the tones of the universe itself. Or that might be your python program reporting an error..""",
  "lab": """This is the lambda lab. Here elegant solutions and math heavy expressions are discovered for programming. Legend has it that Smalltalk and Python were invented here. Some have called this place the 'MIT away from MIT'. A wellspring of knowledge. We stand on the shoulders of giants.""",
  "hacktopia": """This is the land of hackers. Cool programs, beginner projects, and other fun learning/experiments happen here.""",
  # people
  "python": """Your pet python. It's a really good interpreter, a great friend, and has been a great buddy on your adventures.""",
  "blahaj": """A cute swedish shark. It's just vibing, hacking away at a computer for MLH""",
  "octocat": """A cat with 8 arms. It's really good at keeping records of what's changed. Friend of hackers everywhere.""",
  "bird girl": """They look to be a girl in a red dress with the head of a bird skull. No one knows why they're up here, but they keep saying something about a fantastic planet and vibing on their maschine...""",
  "lambda": """An eccentric category theorist. Their solutions are elegant and legendary, but it's really hard to know what they're talking about sometimes... A true mad scientist at heart.""",
  # items
  "time machine": """An invention by octocat and lambda. The official name is 'git'. It can undo any changes you've made (or redo them) selectively. It's part of what makes hacktopia hacktopia.""",
  "linux": """Its a cute penguin that is running around and helping everyone have a good time.""",
  "lambda tesseract": """A 4-Dimensional lambda cube. Only category theorists like dr lambda dare to comprehend the mathematical implications of such an object. Beware! If you look at it for too long you might start speaking in SKI calculus!""",
  "monad": """'A monoid in the category of endofunctors' - whatever that means.""",
}


def where(location):
  print("You look around you")
  print(description[location])
  print(f"You see these locations nearby: {locations[location]}")


def look(target, location):
  if target == [] or target == "":
    print("You see...")
    print(f"Items: {items[location]}")
    print(f"People: {people[location]}")
  else:
    print(f"You look at {target}")
    print(description[target])


def go(target, location):
  if target in locations[location]:
    return True
  else:
    print(f"{location} doesn't seem to be anywhere nearby..")
    return False

def help():
  print("Recognized command:keyword are")
  for command in commands:
    print(f"\t* {command} : {commands[command]}")




def game(debug=False):
  location = "home"

  print("""
  Hey, welcome to my text-adventure game! Thanks for playing!
  For help, type 'help'.
  To quit, type 'quit'.
  """)
  
  game_running = True
  while game_running:
    # collect tokens for command
    tokens = [token for token in input().split(maxsplit=1)]
    command = tokens[0]
    target = "".join(tokens[1:])
    if debug: print(tokens, command, target)
  
    # decide what to do based on command word (cmd)
    if len(tokens) >= 1:
      if command in commands["end"]:
        break
      elif command in commands["spell"]:
        print(f"You cast the spell by uttering a pythonic string... '{tokens[1]}'")
        eval(tokens[1])
      elif command in commands["whereami"]:
        where(location)
      elif command in commands["look"]:
        look(target, location)
      elif command in commands["go"]:
        if go(target, location):
          location = target
          print(f"You arrive at {location}")
      elif command in commands["help"]:
        help()
      else:
        print(f"'{command}' is not a recognized command.")
        help()


if __name__ == '__main__':
  game(True)
