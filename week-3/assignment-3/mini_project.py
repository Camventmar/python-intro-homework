day= input("What day is it: ").lower()
time = input("What time of the day is it: ").lower()
if day == "saturday":
    print("It's the weekend! Check if you have homework, if not - try to rest.")
elif day == "sunday":
    print("Happy Sunday! Make sure you do one thing to relax before the start of the week.")
elif (day == "monday" or day =="tuesday") and time == "morning" or time == "afternoon":
    print (f"Happy {day}! Look over your schedule and sieze the day!")
elif (day == "wednesday") and time == "evening":
    print (f"It is {day} {time}. Have you started your homework?")
elif (day == "wednesday") and time == "morning":
    print (f"It is {day} {time}. Good morning!")
elif (day == "wednesday") and time == "evening":
    print (f"It is {day} {time}. Good night, get some rest!")
elif (day == "Thursday") and time == "evening":
    print (f"It is {day} {time}. Good night, it's almost Friday!")
elif (day == "Thursday") and time == "afternoon":
    print (f"It is {day} {time}. There's still time to get things done!")
elif (day == "Thursday") and time == "morning":
    print (f"It is {day} {time}. Good morning, don't forget to eat some breakfast.")
elif day == "":
    print(f"It's the {time}, do one thing that makes you happy before the day ends!")
else:
    print("Sorry, I don't recognize your input. Can you try again?")
