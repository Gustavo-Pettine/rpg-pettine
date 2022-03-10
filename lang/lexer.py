from sly import Lexer

class RPGLexer(Lexer):
  ignore = r" \t"
  ignore_comment = r"//.*\n"
  ignore_newline = r"\n+"

  tokens = { ID, ASSIGN, STRING, PRINT, LOAD, BATTLE }

  PRINT   = r"PRINT"
  LOAD    = r"LOAD"
  BATTLE  = r"BATTLE"
  ASSIGN  = r'='
  ID      = r"[a-zA-Z_]\w*"

  @_(r'".*"')
  def STRING(self, t):
    return t

  def ignore_newline(self, t):
    self.lineno += t.value.count("\n")

  def error(self, t):
    print(f"Error: Wrong character '{t.value[0]}' at line: {self.lineno}, column: {self.index + 1}")
    self.index += 1