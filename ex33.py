def for_looper(x, z):
    all_numbers = range(0, x, z)
    numbers = []
    for num in all_numbers:
        print 'At the top num is %d' % num
        numbers.append(num)
        print "Numbers now: ", numbers
    return numbers

def while_looper(x, z):
    i = 0
    numbers = []
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + z
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

numbers = while_looper(60,3)

print "The numbers: "

def print_num(numbers):
    for num in numbers:
        print num

print_num(numbers)
