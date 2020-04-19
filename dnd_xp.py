#!/usr/bin/env python

current_xp = input("Current experience: ")
current_xp = int(current_xp)
unmod_xp = input("Enter unmodified experience: ")
unmod_xp = int(unmod_xp)
mod_xp = input("Enter modifiable (10%) experience: ")
mod_xp = int(mod_xp) * (1.1)
sum = (unmod_xp) + (mod_xp) + (current_xp)

print("Your new total experience is: {}".format(sum))