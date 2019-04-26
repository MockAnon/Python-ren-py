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

