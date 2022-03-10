from lang.lang import Lang

def start(args):
  lang    = Lang()
  command = args[1] if len(args) > 1 else None

  if command == None:
    lang.shell()
  elif command == "help":
    print("\ndocumentation: https://github.com/Gustavo-Pettine\n")
  elif command == "license":
    print("\nThis software is under MIT license.\n")
  elif command == "copyright":
    print("\nMade in Brazil by Gustavo Pettine.\n")
  else:
    lang.parseFile(command)