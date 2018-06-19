a = [] # empty list
b = [a] # list of one element with variable
big_list = [1,2,3,4,5] # 5 elements in a list

yes_list = [1, "a"] # don't do this

big_list[0] # get the first element in the list
print(big_list[0]) # 1
big_list[4] # get the fith element

print(big_list[5]) # da error

big_list.append(-1) # [1,2,3,4,5,-1]
#               index, value
big_list.insert(3, 25) # [1, 2, 3, 25, 4, 5, -1]

# big_list = big_list + [3] 
big_list += [3]

# [1,2,3,"a","b","c"]
print([1,2,3] + ["a", "b", "c"])
#   0           1
matrix = [[4, 5, 6], [1, 2, 3]]

print(matrix[0][0]) # 4

inner_list = matrix[1] # [1, 2, 3]
print(inner_list[2]) # 3


number_of_grades = 5
grades = []

for i in range(number_of_grades):
    # pregunta la nota
    nota = 9 # asume que pedistes la nota
    grades.append(nota)

# grades has 5 elements
print(grades)

# desde 5 hasta 20 brincando 2 cada vez
for i in range(5, 20, 2):
    print(i)


pares = [x + 1 for x in range(5, 100, 2)]
print(pares)