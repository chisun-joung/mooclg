square = []
square_size = 0
isvalid_input = False
isodd_square = False
def in_proc():
    global square_size, isvalid_input, isodd_square
    isvalid_input, isodd_square = False , False
    value = input("Enter of square num : ")
    if value.isdigit():
        value = int(value)
        if value > 2 and (value%2 == 1 or value%4 == 0):
            isvalid_input = True
            square_size = value
            if value%2 == 1:
                isodd_square = True
    return value

def out_proc():
    span = len(str(max(square)))
    for i in range(square_size):
        ret = square[i*square_size:i*square_size + square_size]
        for j in ret:
            print("{0:>{1}} ".format(j,span),end = '')
        print()

def square_odd():
    print("2n+1 Solving")

def square_even():
    print("4n Solving")

def square_init():
    global square
    square = [i for i in range(square_size**2)]

def main():
    loop = True
    while loop:
        value = in_proc()
        if value == 0 :
            loop = False
            continue
        if not isvalid_input:
            print("Invalid value")
            continue
        square_init()
        if isodd_square:
            square_odd()
        else:
            square_even()
        out_proc()
    print("===== End =====")

if __name__ == "__main__":
    main()
