# Here's some new strange stuff, remember type it exactly.

days= "Mon Tue Wed Thu Fri Sat Sun"
months= "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#\n 隔行？

print("Here are the days: ", days)
print("Here are the months: ", months)

#print define咗嘅嘢出嚟
#打咗\n 啲嘢就會隔行

print("""
There's something going on here. 
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# """ 三個要連住（否則會錯CODE），打咗之後，中間有幾多字，打幾多行都得
# """ 仲可以包住' " { } 之類嘅文字，make sure python唔會認錯佢係Program language

print("試吓\n打咗\nD乜")

#如果只打一個 " "，就會冇隔行，全部痴埋
#如果打 "" "" 會錯CODE
