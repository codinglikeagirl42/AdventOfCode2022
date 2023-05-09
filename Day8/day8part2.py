#Get data from text file
data = open("Day8/day8.txt", "r").read().split("\n")

x_total = len(data)
y_total = len(data[0])


def left_top_view(left_top):
  # how many trees can you see for tree
  view = 0
  for neighbor in left_top[::-1]:
    if tree <= neighbor:
      view += 1
      return(view)
    else:
      view += 1
  return(view)

def right_bottom_view(right_bottom):
  # how many trees can you see for tree
  view = 0
  for neighbor in right_bottom:
    if tree <= neighbor:
      view += 1
      return(view)
    else:
      view += 1
  return(view)
  
scenic_view = 0 
for x in range(1, (len(data) - 1)):
  for y in range(1, ((len(data[0]) - 1))):
    # iterate thru each tree
    tree = data[x][y]
    tree_line = []
    tree_verticle = []
    for i in range(len(data)):
      tree_line += data[x][i]
      tree_verticle += data[i][y]

    left = tree_line[0:y]
    right = tree_line[y + 1:]
    top = tree_verticle[0:x]
    bottom = tree_verticle[x + 1:]

    l = left_top_view(left)
    r = right_bottom_view(right)
    t = left_top_view(top)
    b = right_bottom_view(bottom)
    
    score = (l*r*t*b)
    if scenic_view < score:
      scenic_view = score
  

      

    

print("Part 2: " + str(scenic_view))
    
