init python:
  def week01():
    if day == 0:
      renpy.say(p, "Church e 01")
      if location == "homeroom":
        renpy.say(p, "HomeROOM")
    if day == 1:
      renpy.say(p, "Church e 02")
      if location == "homeroom":
        renpy.say(p, "HomeROOM")
      if location == "period_01":
        renpy.say(p, "period 01")
      if location == "period_02":
        renpy.say(p, "period 02")
      if location == "lunch":
        renpy.say(p, "its lunctime")
      if location == "period_03":
        renpy.say(p, "its period 03")
      if location == "afterschool":
        renpy.say(p, "its afterschool")
      if location == "night":
        renpy.say(p, "Its cold...")
    if day == 2:
      renpy.say(p, "Church e 03")
    if day == 3:
      renpy.say(p, "Church e 04")
    if day == 4:
      renpy.say(p, "Church e 05")
    if day == 5:
      renpy.say(p, "Church e 06")
    if day == 6:
      renpy.say(p, "Church e 07")
    if day == 7:
      renpy.say(p, "Church e 08")
