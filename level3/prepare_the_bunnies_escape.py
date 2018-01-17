
def answer(maze):
    

    def build(maze):
        tiles = {} # Dict to be filled with tiles
        for i in range(len(maze)): # Loop thru each row
            for j in range(len(maze[i])): # Loop thru each column
                
                #input("ROW: "+str(i)+" COLUMN: "+str(j))

                tile = {}
                tile["value"] = maze[i][j] # Value of tile, 1 or 0
                
                # UP
                if i == 0: #First level
                    tile["up"] = None
                else: # Any other level
                    tile["up"] = str(i-1)+str(j)

                # DOWN
                if i == len(maze)-1:
                    tile["down"] = None
                else:
                    tile["down"] = str(i+1)+str(j)

                # LEFT
                if j == 0: #Leftmost tile
                    tile["left"] = None
                else: 
                    tile["left"] = str(i)+str(j-1)
                
                #RIGHT
                if j == len(maze)-1: #Rightmost tile
                    tile["right"] = None
                else:
                    tile["right"] = str(i)+str(j+1)

                position = str(i)+str(j) # Tile position, "00" or "23"
                
                #print(tile)

                tiles[position] = tile

        return tiles

    def step(board, tile, exit, length, prev_tile):

        length += 1
        #print(length)
        print("CURRENT TILE: "+tile)
        #print("PREVIOUS TILE: "+prev_tile+"\n")
        #print("dead"+str(dead_ends))
        #print(board[tile])
        #print(board[tile]["down"])
        #print(board[board[tile]["down"]]["value"])
        
        # If tile found, return length!
        if tile == exit:
            return length
        
        # Go DOWN
        elif board[tile]["down"] != None and board[ board[tile]["down"] ]["value"] == 0:
            
            if board[tile]["down"] == prev_tile:
                board[tile]["value"] = 1
                print("DEADEND!"+tile)
                length -= 1
                return step(board,prev_tile,exit,length,tile)
            else:
                return step(board,board[tile]["down"],exit,length,tile)

        # Go RIGHT
        elif board[tile]["right"] != None and board[ board[tile]["right"] ]["value"] == 0:
            
            if board[tile]["right"] == prev_tile:
                board[tile]["value"] = 1
                print("DEADEND!"+tile)
                length -= 1
                return step(board,prev_tile,exit,length,tile)
            else:
                return step(board,board[tile]["right"],exit,length,tile)

        # Go LEFT
        elif board[tile]["left"] != None and board[ board[tile]["left"] ]["value"] == 0:
            
            if board[tile]["left"] == prev_tile:
                board[tile]["value"] = 1
                print("DEADEND!"+tile)
                length -= 1
                return step(board,prev_tile,exit,length,tile)
            else:
                board[tile]["value"] = 1
                length -= 1
                return step(board,board[tile]["left"],exit,length,tile)
            
        # Go UP
        elif board[tile]["up"] != None and board[ board[tile]["up"] ]["value"] == 0:
            
            if board[tile]["up"] == prev_tile:
                board[tile]["value"] = 1
                print("DEADEND!"+tile)
                length -= 1
                return step(board,prev_tile,exit,length,tile)
            else:
                return step(board,board[tile]["up"],exit,length,tile)

            
    def start(maze):
        start = "00" #Name of start node
        exit = str(len(maze)-1)+str(len(maze)-1) #Name of exit node
        path_lengths = []

        input(maze)

        for row in range(len(maze)):
            # Location of walls in row
            walls = [i for i,x in enumerate(maze[row]) if x == 1]
            #print(walls)
            # One-by-one switch each wall to hallway and find shortest path
            for wall in range(len(walls)):
                # Change a wall to hallway
                maze[row][walls[wall]] = 0
                # Build board structure
                #input(maze)
                board = build(maze)
                #print(board)
                # Calculate shortest path of this board arrangement
                path_length = step(board, start, exit, 0, "")
                # Add calculated path lenght to path_lengths
                path_lengths.append(path_length)
                # Restore changed wall
                maze[row][walls[wall]] = 1

        print(path_lengths)
        
        path_lengths = [x for x in path_lengths if x is not None]
        
        shortest_path_length = min(path_lengths)
        return shortest_path_length

    shortest_path_length = start(maze)
    return shortest_path_length



maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
solution = answer(maze)
print("LENGTH: "+str(solution))

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
solution = answer(maze)
print("LENGTH: "+str(solution))




