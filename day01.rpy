init python:
  class CharacterObj:

    def __init__(self, first, last, love, like):
      self.first = first
      self.last = last
      self.like = like
      self.love = love

    def addLove(self, number):
      # like = 0
      # like = self.like
      self.like = self.like + 1
      # like += number
      out = str(self.like)
      print(out)
      # e(out)
      # return like


  char_1 = CharacterObj('Emily', 'Jones', 0, 0)
  char_2 = CharacterObj('Emily', 'Jones', 0, 0)
  char_1.addLove(1)
  char_1.addLove(1)
  char_1.addLove(3)


  print(char_1.first)

  class Emily:
    love = 0
    like = 0

    def addLove(self, number):
      # like = 0
      like = self.like
      like = like + 1
      # like += number
      out = str(like)
      e(out)
      return like

    def lybrary(what, **kwargs):
      e("another file-Emily")

    def rink(what, **kwargs):
      e("inception")

  class Janet:
    def lybrary(what, **kwargs):
      e("another file -Janet")

    def rink(what, **kwargs):
      e("inception")