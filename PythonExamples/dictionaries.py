#!/usr/bin/python

fruit = {1:"apple", 2:"orange", 3:"banana"}
rgb = {"red": [255, 0, 0], "teal": [0, 128, 128], "cyan": [0,255,255], "blue": [0,0,255]}
temps = {"Monday": 30, "Tuesday": 41, "Wednesday": 61, "Thursday": 49, "Friday": 41}

"""
#replacing
print(fruit)
fruit[0] = "pear"
fruit[1] = "pineapple"
print(fruit)
print("----------")
print(temps)
temps["Friday"] = 70
print(temps)
"""

#accessing
myFruit = fruit[2]
print(myFruit)
#myTemp = temps["Saturday"]

# g3
colors = rgb.keys()
print(colors)
rgbVals = rgb.values()
print(rgbVals)
bgr = rgb.items()
print(bgr)

#g4
