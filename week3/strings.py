#!usr/bin/env python3

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = "10.4516295"

#Example Question
print(f"Your {varGreen:<0s} Output")
#Question 1
print(f"Hello {varName:<0s}")
#Question 2
print(f"{varRed}-{varGreen}-{varBlue}")
#Question 3
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
#Question 4
print(f"My name is {varName.upper()}")
#Question 5
print(f"[{varRed:+^7s}]")
#Question 6
print(f"[{varGreen.lower():=<7s}]")
#Question 7
print(f"[{varBlue.lower():*>9s}]")
#Question 8
print(f"{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}{varBlue}")
#Question 9
print(f"{varLoot}")
#Question 10
print(f"{varLoot:*<.4s}")
#Question 11
print(f"I have ${varLoot:*<.5s}")
#Question 12
print(f"[$$${varRed:$<7s}][$${varGreen:$<8s}][{varBlue:$^10s}]")
#Question 13
print(f"[{varRed[::-1]: ^7s}][{varGreen: ^9s}][{varBlue[::-1]: ^8s}]")
#Question 14
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
