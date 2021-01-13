
##Challenge
##Prepare the Bunnies' Escape
##===========================
##You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 
##You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 
##Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
##Languages
##=========
##To provide a Python solution, edit solution.py
##To provide a Java solution, edit solution.java
##Test cases
##==========
##Inputs:
##    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
##Output:
##    (int) 7
##Inputs:
##    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
##Output:
##    (int) 11


def solution(maze):
    orig = maze
    counts = []
#make arrays for variations
    def arrays(orig):
        import copy
        temp = []
        arr = []
        for x in range(0, len(orig)):
            for y in range(0, len(orig[x])):
                temp = copy.deepcopy(orig)
                
                if temp[x][y] == 0:
                    temp[x][y] = 1
                    
                    arr.append(temp) 
                else:
                    temp[x][y] = 0
                    
                    arr.append(temp)
        arr.append(orig)
        return arr
    arr = arrays(maze)
#add walls on outer edge
    for group in arr:
        group.insert(0, [1]*len(group[1]))
        group.append([1]*len(group[1]))
               
        for x in range(len(group)):
            group[x].insert(0,1)
            group[x].append(1)
        
    #print(arr)
    
 #check how to progress the steps by checking against walls and the previous steps
            #arr shows walls and visited steps, orig is the original maze layout. 
    def solver(a):
        m = []
        for i in range(len(a)):
            m.append([])
            for j in range(len(a[i])):
                m[-1].append(0)
        m[1][1]= 1
        def make_step(k):
          for i in range(len(m)):
            for j in range(len(m[i])):
              if m[i][j] == k:
                if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
                  m[i-1][j] = k + 1
                if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
                  m[i][j-1] = k + 1
                if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
                  m[i+1][j] = k + 1
                if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
                   m[i][j+1] = k + 1                
                
        step = 0
    
        while m[len(m)-2][len(m[0])-2] == 0 and step < len(m)*len(m[0]):
            step += 1
            make_step(step)
##            print(step)
##            print(m)
##            print(a)
            
        
            
        return step


    for elem in arr:
        counts.append(solver(elem))
        #print(counts)

    return (min(counts)+1)
    
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))





