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
    renpy.say(narrator, "It's day %(day)d, %(dayOfWeek)s and %(time)s")
    if day <= 7:
      week01()
      return
    if day <= 14:
      week02()
      return
    if day <= 21:
      week03()
      return
    if day <= 27:
      week04()
      return
    if day == 28:
      renpy.say(narrator, "I left the school. sitting there starring up at the sky... holding what was left. These memories, were they ever mine.")
      renpy.jump("start");
      return


