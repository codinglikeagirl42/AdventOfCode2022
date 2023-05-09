#Get data from text file
data = open("Day8/day8.txt", "r").read().split("\n")
trees_visable = 0

# get the outsitd visible trees form data grid, top and bottom
trees_visable += len(data)*2

# get the left and right side visiable trees form data grid
trees_visable += (len(data[0]) - 2)*2

#function for Part 2
def scenic_view(trees):
  # how many trees can you see form tree
  view = 0
  for neighbor in trees:
    if tree <= neighbor:
      view += 1
      return(view)
    else:
      view += 1
  return(view)

scenic_view_score = 0 

# iterate thru each tree
for x in range(1, (len(data) - 1)):
  for y in range(1, ((len(data[0]) - 1))):
    
    #look at a single tree
    tree = data[x][y]
    tree_line = []
    tree_verticle = []

    #get all trees on the same horizontal and vertile axis as tree
    for i in range(len(data)):
      tree_line += data[x][i]
      tree_verticle += data[i][y]
    
    #Need to reverse the order of left and top- as we are looking at them for part 2
    #Order Doesn't matter for part 1 as we want the Max value
    #Used a lot of print statements to figure out the logic
    left = (tree_line[0:y])[::-1]
    right = tree_line[y + 1:]
    top = (tree_verticle[0:x])[::-1]
    bottom = tree_verticle[x + 1:]

    #part 1 find how many trees are visible and add to total 
    if max(left) < tree or max(right) < tree or max(top) < tree or max(bottom) < tree:
      trees_visable += 1

    #part 2 check trees can be seen to by each tree for best location for tree house
    score = (scenic_view(left)) * (scenic_view(right)) * (scenic_view(top)) * (scenic_view(bottom))
    
    #simple way to find the highest scenic view score and best location for the tree house
    if scenic_view_score < score:
      scenic_view_score = score
   
print("Part 1: " + str(trees_visable))
print("Part 2: " + str(scenic_view_score))