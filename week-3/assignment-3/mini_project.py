day= input("What day is it: ").lower()
time = input("What time of the day is it: ").lower()
if day == "saturday":
    print("It's the weekend! Check if you have homework, if not - try to rest.")
elif day == "sunday" and (time == "morning" or time == "afternoon" or time == "evening"):
    print("The weekend is almost over. Take a break if needed and make sure to finish your homework!")
elif (day == "monday" or day =="tuesday"):
    print (f"Happy {day}! Look over your schedule and sieze the day!")
elif day == "" and time == "morning" or time == "afternoon":
    print("There's still time left in the day. Take advantage of it!")
elif (day == "wednesday" or day == "thursday") or time == "evening":
    print (f"It is {day} {time}. Have you started your homework?")
elif day == "friday" and time == "morning" or time == "afternoon":
    print ("It's almost the weekend, finish off strong!")
elif day == "Friday" and time == "evening":
    print ("The weekend is here! Make sure to take a break.")
elif day == "":
    print(f"It's the {time}, do one thing that makes you happy before the day ends!")
else:
    print("Sorry, I don't recognize your input. Can you try again?")
