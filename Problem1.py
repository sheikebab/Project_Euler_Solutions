number=raw_input("Enter a Number:")

def sum_3_5(x):
    list = []
    y = int(x)
    for i in range(y):
        list.append(i)
        print list
    final = []
    for i in list:
        if i%3==0 or i%5==0 :
            final.append(i)
        else:
            continue
    result = sum(final)
    return result


print "Sum of multiples of 3 or 5 bewlow", number
print sum_3_5(number)