secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = secs_int // 3600
seconds_left_over = secs_int % 3600
minutes = seconds_left_over // 60
seconds_left_over = secs_int % 60
seconds = seconds_left_over
print(hours,":",minutes,":",seconds) # do not change this line 