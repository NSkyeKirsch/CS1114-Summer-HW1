"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q3
Date due: 2022-05-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# inputs: weight + height
# outputs: BMI

weight = float(input("Please enter weight in kg: "))
height = float(input("Please enter height in meters: "))

BMI = weight/(height ** 2)

print("Your BMI is:", BMI)