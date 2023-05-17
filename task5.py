
def square(list_input):
    list_sq=[]
    for i in range(0,len(list_input)):
        sq_num=pow(list_input[i],2)
        list_sq.append(sq_num)

    print(list_sq)



def cube(list_input):
    list_cube=[]
    for i in range(0,len(list_input)):
        cube_num=pow(list_input[i],3)
        list_cube.append(cube_num)

    print(list_cube)


list_input = []
list_input = [int(numbers) for numbers in input("Enter the list item: ").split()]
square(list_input)
cube(list_input)
print(list_input)