init python:
  def hideAll():
    array = renpy.list_images()
    print array

    for x in array:
      if (renpy.has_image(x, exact=False) == True) and (x != 'black'):
        print(x)
        # ImageDissolve(x, 1.0)
        renpy.hide(x,)
    print "It's day %(day)d and %(time)s"
    renpy.say(narrator, "It's day %(day)d, %(dayOfWeek)s and %(time)s")

  def eventSystem():
    # if day == 1:
    #   Day01()
    #   return
    StandardEvent()

    def eventStory():
        if (location == ""):
            if (day == 1):
              Act01()
              return
            if (day == 2):
              Act02()
              return
            if (day == 3):
              Act03()
              return
            if (day == 4):
              Act04()
              return


