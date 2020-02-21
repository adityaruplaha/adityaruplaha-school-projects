# EMI Calculation

P = float(input("Enter principal loan amount: "))
R = float(input("Enter annual RoI (%): ")) / 12 / 100
n = float(input("Enter repayment tenure (years): ")) * 12

increase_factor = (1+R)**n
E = (P*R*increase_factor)/(increase_factor-1)

print("EMI is:", round(E, 2))
