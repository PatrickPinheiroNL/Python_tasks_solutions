#This show a welcome message in the user's screen.
print("Welcome to the tip calculator!")

#This is to keep the bill as a float number, the tip as interger and the numbers of
# people as interger too.
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#This is to calculate percentage and add to the bill to get the total amount.
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent

#This is to take the first total and add the total tip amount to the final total.
total_bill = bill + total_tip_amount

#This takes the total of the bill and splits to the numbers of persons.
bill_per_person = total_bill / people

#This take the bill per person result and transform to a round number to be more specific and
#to know how exactly how much each person should pay.
final_amount = round(bill_per_person, 2)

#This is to show to the user how much each person should pay.
print(f"Each person should pay: ${final_amount}")




#This is just to not close your terminal right after the last print as a default.
input("Press Enter to leave the program.")