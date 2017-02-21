square = []
square_size = 0

def in_proc():
    global square_size
    value = input("Enter of square num : ")
    if value.isdigit():
        value = int(value)
        square_size = value
    else:
        print("Invalid value")
    return value

def out_proc():
    pass

def square_odd():
    pass

def square_even():
    pass

def square_init():
    global square
    square = [ i for i in range(square_size**2)]

def main():
    loop = True
    while loop:
        value = in_proc()
        if value == 0 :
            loop = False
        square_init()


if __name__ == "__main__":
    main()
