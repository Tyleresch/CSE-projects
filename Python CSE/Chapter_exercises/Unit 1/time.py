secs_str = input("Input seconds: \n") # do not change this line
# hours =
# minutes =
# seconds =
hours = int(secs_str) // 3600
minutes = (int(secs_str) % 3600) // 60
seconds = (int(secs_str) % 3600) % 60 
print(hours,":",minutes,":",seconds) # do not change this line