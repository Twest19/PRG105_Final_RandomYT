"""
You are writing a program to sell tickets to the school play.
If the person buying the tickets is a student, their price is $5.00 per ticket.
If the person buying the tickets is a veteran, their price is $7.00 per ticket.
If the person buying the ticket is a sponsor of the play, the price is $2.00 per ticket.
"""

# Must initialize price and discount to later assign them a new value
price = 0
discount = 0

print(f"{'=' * 6} Play Ticket Types w/ Prices {'=' * 6}"
						"\n(1) Student - $6.00"
						"\n(2) Veteran - $7.00"
						"\n(3) Show Sponsor - $2.00"
						"\n(4) Retiree - $6.00"
						"\n(5) General Public - $10.00")
print(f"{'=' * 36}")

# Ask the buyer which ticket group they fall into
# Choose a number 1-5 or it will display an error and prompt them until they provide a proper response
while True:
	prompt = input("\nPlease choose a number for the corresponding ticket type that you fall into: ")

	if prompt in ('1', '2', '3', '4', '5'):
		ticket_type = int(prompt)
		# Assign the ticket to a price for the number chosen by the buyer

		if ticket_type == 1:
			price = 6.00
			print("\nYou have selected Student.")

		elif ticket_type == 2:
			price = 7.00
			print("\nYou have selected Veteran.")

		elif ticket_type == 3:
			price = 2.00
			print("\nYou have selected Show Sponsor.")

		elif ticket_type == 4:
			price = 6.00
			print("\nYou have selected Retiree.")

		elif ticket_type == 5:
			price = 10.00
			print("\nYou have selected General Public.")

		break
	else:
		print("\nError please try again")

# Let the buyer know that they can receive a discount when they buy more tickets
print("\nIf you buy 4 - 8 tickets you get a 10% discount.")
print("If you buy 9 - 15 tickets you get a 15% discount.")
print("If you buy more than 15 tickets you get a 20% discount.")

# Ask buyer how many tickets they would like to purchase
ticket_quantity = int(input("\nHow many tickets would you like to buy? "))

# Get the total price before any discounts are applied if there are any
ticket_total = price * ticket_quantity

# Determine if the buyer has met the requirements for a discount
if ticket_quantity > 15:
	print("\nYou get a 20% discount!")
	discount = ticket_total * .20
elif ticket_quantity >= 9:
	print("\nYou get a 15% discount!")
	discount = ticket_total * .15
elif ticket_quantity >= 4:
	print("\nYou get a 10% discount")
	discount = ticket_total * .10
else:
	print("\nSorry, you do not get a discount.")

# Calculate the price by applying the discount
discount_applied = ticket_total - discount

# Calculate average price paid
avg = discount_applied / ticket_quantity

# Display the total before and after discount with how much they saved
print(f"\nTotal before discount: ${ticket_total:.2f}")
print(f"You saved: ${discount:.2f} ")
print(f"Your price per ticket is: ${avg:.2f}")
print(f"Total after discount: ${discount_applied:.2f}")
