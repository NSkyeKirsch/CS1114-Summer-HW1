"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q4
Date due: 2022-05-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


john_days = int(input("Please enter the number of days John has worked: "))
john_hours = int(input("Please enter the number of hours John has worked: "))
john_minutes = int(input("Please enter the number of minutes John has worked: "))
bill_days = int(input("Please enter the number of days Bill has worked: "))
bill_hours = int(input("Please enter the number of hours Bill has worked: "))
bill_minutes = int(input("Please enter the number of minutes Bill has worked: "))


total_minutes = (john_minutes + bill_minutes)

num_min_to_hrs = total_minutes // 60

total_minutes = total_minutes % 60

total_hours = john_hours + bill_hours + num_min_to_hrs;

num_hrs_to_days = total_hours // 24;

total_hours = total_hours % 24;

total_days = john_days + bill_days + num_hrs_to_days;


print("The total time both of them worked together is:",total_days, "days,",total_hours,"hours, and",total_minutes,"minutes.");
