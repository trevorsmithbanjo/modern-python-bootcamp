donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for donation in donations.values():
    total_donations += donation

print(total_donations)