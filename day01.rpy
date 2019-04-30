init python:
  def StandardEvent():
    BrynnStandard()







  def BrynnStandard():
    if (time == 'noon' or time == 'morning') and (location == 'lybrary'):
      renpy.say(narrator, "It's day %(day)d this system sorta works noon")
      if char_1.a == 0:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 00")
        char_1.addLove(2)
        char_1.aUp()
        shift = renpy.display_menu([('bump anger', 'bump'), ('calm anger', 'calm')])
        if shift == 'bump':
          # do bump stuff
          renpy.say(narrator, "option 01")
          question02 = renpy.display_menu([('bump anger', 'bump'), ('calm anger', 'calm')])
          if question02 == 'bump':
            renpy.say(narrator, "option 01b")
          else:
            renpy.say(narrator, "option 02b")
        else:
          renpy.say(narrator, "option 02")
    # do calm stuff
        # renpy.display_menu("Hello", "OH MY", interact=True, screen="choice")
          # "yes":
          #   char_1.addLove(2)
          # "No":
          #   char_1.addLove(2)
        return
      if char_1.a == 1:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 01")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 2:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 02")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 3:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 03")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 4:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 04")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 5:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 05")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 6:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 06")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 7:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 07")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 8:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 08")
        char_1.addLove(2)
        char_1.aUp()
        return
      if char_1.a == 9:
        renpy.show("brynn")
        renpy.say(narrator, "It's day %(day)d this system sorta works noon 09")
        char_1.addLove(2)
        char_1.aUp()
        return
label day01:
  "this is day 01 label"
