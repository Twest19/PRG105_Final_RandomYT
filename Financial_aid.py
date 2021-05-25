"""
	You are writing a program to determine if a student is eligible for financial aid for the next semester.
	To qualify, the student must either be a new student, or a current student with a GPA of 2.0 or higher.
	Additionally, the student may not have a criminal record for drugs, must enroll in a minimum of six credit hours of
	classes, and must have a gross yearly income of less than $50,000. You will gather information from the student,
	and you will let them know if they are eligible for financial aid or not.
"""

financial_aid_eligibility = True

enrollment = input("Are you currently enrolled as a student (yes/no)? ").lower()

if enrollment == 'yes':
	gpa = float(input("What is your GPA? "))
	if gpa < 2.0:
		financial_aid_eligibility = False
	else:
		credit_hour = int(input("How many credit hours are you currently enrolled in? "))
		if credit_hour < 6:
			financial_aid_eligibility = False
		else:
			criminal = input("Do you have a criminal record for drugs (yes/no)? ").lower()
			if criminal == 'yes':
				financial_aid_eligibility = False
			else:
				income = float(input("What is your gross yearly income? "))
				if income >= 50000:
					financial_aid_eligibility = False
else:
	credit_hour = int(input("How many credit hours are you currently enrolled in? "))
	if credit_hour < 6:
		financial_aid_eligibility = False
	else:
		criminal = input("Do you have a criminal record for drugs (yes/no)? ").lower()
		if criminal == 'yes':
			financial_aid_eligibility = False
		else:
			income = float(input("What is your gross yearly income? "))
			if income >= 50000:
				financial_aid_eligibility = False

if financial_aid_eligibility:
	print("Congratulations! You are eligible for financial aid.")
else:
	print("Sorry, you are not eligible for financial aid.")
