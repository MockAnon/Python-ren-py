init python:
  def StandardEvent():
    BrynnStandard()







  def BrynnStandard():
    if (time == 'noon' or time == 'morning') and (location == 'lybrary'):
      renpy.say(narrator, "It's day %(day)d this system sorta works noon")
      if char_1.a == 0:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':
          # do bump stuff
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(b, "Thank you and have a nice day!")
          return
        if shift == '01':
          renpy.say(main, "How much does a polar bear weigh?")
          renpy.say(b, "I believe that a fully grown male polar bear weights approximately 450kg...?")
          renpy.say(main, "Enough to break the ice... wait what?")
          renpy.say(b, "We live in Canada buddy... So are you actually going to buy anything? ")
          renpy.say(main, "No.")
          renpy.say(b, "Why are you even here?")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Here. By the way, do you know how much a polar bear weighs?")
          renpy.say(b, "...maybe")
          renpy.say(main, "Enough to break the ice.")
          renpy.say(b, "That's cute.")
          renpy.say(main, "I try.")
          renpy.say(b, "Anyways, thank you and have a nice day!")
          char_1.addLove(1)
          char_1.aUp()
          return
      if char_1.a == 1:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        renpy.say(b, "Oh, its you again...")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Oh? Sure, that will be $2.50")
          renpy.say(b, "Have a nice day!")
          return
        if shift == '01':
          renpy.say(main, "So, two peanuts walk into a bar. One was a salted.")
          renpy.say(b, "Heh...")
          renpy.say(b, "I mean... please stop, I'm working")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Tell me if this is funny. Two peanuts walk into a bar. One was a salted.")
          renpy.say(b, "Heh...")
          renpy.say(b, "That's cute.")
          renpy.say(main, "But, is it funny.")
          renpy.say(b, "Yep, thank you and have a nice day!")
          char_1.addLove(1)
          char_1.aUp()
          return
      if char_1.a == 2:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        if char_1.like == 0:
          renpy.say(b, "You again...")
        else:
          renpy.say(b, "Oh hey, how are you?")
          renpy.say(main, "Great!")
          renpy.say(b, "What would you like?")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Oh? Sure, that will be $2.50")
          renpy.say(b, "Have a nice day!")
          return
        if shift == '01':
          renpy.say(main, "So, two peanuts walk into a bar. One was a salted.")
          renpy.say(b, "Oh...")
          if char_1.like == 0:
            renpy.say(b, "If you're not going to buy anything then please leave.")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Tell me if this is funny. Two peanuts walk into a bar. One was a salted.")
          renpy.say(b, "Heh...")
          renpy.say(b, "That's cute.")
          renpy.say(main, "But, is it funny.")
          renpy.say(b, "Yep, thank you and have a nice day!")
          char_1.addLove(1)
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
