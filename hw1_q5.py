"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q5
Date due: 2022-05-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter your amount in the format of dollars and cents on two separate lines.")

dollars_in = int(input())
cents_in = int(input())

# convert dollars and cents to just cents
total_cents = (dollars_in * 100) + cents_in

# start subtracting as much as possible from biggest cent to smallest cent
quarters = total_cents // 25  # get num of quarters
total_cents -= (quarters * 25)  # subtract by value of the quarters

dimes = total_cents // 10
total_cents -= (dimes * 10)

nickels = total_cents // 5
total_cents -= (nickels * 5)

pennies = total_cents

print(dollars_in,"dollars and",cents_in,"cents are:",quarters,"quarters",dimes,"dimes",nickels,"nickels and",pennies,"pennies");
