

#Logic help - https://www.youtube.com/watch?v=FXQWIWHaFBE

#Get data from text file
data = open("Day7/day7.txt", "r").read().split("\n")

#create dictionary for directories
directories_size = {"/home":0}

#set starting directories
location = "/home"
numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

for line in data:
    if line[0] == "$":

        if line[2:4] == "cd":

            # Set location cd / as home 
            if line[5:7] == "/":
                location = "/home"
            
            #update location going back 1 location
            elif line[5:7] == "..":
                #https://www.w3schools.com/python/ref_string_rfind.aspin
                location = location[0:location.rfind("/")]

            else:
                #add new location to directory to directory_size
                directory_name = line[5:]
                location = location + "/" + directory_name
                directories_size.update({location:0})
    
    elif line[0] in numbers:

        #Get size of directory
        size = int(line[:line.find(" ")])
        directory = location

        for i in range(location.count("/")):
            directories_size[directory] += size
            directory = directory[:directory.rfind("/")]


#part1
total = 0

for directory in directories_size:

    #print(directory + ": " + str(directories_size[directory]))

    if directories_size[directory] < 100000:
        total += directories_size[directory]
          
print("Part 1: " + str(total))

#part 2
total2 = 70000000

for directory in directories_size:

    if (30000000 - (70000000 - directories_size["/home"])) <= directories_size[directory]:

        if directories_size[directory] < total2:
            total2 = directories_size[directory]
          

print("Part 2: " + str(total2))
