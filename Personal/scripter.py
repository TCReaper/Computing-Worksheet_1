

# :regional_indicator_c: :regional_indicator_o: :regional_indicator_d: :regional_indicator_e:

def wordswitch():
        global n
        final = ""
        for i in n:
                if i == " ":
                        final = final + "\t" + "\t"
                else:
                        i = i.lower()
                        final = final + ":regional_indicator_" + i + ": "
        print(final)


while True:
        n = input("Sentence:   ")
        wordswitch()