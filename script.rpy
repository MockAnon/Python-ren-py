﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define g = Character("Girl")

define affection = 0






init python:
    # import store.day01 as day01
    Emily = Emily()
    # Janet = Janet()
    time = "noon"
    day = 0

    def PrintMessage(what, **kwargs):
         g("bobbiw")
         e("steve")
    # def lybrary(what, **kwargs):
    #     if day == 2:
    #       e("this file")

    def TimeSystem():
        global time
        global day
        if time == "noon":
            time = "afternoon"
            day += 1
            g("It's day " + str(day) + " and " + time)
            return time
        if time == "afternoon":
            time = "evening"
            day += 1
            g("It's day " + str(day) + " and " + time)
            return time
        if time == "evening":
            time = "night"
            day += 1
            g("It's day " + str(day) + " and " + time)
            return time
        if time == "night":
            time = "noon"
            day += 1
            g("It's day " + str(day) + " and " + time)
            return time

    class Character():
        bob = 30
        interest = 50
        friendship = 0
        # def properties(self):
        #     self.interest = 50
        #     self.friendship = 0

        # $ printMessage(self):
        #     "I love cheetos anon"

screen gui_game_menu():
     vbox xalign 1.0 yalign 1.0:
          imagebutton auto idle hover "Icon_01_%s.png" action Jump('lybrary')
          # imagebutton auto "prefs_%s.png" action ShowMenu('preferences')
          # imagebutton auto "skip_%s.png" action Skip()
          # imagebutton auto "afm_%s.png" action Preference("auto-forward mode", "toggle")


screen world_map: #Preparing the imagemap
  imagemap:
    ground "Solar_sys.jpg"
    hover "Icon_01_select.png"
    # ground "planets.jpg"
    # hover "planets-hover.png"

    hotspot (62, 399, 90, 91) clicked Jump("lybrary")
    hotspot (227, 302, 141, 137) clicked Jump("club")
    hotspot (405, 218, 164, 118) clicked Jump("boathouse")
    hotspot (591, 78, 123, 111) clicked Jump("cottage")

# The game starts here.
label start:
    # $ lybrary = day01.lybrary()
    $ obj = Character()
    # $ day = 0
    # $ time = ""

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "This is an imagemap tutorial."
    # jump world_map
    jump gui_game_menu

    label world_map:
        call screen world_map #Displaying the imagemap

    label lybrary:
        "It is lybrary."
        python:
            TimeSystem()
        jump world_map

    label club:
        "It is club."
        python:
            TimeSystem()
        jump world_map

    label boathouse:
        "It is boathouse."
        python:
            TimeSystem()
        jump world_map

    label cottage:
        "It is cottage."
        python:
            TimeSystem()
        jump world_map

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    label morning:
        # $ day += 1
        # $ time = "morning"
        "It's day %(day)d and %(time)s"

        if day == 2:
            PrintMessage ""
            $ affection += 1
            python:
                Emily.lybrary()
                # Janet.lybrary()



        #     "printing this"

        if day == 20:
            "It's day %(day)d and %(time)s thus its time to go home."
            return

        if affection == 1:
            e "I RUVVV YOUUU"

        jump noon



    label noon:
        g "test"
        $ time = "noon"
        "It's day %(day)d and %(time)s"
        jump afternoon

    label afternoon:

        $ time = "afternoon"
        "It's day %(day)d and %(time)s"
        python:
            # Emily.addLove(1)
            char_1.addLove(2)
            char_1.subtractLove(1)
        jump evening
        # python:
        #     Emily.lybrary()

    label evening:

        $ time = "evening"
        "It's day %(day)d and %(time)s"
        jump night

    label night:
        $ time = "night"
        "It's day %(day)d and %(time)s"
        python:
            if char_1.like >= 10:
                e("I LOVE YOU ANON")
        jump morning




    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    g "I don't like you casual"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "Hey Bob you look nice today!":
            jump boblooksnice
        "Hey Bob you're dumb":
            jump bobisdumb

    label boblooksnice:
        g "Why thank you girl"
        return
    label bobisdumb:
        g "Go AWAY!!!"
        "Bob walks away"
        return
    return
