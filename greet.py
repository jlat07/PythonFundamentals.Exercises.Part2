def greet(name):
  print("Hello " + name)

"""Takes string and adds it after Hello"""

def name_input():
  user_name = input("Whats your name?:")
  greet(user_name)
"""Ask user to input name and saves input as user_name then calls greet() function using that username"""
name_input()