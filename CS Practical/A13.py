# Seconds --> Mins:Seconds

secs = float(input("Enter seconds: "))

mins = int(secs // 60)
secs %= 60

print("{}:{}".format(mins, secs))
