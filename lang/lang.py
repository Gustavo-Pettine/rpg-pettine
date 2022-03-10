from lang.lexer  import RPGLexer
from lang.parser import RPGParser

class Lang:
  def __init__(self):
    self.lexer   = RPGLexer()
    self.parser  = RPGParser()
    self.version = "0.0.1"

  def parse(self, text):
    self.parser.parse(self.lexer.tokenize(text))

  def shell(self):
    print(f'RPGPettine {self.version}\nType "help", "copyright" or "license" for more information')
    while True:
      try:
        text = input(">> ")
      except EOFError:
        break
      if text:
        self.parse(text)

  def parseFile(self, file_path):
    with open(file_path) as file:
      for line in file:
        self.parse(line)