init python:
  def hideA():
    renpy.hide('brynn',)
    renpy.hide('ella',)
    renpy.hide('lissandra',)
    renpy.get_showing_tags(layer='master', sort=False)

    # hide brynn
