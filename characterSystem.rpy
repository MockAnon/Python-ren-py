init python:
  class CharacterObj:

    def __init__(self, first, last, love, like):
      self.first = first
      self.last = last
      self.like = like
      self.love = love
      self.a = 0
      self.b = 0
      self.c = 0

    def addLove(self, number):
      # like = 0
      # like = self.like
      self.like = self.like + number
      # like += number
      out = str(self.like)
      print("You have gained " + out)
      e("You have gained " + str(number) + " and are now at " + out)
      # e(out)
      # return like
    def subtractLove(self, number):
      self.like = self.like - number
      out = str(self.like)
      print(out)
      e("You have lost " + str(number) + " and are now at " + out)

    def aUp(self):
      self.a = self.a + 1
      print(self.a)

  class protagonist:
    def __init__(self):
      self.faith = 0
      self.intelligence = 0
      self.strength = 0
      self.popularity = 0

      self.weeb = 0
      self.soy = 0
      self.endurance = 0
      self.girlfriend = []

    def raiseStat(self, type, number):
      vars(self)[type] += number
      output = vars(self)[type]
      print vars(self)[type]
      renpy.say(narrator, "You have gained " + str(number) + " " + type + ". You now have " + str(output) + " " + type)
      return vars(self)[type]



  anon = protagonist()
  char_1 = CharacterObj('Emily', 'Jones', 0, 0)
  char_2 = CharacterObj('Emily', 'Jones', 0, 0)


  print(char_1.first)



# Emily maybe delete
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

    # def lybrary(what, **kwargs):
    #   e("another file-Emily")

    # def rink(what, **kwargs):
    #   e("inception")
