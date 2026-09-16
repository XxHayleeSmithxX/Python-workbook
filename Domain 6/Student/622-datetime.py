import datetime
current_time = datetime.datetime.now()
print("The current date and time is:", current_time.strftime('%m-%d-%Y %H:%M %p'))
print('The day of the week is:', current_time.weekday())
print('The day of the week is:', current_time.strftime('%A'))