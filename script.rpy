﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define g = Character("Girl")

define affection = 0






init python:
    # import store.day01 as day01
    Emily = Emily()
    Janet = Janet()

    def PrintMessage(what, **kwargs):
         g("bobbiw")
         e("steve")
    # def lybrary(what, **kwargs):
    #     if day == 2:
    #       e("this file")


    class Character():
        bob = 30
        interest = 50
        friendship = 0
        # def properties(self):
        #     self.interest = 50
        #     self.friendship = 0

        # $ printMessage(self):
        #     "I love cheetos anon"









# The game starts here.



label start:
    # $ lybrary = day01.lybrary()
    $ obj = Character()
    $ day = 0
    $ time = ""

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    label morning:
        $ day += 1
        $ time = "morning"
        "It's day %(day)d and %(time)s"

        if day == 2:
            PrintMessage ""
            $ affection += 1
            python:
                Emily.lybrary()
                Janet.lybrary()



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
