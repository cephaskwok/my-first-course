formatter = "{} {} {} {}"

#define formatter

print(formatter.format(1,2,3,4))
#string入面有四個integers

print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format("True", "False", "False", "True"))
#true同False係command words, 驗證嘅結果，Qoute咗就變咗字

print(formatter.format(formatter, formatter, formatter, formatter))
#

print(formatter.format(
    "try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
))

#放唔同嘅嘢入去formatter四個格仔入面。