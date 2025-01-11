day = input("is it Saturday today? [yes/no]")
if day == "no":
    print ("Ok")
elif day == "yes":
      time = int(input("what time to start the alarm?")) 
      if time > 14:
             print("try again")
      if time<8:
             print("try again")
      elif time<14 and time>8:
         timee = int(input("what time to end the alarm?")) 
         if timee > 14:
             print("try again")
         if timee<8:
             print("try again")
         if timee<14 and timee>8:
             print(f"Alarm is set to {time} - {timee}")

