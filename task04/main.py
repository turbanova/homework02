def done(words):
    for i in range(len(words)):
        word = words[i]    
        if len(word) > 10:
            print(str(i) + " " + word[:10])
        else:
            print(str(i) + " " + word)

a = input("words").split()
done(a)
