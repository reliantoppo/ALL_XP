#!/usr/bin/python

current_xp = input("Current experience: ")
current_xp = int(current_xp)
unmod_xp = input("Enter unmodified experience: ")
unmod_xp = int(unmod_xp)
modifier = input("What if any, is your modifier percentage? (0, 5, 10, 15, 20): ")
mod_xp = input("Enter modifiable experience: ")
mod_xp = int(mod_xp) * int(modifier)
sum = (unmod_xp) + (mod_xp) + (current_xp)

print("Your new total experience is: {}".format(sum))
