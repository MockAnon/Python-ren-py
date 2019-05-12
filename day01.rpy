init python:
  def StandardEvent():
    if (time == 'noon' or time == 'morning') and (location == 'lybrary'):
      BrynnStandard()
      char_1.aUp()

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
          renpy.say(main, "But, is it funny?")
          renpy.say(b, "Yep, thank you and have a nice day!")
          renpy.say(main, "She, thinks I'm cute.")
          char_1.addLove(1)

          return
      if char_1.a == 2:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        if char_1.like == 0:
          renpy.say(b, "You again...Are you actually going to buy anything this time?")
        else:
          renpy.say(b, "Oh hey, how are you?")
          renpy.say(main, "Great!")
          renpy.say(b, "What would you like?")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':

          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Oh? Sure, that will be $2.50")
          renpy.say(b, "Here you go, that will be $2.50")
          renpy.say(main, "Thanks")
          if char_1.like > 2:
            renpy.say(b, "No funny jokes today?")
            renpy.say(main, "If you were a chicken, you'd be impeccable!")
            renpy.say(b, "Thanks")
          renpy.say(b, "Have a nice day!")
          return
        if shift == '01':
          renpy.say(main, "If you were a chicken, you'd be impeccable!")
          renpy.say(b, "Oh... heh.")
          if char_1.like == 0:
            renpy.say(b, "If you're not going to buy anything then please leave.")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Tell me if this is funny. If you were a chicken, you'd be impeccable!")
          renpy.say(b, "Heh...")
          renpy.say(b, "That's cute.")
          if char_1.like > 2:
            renpy.say(b, "You're pretty funny!")
          char_1.addLove(1)
        return
      if char_1.a == 3:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        if char_1.like == 0:
          renpy.say(b, "If you aren't going to buy anything then please leave.")
        else:
          renpy.say(b, "Oh hey, how are you?")
          renpy.say(main, "Great!")
          renpy.say(b, "What would you like?")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Oh? Sure, that will be $2.50")
          renpy.say(b, "Here you go, that will be $2.50")
          renpy.say(main, "Thanks")
          if char_1.like > 2:
            renpy.say(b, "No funny jokes today?")
            renpy.say(main, "Tell me if this is funny. If you were a chicken, you'd be impeccable!")
            renpy.say(b, "Thanks")
          renpy.say(b, "Have a nice day!")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Tell me if this is funny. If you were a chicken, you'd be impeccable!")
          renpy.say(b, "Heh...")
          renpy.say(b, "That's cute.")
          if char_1.like > 2:
            renpy.say(b, "You're pretty funny!")
        char_1.addLove(2)
        return
      if char_1.a == 4:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        if char_1.like < 2:
          renpy.say(b, "I'm happy that you actually bought something last time.")
        else:
          renpy.say(b, "Oh hey, what would you like?")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':

          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Here you go, that will be $2.50")
          if char_1.like < 2:
            renpy.say(narrator, "Gives her $2.50")
            renpy.say(b, "Thanks, I'm happy to see you had a change of heart.")
          else:
            renpy.say(narrator, "Gives her $2.50")
            renpy.say(b, "Thanks for coming!")
          return
        if shift == '01':
          renpy.say(main, "What do you call a group of unorganized cats? A cat-astrophe!")
          renpy.say(b, "... AH HA HA HA HA HA!!!!! That's so...")
          if char_1.like < 2:
            renpy.say(b, "Please... sir, this is a buisness. If you're not going to buy anything then please leave.")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "What do you call a group of unorganized cats? A cat-astrophe!")
          renpy.say(b, "Heh...")
          renpy.say(b, "...AH HA HA HA HA HA!!!!! Hm... This time you even ask if its funny. You really brighten up my day")
          char_1.addLove(1)
        return

      if char_1.a == 5:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        if char_1.like < 2:
          renpy.say(main, "...")
          renpy.say(b, "...You didn't get mad this time.")
          renpy.say(main, "Please just order something.")
        shift = renpy.display_menu([('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Here you go, that will be $2.50")
          renpy.say(narrator, "Gives her $2.50")
          renpy.say(b, "Thanks for coming!")
          return
        if shift == '01':
          renpy.say(main, "Didn't I see you on the cover of Vogue?")
          renpy.say(b, "...At least your last few comments were actually funny. Now you're clearly just trying to pick me up. Please leave before I get my manager.")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Now I remember where I've seen you before... didn't I see you on the cover of Vogue?")
          renpy.say(b, "Heh... that's sorta sweet. Anyways.. thanks for your buisness.")
          char_1.addLove(1)
        return

      if char_1.a == 6:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        shift = renpy.display_menu([('Ask for her number', '03'), ('Buy icecream and leave.', '02'), ('Make cheesy joke and then buy nothing', '01'), ('Buy icecream and then make cheesy joke', '00')])
        if shift == '00':
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Here you go, that will be $2.50")
          renpy.say(narrator, "Gives her $2.50")
          renpy.say(b, "Thanks for coming!")
          return
        if shift == '01':
          renpy.say(main, "Why don't they play poker in the jungle? Too many cheetahs.")
          renpy.say(b, "This is seriously your last warning, if you do this again I will be getting my manager.")
          return
        if shift == '03':
          renpy.say(main, "I seem to have lost my number, can I have yours?")
          renpy.say(b, "This is my job... please... stop.")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Do you know why they don't play poker in the jungle? Too many cheetahs!")
          renpy.say(b, "AH HA HA HA! You are starting to become my favourite customer.")
          char_1.addLove(1)
          return
      if char_1.a == 7:
        renpy.show("brynn")
        renpy.say(b, "Welcome to Dairy Shack, how may I help you?")
        shift = renpy.display_menu([('Buy icecream and leave.', '00'), ('Make cheesy joke, ask for her number', '01')])
        if shift == '00':
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Here you go, that will be $2.50")
          renpy.say(narrator, "Gives her $2.50")
          renpy.say(b, "Thanks for coming!")
          return
        if shift == '01':
          renpy.say(main, "Why don't they play poker in the jungle? Too many cheetahs.")
          renpy.say(b, "Please stay here for a second.")
          renpy.say(main, "Wait. One more thing...")
          renpy.say(b, "Are you planning to buy something?")
          renpy.say(main, "...I seem to have lost my number. Can I have yours?")
          renpy.say(b, "Yep... as I said, please stay here for a second.")
          renpy.say(b, "This man is harassing me...")
          renpy.say(main, "I'm a paying customer")
          renpy.say(narrator, "This man appears to be a paying customer. Missy just take this mans hard earned money. Sir, what would you like?")
          renpy.say(b, "I hate life...")
          renpy.say(narrator, "What was that?")
          renpy.say(b, "Nothing.")
          renpy.say(main, "Thank you.")
          return
        else:
          renpy.say(main, "May I have some icecream?")
          renpy.say(b, "Sure, that will be $2.50")
          renpy.say(main, "Do you know why they don't play poker in the jungle? Too many cheetahs!")
          renpy.say(b, "AH HA HA HA! You are starting to become my favourite customer.")
          char_1.addLove(1)
          return
      if char_1.a == 8:
        renpy.show("brynn")
        renpy.say(b, "Listen, you clearly have a thing for me. If you just stop coming here only to make weird jokes then I'll just give you my number.")

label day01:
  "this is day 01 label"
