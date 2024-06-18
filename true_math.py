from math import inf

def divide (first, second):
    if second == 0:
        return inf
    else:
        return round(first / second, 2)

if __name__ == '__main__':
    result3 = divide(491, 7)
    result4 = divide(15, 0)
    print(result3)
    print(result4)




