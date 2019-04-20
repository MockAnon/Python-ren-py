# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define b = Character("Brynn")

define g = Character("Girl")

image bg library = "gui/locations/library.jpg"
image bg club = "gui/locations/club.jpg"
image bg boathouse = "gui/locations/boathouse.jpg"

image brynn = "images/characters/brynn.jpeg"
image ella = "images/characters/ella.jpeg"
image lissandra = "images/characters/lissandra.jpeg"

define affection = 0






init python:
    # import store.day01 as day01
    Emily = Emily()
    # Janet = Janet()
    time = "noon"
    day = 1
    location = ""
    dayOfWeek = "Sunday"

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

screen gui_game_menu():
     # vbox xalign 1.0 yalign 1.0:
          imagebutton auto  "Icon_01_%s.png" action ShowMenu('lybrary')
          # imagebutton auto "prefs_%s.png" action ShowMenu('preferences')
          # imagebutton auto "skip_%s.png" action Skip()
          # imagebutton auto "afm_%s.png" action Preference("auto-forward mode", "toggle")
# screen library:


screen world_map: #Preparing the imagemap
  imagemap:
    ground "images/Solar_sys.jpg"
    hover "images/Icon_01_select.png"
    # ground "planets.jpg"
    # hover "planets-hover.png"

    # hotspot (62, 399, 0, 91) hovered Show("gui_tooltip", my_picture="images/Icon_01_hover.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")]
    # hotspot (227, 302, 0, 137) clicked Jump("club")
    # hotspot (405, 218, 164, 118) clicked Jump("boathouse")
    # hotspot (591, 78, 123, 111) clicked Jump("cottage")
    hotspot (1106, 498, 66, 61) hovered Show("gui_tooltip", my_picture="images/Icon_02.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")] clicked Jump("club")
    hotspot (474, 156, 98, 92) hovered Show("gui_tooltip", my_picture="images/Icon_01_hover.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")] clicked Jump("boathouse")
    hotspot (1203, 453, 59, 52) hovered Show("gui_tooltip", my_picture="images/Icon_03.png", my_tt_xpos=0, my_tt_ypos=0) unhovered [Hide("gui_tooltip")] clicked Jump("lybrary")

    # hotspot (790, 164, 233, 56) action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_load.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

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
    jump world_map
    # jump gui_game_menu

    label gui_game_menu:
        call screen gui_game_menu

    label world_map:
        call screen world_map #Displaying the imagemap
        $ location = ""

    label lybrary:
        hide screen gui_tooltip
        show bg library
        with dissolve
        $ location = "lybrary"
        "It is %(location)s"


        python:
            eventSystem()
            TimeSystem()
            hideAll()
        "this returned thus is usable"
        jump world_map

    label club:
      hide screen gui_tooltip
      show bg club
      with dissolve
      $ location = "club"
      "It is %(location)s"

      show brynn at right
      "It is club."
      b "Hey Anon, do you want me to show you something?"
      python:
        eventSystem()
        TimeSystem()
        hideAll()
      jump world_map

    label boathouse:
        hide screen gui_tooltip
        show bg boathouse
        "It is boathouse."
        show brynn at right
        b "Awesome"
        b "this is my friend margret"
        show ella at left
        b "woah"
        # hide brynn
        b "bye bye"
        python:
            eventSystem()
            TimeSystem()
            hideAll()
            renpy.jump('world_map')


    label cottage:
        $ location = "cottage"
        "It is %(location)s"
        python:
            eventSystem()
            TimeSystem()
            hideAll()
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

        if day == 123:
            "It's day %(day)d and %(time)s thus its time to go home."
            return

        if affection == 1:
            e "I RUVVV YOUUU"

        jump noon



    label noon:
        g "test"
        $ time = "noon"
        # "It's day %(day)d and %(time)s"
        jump afternoon

    label afternoon:

        $ time = "afternoon"
        # "It's day %(day)d and %(time)s"
        python:
            # Emily.addLove(1)
            char_1.addLove(2)
            char_1.subtractLove(1)
        jump evening
        # python:
        #     Emily.lybrary()

    label evening:

        $ time = "evening"
        # "It's day %(day)d and %(time)s"
        jump night

    label night:
        $ time = "night"
        # "It's day %(day)d and %(time)s"
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
