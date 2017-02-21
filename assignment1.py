def in_proc():
    value = input("Enter of square num : ")
    if value.isdigit():
        value = int(value)
    else:
        print("Invalid value")
    return value

def out_proc():
    pass

def square_odd():
    pass

def square_even():
    pass

def main():
    loop = True
    while loop:
        value = in_proc()
        print(value)
        if value == 0 :
            loop = False



if __name__ == "__main__":
    main()
