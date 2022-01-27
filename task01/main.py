lst = ["apple", "vine", "sweets", 125, "moscow city", 500]
for i in lst:
    if type(i) is str:
        print("The text is " + str(i))
    elif type(i) is int or type(i) is float:
        print("The value is " + str(i))
