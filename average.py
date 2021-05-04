def listAverage(list):
    if len(list) == 0:
        return 0
    else:
        return sum(list) / len(list)
    
#a = [1,3,5,7,9]
#print(listAverage(a))