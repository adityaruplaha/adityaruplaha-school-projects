# Height in cm --> feet and inches
# (just for ya fookin 'muricans)

cm = float(input("Enter height in cm: "))

inches = cm/2.54
ft = int(inches//12)
inches = int(round(inches % 12))

print("Height is about {}'{}\".".format(ft, inches))
