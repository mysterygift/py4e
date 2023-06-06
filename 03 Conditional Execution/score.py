strscore = input("Please enter a score between 0.0 and 1.0: ")
try :
    fscore = float(strscore)
    if fscore >= 0.0 and fscore <= 1.0 :
        if fscore >= 0.9 :
            print("A")
        elif fscore >= 0.8 :
            print("B")
        elif fscore >= 0.7 :
            print("C")
        elif fscore >= 0.6 :
            print("D")
        elif fscore >= 0.5 :
            print("E")
        elif fscore < 0.5 :
            print("even uni students would do better than this bruh")
    else :
        print("Something tells me you're lying.\n")
except :
    print("Numbers only, fool")