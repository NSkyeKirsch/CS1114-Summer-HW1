"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q3
Date due: 2022-05-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
# unlike last problem, convert from lbs/in to metric


weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))

weight *= 0.453592
height *= 0.0254

BMI = weight/(height ** 2)

print("Your BMI is:", BMI)