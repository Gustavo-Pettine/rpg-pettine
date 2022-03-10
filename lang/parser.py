from sly import Parser
from lang.lexer import RPGLexer

import lang.functions as lf

class RPGParser(Parser):
  tokens = RPGLexer.tokens

  precedence = (
    ("left" , PRINT),
    ("left" , LOAD  , BATTLE),
  )

  def __init__(self):
    self.ids = {}

  @_("PRINT expr")
  def expr(self, p):
    lf.print_player(p.expr)
    return p.expr

  @_('ID')
  def expr(self, p):
    try:
      return self.ids[p.ID]
    except LookupError:
      print(f'Undefined name {p.ID!r}')

  @_('ID ASSIGN expr')
  def expr(self, p):
    self.ids[p.ID] = p.expr

  @_('LOAD')
  def expr(self, p):
    return lf.load()

  @_('LOAD STRING')
  def expr(self, p):
    return lf.load(p.STRING)

  @_('BATTLE expr expr')
  def expr(self, p):
    return lf.battle(p.expr0, p.expr1)