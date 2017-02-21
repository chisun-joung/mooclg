square = []
square_size = 0
isvalid_input = False

def in_proc():
    global square_size, isvalid_input
    isvalid_input = False
    value = input("Enter of square num : ")
    if value.isdigit():
        value = int(value)
        if value > 2 and (value%2 == 1 or value%4 == 0):
            isvalid_input = True
            square_size = value
    return value

def out_proc():
    for i in range(square_size):
        print(square[i*square_size:i*square_size + square_size])

def square_odd():
    pass

def square_even():
    pass

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
        out_proc()
    print("===== End =====")

if __name__ == "__main__":
    main()
