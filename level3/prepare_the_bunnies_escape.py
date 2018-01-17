## Search ##
# If the tile you're about to go to has been previously visited, you've found a loopback!


def answer(maze):
    
    def build(maze):
        tiles = {} # Dict to be filled with tiles
        for i in range(0,len(maze)): # Loop thru each row
            for j in range(0,len(maze[i])): # Loop thru each column

                tile = {}
                tile["value"] = maze[i][j] # Value of tile, 1 or 0
                
                # UP
                if i == 0: #First level
                    tile["up"] = None
                else: # Any other level
                    tile["up"] = str(i-1)+"-"+str(j)

                # DOWN
                if i == len(maze)-1:
                    tile["down"] = None
                else:
                    tile["down"] = str(i+1)+"-"+str(j)

                # LEFT
                if j == 0: #Leftmost tile
                    tile["left"] = None
                else: 
                    tile["left"] = str(i)+"-"+str(j-1)
                
                #RIGHT
                if j == len(maze[i])-1: #Rightmost tile
                    tile["right"] = None
                else:
                    tile["right"] = str(i)+"-"+str(j+1)

                position = str(i)+"-"+str(j) # Tile position, "00" or "23"

                tiles[position] = tile

        return tiles

    def isdeadend(board, tile):
        # Ex. tile (3,2) is a dead-end
        # Sum of (3,2) neighbord is 3
        #  0 1 1 1 
        #  0 0 0 0 
        #  1 0 1 0
        #  1 1 1 0
        
        # Check if exists before grabbing the value
        if board[tile]["down"] != None:
             down = board[ board[tile]["down"] ]["value"]
        else:
            down = 1
        if board[tile]["up"] != None:
            up = board[ board[tile]["up"] ]["value"]
        else:
            up = 1
        if board[tile]["left"] != None:
            left = board[ board[tile]["left"] ]["value"]
        else:
            left = 1
        if board[tile]["right"] != None:
            right = board[ board[tile]["right"] ]["value"]
        else:
            right = 1
        
        # Border tile's with no neighbor (None) can still be dead-ends
        if up == None:
            up = 1
        if down == None:
            down = 1
        if left == None:
            left = 1    
        if right == None:
            right = 1

        # Sum the result
        result = up+down+left+right
        
        # If sum is greater than 3 ITS A DEAD END!
        if tile == "0-0":
            result = False
        elif result >= 3:
            result = True
        else:
            result = False
        
        return result
    
    
    def step(board, tile, exit, length, visited, prev_tile, path):
        
        if tile not in path:
            length += 1
        #print(length)
        #print(board)
        visited.append(tile)
        #print("PREVIOUS TILE: "+prev_tile+"\n")
        #print("dead"+str(dead_ends))
        #print(board[tile])
        #print(board[tile]["down"])
        #print(board[board[tile]["down"]]["value"])
        
        value = board[tile]["value"]
        down = board[tile]["down"]
        up = board[tile]["up"]
        right = board[tile]["right"]
        left = board[tile]["left"]
        
        #print("TILE: "+tile+" U:"+str(up)+" D:"+str(down)+" L:"+str(left)+" R:"+str(right)+" V:"+str(value))
        path.append(tile)
        
        # If tile (currently on) is a deadend, close it off!
        deadend = isdeadend(board, tile)
        if deadend == True:
            board[tile]["value"] = 1
        
        # If tile found, return length!
        if tile == exit:
            return length
        
        # Go DOWN
        elif down != None and board[down]["value"] == 0 and down not in visited:
            next_tile = down

        # Go RIGHT
        elif right != None and board[right]["value"] == 0 and right not in visited:
            next_tile = right
        
        # Go UP
        elif up != None and board[up]["value"] == 0 and up not in visited:
            next_tile = up

        # Go LEFT
        elif left != None and board[left]["value"] == 0 and left not in visited:
            next_tile = left
        
        #######
        # Go DOWN
        elif down != None and board[down]["value"] == 0:
            next_tile = down
        
        # Go RIGHT
        elif right != None and board[right]["value"] == 0:
            next_tile = right
        
        # Go UP
        elif up != None and board[up]["value"] == 0:
            next_tile = up

        # Go LEFT
        elif left != None and board[left]["value"] == 0:
            next_tile = left
        
        # If you can't go any direction, you're stuck!
        else:
            return 1000
            
        # If tile (about to visit) has been visited before, make tile a wall, and go back to previous tile!
        if next_tile in visited:
            board[next_tile]["value"] = 1
            length -= 1
            visited = []
        
        return step(board,next_tile,exit,length,visited,prev_tile, path)
            
         
    def start(maze):
        start = "0-0" #Name of start node
        exit = str(len(maze)-1)+"-"+str(len(maze[0])-1) #Name of exit node
        path_lengths = []

        # Solve initial config without removing walls
        board = build(maze)
        path_length = step(board, start, exit, 0, [], "", [])
        path_lengths.append(path_length)
        
        # Solve subsequent maps for each present wall
        for row in range(len(maze)):
            # Location of walls in row
            walls = [i for i,x in enumerate(maze[row]) if x == 1]
            #print(walls)
            # One-by-one switch each wall to hallway and find shortest path
            for wall in range(len(walls)):
                # Change a wall to hallway
                maze[row][walls[wall]] = 0
                # Build board structure
                
                #for level in maze:
                    #print(level)
                #input(" ")
                
                board = build(maze)
                #print(board)
                # Calculate shortest path of this board arrangement
                path_length = step(board, start, exit, 0, [], "", [])
                # Add calculated path lenght to path_lengths
                path_lengths.append(path_length)
                # Restore changed wall
                maze[row][walls[wall]] = 1

        print(path_lengths)
        
        shortest_path_length = min(path_lengths)
        return shortest_path_length

    shortest_path_length = start(maze)
    return shortest_path_length


maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
solution = answer(maze)
print("LENGTH: "+str(solution))
if solution == 40:
    print("SUCCESS")
else:
    print("FAILURE")
    
maze = [[0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]]
solution = answer(maze)
print("LENGTH: "+str(solution))
if solution == 7:
    print("SUCCESS")
else:
    print("FAILURE")

maze = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]
solution = answer(maze)
print("LENGTH: "+str(solution))
if solution == 11:
    print("SUCCESS")
else:
    print("FAILURE")

maze = [[0, 1],
        [1, 0]]
solution = answer(maze)
print("LENGTH: "+str(solution))
if solution == 3:
    print("SUCCESS")
else:
    print("FAILURE")
