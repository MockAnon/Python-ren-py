init python:
  def TimeSystem():
    global time
    global day
    if time == "morning":
      time = "noon"
      # g("It's day " + str(day) + " and " + time)
      return time
    if time == "noon":
      time = "afternoon"
      # g("It's day " + str(day) + " and " + time)
      return time
    if time == "afternoon":
      time = "evening"
      # g("It's day " + str(day) + " and " + time)
      return time
    if time == "evening":
      time = "night"
      # g("It's day " + str(day) + " and " + time)
      return time
    if time == "night":
      time = "morning"
      DayOfWeek()
      day += 1
      # g("It's day " + str(day) + " and " + time)
      return time

  def DayOfWeek():
    global dayOfWeek
    if dayOfWeek == "Sunday":
      dayOfWeek = "Monday"
      return dayOfWeek

    if dayOfWeek == "Monday":
      dayOfWeek = "Tuesday"
      return dayOfWeek

    if dayOfWeek == "Tuesday":
      dayOfWeek = "Wednesday"
      return dayOfWeek

    if dayOfWeek == "Wednesday":
      dayOfWeek = "Thursday"
      return dayOfWeek

    if dayOfWeek == "Thursday":
      dayOfWeek = "Friday"
      return dayOfWeek

    if dayOfWeek == "Friday":
      dayOfWeek = "Saturday"
      return dayOfWeek

    if dayOfWeek == "Saturday":
      dayOfWeek = "Sunday"
      return dayOfWeek
