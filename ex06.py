types_of_people = 10
#types_of_ppl is the vaviable
#10 is the data, data type = integer
x = f"There are {types_of_people} types of people."
#

binary = "Binary"
do_not = "don't"
#do_not is the vaviable
#don't is the data, data type = str
y = f"Those who know {binary} and those who {do_not}."

print (x)
print (y)

print (f"I said {x}")
print(f"I also said: '{y}'")
#print string入面，function, string入面搵返 ｛｝入面嗰個Vaiviables 

hilarious = False
#define "hilarious"

joke_evaluation = "Isn't that joke so funny?! {}"
# define Joke_evaluation, 但string入面有個Blanket係未有嘢，留返係下個指令，決定佢填咩入去

print(joke_evaluation.format(hilarious))
#print string入面嘅嘢， .format指要run "joke_evaluation"嗰個String入面嗰個 Blanket，Fill "hilarious"入去


w = "This is the left side of..."
e = "a string with a right side."
#define w同e 呢兩個Strings

print (w + e)
# (w同e)



#點解要.format? 因為.format可以係每次指令，決定填唔同嘅嘢入去
#如果只有 f str 加 blankets, 就要每次都打唔同嘅FUNCTIONS