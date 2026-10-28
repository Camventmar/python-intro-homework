day= input("What day is it: ").lower()
time = input("What time of the day is it: ").lower()
if day == "saturday" or day == "sunday":
    print("It's the weekend! Check if you have homework, if not - try to rest.")
elif (day == "monday" or day =="tuesday") and time == "morning" or time == "afternoon":
    print (f"Happy {day}! Look over your schedule and sieze the day!")
elif (day == "wednesday" or day == "thursday") or time == "evening":
    print (f"It is {day} {time}. Have you started your homework?")
elif day == "":
    print(f"It's the {time}, do one thing that makes you happy before the day ends!")
else:
    print("Sorry, I don't recognize your input. Can you try again?")
