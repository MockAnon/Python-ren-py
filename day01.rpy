init python:
  def Day01():
    if (time == 'noon') and (day <= 30) and (location == 'lybrary'):
      renpy.say(narrator, "It's day %(day)d this system sorta works noon")
      renpy.call('day01')

label day01:
  "this is day 01 label"
