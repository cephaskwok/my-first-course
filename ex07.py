print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))

#.format指示要填返前面個｛｝入面嘅嘢，填個SNOW字入去，後面寫咗個STRING SNOW is a string with a word in it.

print("And everywhere that Mary went.")
print("." * 10) # what'd that do?
# .......... 同一個data x10次

end1= "C"
end2= "h"
end3= "e"
end4= "e"
end5= "s"
end6= "e"
end7= "B"
end8= "u"
end9= "r"
end10= "g"
end11= "e"
end12= "r"

# watch end = ' ' at the end. try removing it to see what happens

print (end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print (end7 + end8 + end9 + end10 + end11 + end12)


#點解冇咗end=' '會變咗隔行?
print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)