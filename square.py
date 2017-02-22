square = []
square_size = 0
isvalid_input = False
isodd_square = False
left_square, over_square = False, False
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


def move_diagonal_left(position):
    position[0] -= 1
    position[1] -= 1


def check_square_out(position):
    global left_square, over_square
    left_square, over_square = False, False
    if position[0] < 0:
        left_square = True
    if position[1] < 0:
        over_square = True


def move_next_position(position):
    if not left_square and over_square:
        position[1] += square_size
    if left_square and not over_square:
        position[1] += square_size
    if left_square and over_square:
        position[0] = 0
        position[1] = 1


def put_value(position, value):
    index = position[0] + position[1]*square_size
    if square[index] == 0:
        square[index] = value
    else:
        position[1] += 1
        index = position[0] + position[1]*square_size
        square[index] = value


def square_odd():
    print("2n+1 Solving")
    # 첫번째 중앙에 1을 위시
    current_index = square_size//2
    current_value = 1
    square[current_index] = current_value
    current_position = [current_index//square_size, current_index%square_size]
    max_value = square_size**2
    while current_value <= max_value:
        current_value += 1
        move_diagonal_left(current_position)
        check_square_out(current_position)
        move_next_position(current_position)
        put_value(current_position, current_value)


def square_even():
    print("4n Solving")

def square_init():
    global square
    square = [0 for i in range(square_size**2)]

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
