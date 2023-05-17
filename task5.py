import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def square(list_input):
    list_sq=[]
    for i in range(0,len(list_input)):
        sq_num=pow(list_input[i],2)
        list_sq.append(sq_num)
    return(list_sq)

def cube(list_input):
    list_cube=[]
    for i in range(0,len(list_input)):
        cube_num=pow(list_input[i],3)
        list_cube.append(cube_num)
    return(list_cube)


list_input = []
list_input = [int(numbers) for numbers in input("Enter the list item: ").split()]

list_sq = square(list_input)
list_cube = cube(list_input)
plt.plot(list_input,list_sq)
plt.plot(list_input,list_cube)
plt.title('Square and Cubic graph')
  

plt.xlabel('Input List Number')
plt.ylabel('Square and Cube of number')

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,1005,50))

plt.show()