# Advent of Code 2022 Day 8
# https://adventofcode.com/2022/day/8

#Get data from text file
data = open("Day8/day8.txt", "r").read().split("\n")
trees_visable = 0

#total rows and columns
x_total = len(data)
y_total = len(data[0])

# get the outsitd visible trees form data grid, top and bottom
trees_visable += len(data)*2

# get the left and right side visiable trees form data grid
trees_visable += (len(data[0]) - 2)*2

#print(trees_visable)


def get_tree_visible(x, y):

    tree = data[x][y]
    
    
    #get tallest tree to the right

    #get tallest tree to the top

    #get tallest tree to the bottom


for x in range(1, (len(data) - 1)):
    for y in range(1, ((len(data[0]) - 1))):
        # iterate thru each tree
        tree = data[x][y]
        tree_line = []
        tree_verticle = []
        for i in range(len(data)):
            tree_line += data[x][i]
            tree_verticle += data[i][y]
        #print(tree)
        #print(tree_line)
        #print(tree_verticle)
        left = max(tree_line[0:y])
        right = max(tree_line[y+1:])
        top = max(tree_verticle[0:x])
        bottom = max(tree_verticle[x+1:])
        #print(bottom)
        # if tree visable count
        if left < tree or right < tree or top < tree or bottom < tree:
            trees_visable += 1

                        
print("Part 1: " + str(trees_visable))

    
