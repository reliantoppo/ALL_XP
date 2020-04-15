#!/usr/bin/env python

current_xp = input("Current experience: ")
unmod_xp = input("Enter unmodified experience: ")
mod_xp = input("Enter modifiable (10%) experience: ")*1.1

print("Unmodified experience: " + str(unmod_xp))
print("Modified experience: " + str(mod_xp))
print("Those plus your previous experience brings your new total experince to...:  "+ int(unmod_xp) + int(mod_xp) + int(current_xp))