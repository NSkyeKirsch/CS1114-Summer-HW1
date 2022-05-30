"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q2
Date due: 2022-05-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
current_population = 332717100
seconds_in_year = 31536000

years = int(input("Enter a 4 digit year in the future: ")) - 2022

# to get the number of births, get the amount of seconds in the years between now and then divide
births = (years * seconds_in_year) // 9
# for deaths, divide by
deaths = (years * seconds_in_year) // 12
# for immigrants, divide by
immigrants = (years * seconds_in_year) // 130

# to get the new population, add the change to the original
future_population = (births + immigrants - deaths) + current_population

print("The US population in 2029 is estimated to be:", future_population)