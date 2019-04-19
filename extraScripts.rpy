init python:
  def hideA():
    # renpy.hide('brynn',)
    # renpy.hide('ella',)
    # renpy.hide('lissandra',)
    # print "output data"
    # print renpy.get_showing_tags(layer='master', sort=False)
    array = renpy.list_images()
    print array
    for x in array:
      print(x)
      renpy.hide(x,)
    # hide brynn
