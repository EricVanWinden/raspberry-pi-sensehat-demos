from NumberMatrix import *
from Orientation import *

"""
for i in range(101):
    matrix = create_matrix(99 - i)
    print_matrix(matrix)
"""





for i in range(360):
    coordinate = calculate_coordinate(i)
    for j in range(coordinate.__len__()):
        print(str(i) + "\t" + str(j) + "\t" + str(coordinate[j][0]) + "\t" + str(coordinate[j][1]))
