#!/usr/bin/python

astring = "I knew who I was this morning, "
bstring = "but I've changed a few times since then..."
cstring = "curiouser and curiouser"
greeting = "HELLO! "

phrase = astring + bstring
swapped = bstring + astring
repeat = greeting * 3

# adding / multiplying strings
#print(phrase)
#print(swapped)
#print(repeat)

# string functions
#print(astring.index("w"))
#print(cstring.count("curious"))

#print(cstring.upper())
#print(greeting.lower())
#print(greeting)

#print(bstring)
#print("b starts with b  "+str(bstring.startswith("b")))
#print("b starts with q  "+str(bstring.startswith("q")))

#print(bstring)
#print("b ends with ...  "+str(bstring.endswith("...")))
#print("b ends with !    "+str(bstring.endswith("!")))

#print(phrase.split(" "))
#print(phrase.find("morning"))
#print(phrase.find("afternoon"))

#slicing
#print(phrase)
#print(phrase[11:29])
#print(phrase[11:29:3])
#print(phrase[-13:])
print(phrase[:6])
