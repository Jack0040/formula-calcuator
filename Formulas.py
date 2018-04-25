"""
		outline for each formula:
		
elif formula == "FORMULA NAME GOES HERE":
  X = int(input("X? "))
  Y = int(input("Y? "))
  Z = int(input("Z? "))
  print (str(X),"*",str(Y),"*",str(Z)," =", "				", X * Y * Z)
  input("Press enter to exit ;)")
"""

"""				List of functions already implemented and thier names:
-test: X*Y*Z
-Celsius to Kelvin (CtoK or ctok)
-boiling point change 

"""

#			Add constants below 

RkPa = 8.314			#R in kPa
Ratm = 0.0821			#R in atm
WaterKf = 1.86
WaterKb = 0.51

#end of constants

import math
formula = input("What formula would you like to use (or type help for a list)? ")	#Input what formuala to use

#		Test X*Y*Z
if formula == "test":
  X = int(input("X? "))
  Y = int(input("Y? "))
  Z = int(input("Z? "))

  print (str(X),"*",str(Y),"*",str(Z)," =","				", X * Y * Z)
  input("Press enter to exit ;)")
 
#end of test

#		Celsius to Kelvin
elif formula == "CtoK" or formula == "ctok":
  C = int(input("Degrees C? "))
  
  print (str(C),"+ 273 =", "				", C + 273,"K")
  input("Press enter to exit ;)")
#end of kelvin
  
#boiling point change
elif formula == 'boiling point change':
  m = int(input("Molality? "))
  iiii = int(input("Particles per molecule dissolved? "))
  water = input("Is the solvent water? Y/N ")
  
  if water == "y" or water == "Y":
    kb = WaterKb
  else: kb = int(input('Kb of solvent? '))
  print (iiii * m * kb) 
  input("Press enter to exit ;)")
#end boiling point change

#you have now reached the end of what has been written! consider adding your own formulae...
elif formula == "help":
  print ("test, CtoK (celsius to Kelvin), boiling point change")
  input("Press enter to exit ;)")

else:
  print ("This is not a recognized formula... Type help for a list of functions.")
  input("Press enter to exit ;)")
"""
This is (obviously) the end of this program.  Written by Jack Martin @Jack0040
    /@
    \ \
  ___> \
 (__O)  \
(____@)  \
(____@)   \
 (__o)_    \
       \    \
"""
