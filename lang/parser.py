from sly import Parser
from lang.lexer import RPGLexer

import lang.functions as lf

class RPGParser(Parser):
  tokens = RPGLexer.tokens

  precedence = (
    ("left" , PRINT, SELECT, FROM),
    ("left" , LOAD  , BATTLE),
  )

  def __init__(self):
    self.ids = {}

  @_('PRINT expr')
  def statement(self, p):
    return lf.print_player(p.expr)

  @_('ID ASSIGN expr')
  def statement(self, p):
    self.ids[p.ID] = p.expr

  @_('expr')
  def statement(self, p):
    return p.expr

  @_('LOAD')
  def expr(self, p):
    return lf.load()

  @_('LOAD STRING')
  def expr(self, p):
    return lf.load(p.STRING)

  @_('BATTLE expr expr')
  def expr(self, p):
    return lf.battle(p.expr0, p.expr1)
  
  @_('ID')
  def expr(self, p):
    try:
      return self.ids[p.ID]
    except LookupError:
      print(f'Undefined name {p.ID!r}')

  @_('select')
  def expr(self, p):
    return p.select

  @_('SELECT STRING FROM expr')
  def select(self, p):
    return (lf.select_from(p.STRING, p.expr))
