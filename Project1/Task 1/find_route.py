#CSE 5360 - Artificial Intelligence
#Project 1 - Task 1

#Student Name: Sujitraj Thirumurthy 
#Student Id: 1001830297

#Written in Python (Version 3.8.9)



import sys #importing sys to get command line argument
EndOfFile = 'END OF INPUT' #Reading the file till END OF INPUT
path = [] #Adding the path Forward and backward from the given input file 
Heuristics = [] #Collecting the Heuristic value from Given File 


#Creating a Node Data structure to store the values of state name , it's Parent , cost and depth of the node
class node:
    def __init__(self,name,cost,depth):
        self.name = name
        self.parent = None
        self.cost = cost
        self.depth = depth 
    # def __str__(self):
    #     return '< name = '+self.name+' cost = '+ str(self.cost)+', depth = '+str(self.depth)+', Parent = Pointer to {'+str(self.parent)+'} >' 


def main():
    lengthOfcmdArgs = len(sys.argv)
    print("lengthOfArgument",lengthOfcmdArgs)
    source = sys.argv[2]
    destination = sys.argv[3]
    print("Source and Destination",source,destination)
    # checking from CMD argument , if len is 4 we will perform Uninformed Search
    if lengthOfcmdArgs == 4 :
        print("UninformedSearch")
        UnInformSearch(source,destination)
    # Else perfoem Informed Search
    else:
        print("InformedSearch")
        InformSearch(source,destination)

#function to read input file from the user
def readInputData():
    inputFileFromUser = sys.argv[1]
    openInputFile = open(inputFileFromUser)
    for row in openInputFile:
        if EndOfFile not in row:
            city = row.split()
            source = city[0]
            Destination = city[1]
            Distance = city[2]
            forwardPath = [source,Destination,Distance]
            path.append(forwardPath)
            reversePath = [Destination,source,Distance]
            path.append(reversePath)
        else :
            break
    #print(path)
    return path

 # function to read heuristic data from the file and store it in Heuristics   
def getheuristics():
    inputHeuristicsFromUser =  sys.argv[4]
    openHeuristicFile = open(inputHeuristicsFromUser)
    for row in openHeuristicFile:
        if EndOfFile not in row :
            heuristic = row.split()
            heuristicCity = heuristic[0]
            heuristicValue = heuristic[1]
            cityHeuristics = [heuristicCity,heuristicValue]
            Heuristics.append(cityHeuristics)
        else :
            break
    # print(Heuristics)
    return Heuristics


        



def UnInformSearch(source,destination):
    Fringe = [] #creating a list to store the fringe values
    getData = readInputData() #reading inputfile
    nodespopped = 0 #Initialising the number of nodes popped
    nodesExpanded = 0 #Initilising the number of nodes expanded
    nodesgenrated =1 #Initialising the number of nodes generated
    closedSet = [] #Creating a closed set list to check if the city is already visited or not
    Fringe.append(node(source,0,0)) #Appending a intial node(source) to the Fringe 
    flag = 0 #This variable is to set to 1 if the fringe is empty and no route is possible
    lengthOfFringe = len(Fringe)
    # print(lengthOfFringe)
    while 1:
        #checking if the fringe is not empty
        if len(Fringe) != 0 :
            #popping out the first node in the fringe
            popNode = Fringe.pop(0)
            #incrementing the popped node counter
            nodespopped += 1
            # checking if the popped node is the destination 
            if popNode.name == destination:
                print("Goal State reached")
                break
            # checking if the popped node is presrent in the closed set
            if popNode.name not in closedSet  :
                    #incrementing the node Expanded counter
                    nodesExpanded += 1 
                    for successor in getData:
                        #generating the successors to the popped node
                        if successor[0] == popNode.name:
                            #calculating the cost
                            cost = popNode.cost + int(successor[2])
                            #creating a new node 
                            newSuccessorNode = node(successor[1],cost,popNode.depth+1)
                            #incrementing the generated node
                            nodesgenrated+=1
                            #adding the successor parent to be the popped node
                            newSuccessorNode.parent = popNode
                            #appending the new node to the fringe
                            Fringe.append(newSuccessorNode)
                            #sorting the fringe based on cost
                            Fringe = sorted(Fringe, key = lambda node:node.cost)
                    #adding the popped node to the closed set (visited city)
                    closedSet.append(popNode.name)
        #if the fringe is empty and goal state not reached setting the flag to 1
        else :
            flag = 1
            break
    #if no route printing the following information
    if (flag == 1): 
        print("No Route Exists")
        print("nodes popped",str(nodespopped))
        print ("nodes expanded: " , str(nodesExpanded))
        print("nodesgenrated",str(nodesgenrated))
        # print ("distance: " , str(popNode.cost))
        print("Route")
        print('None')
    else:
        print("nodes popped",str(nodespopped))
        print ("nodes expanded: " , str(nodesExpanded))
        print("nodesgenrated",str(nodesgenrated))
        print ("distance: " , str(popNode.cost))
        #creating a route list to store the path from source to destination
        route = []
        route.append(destination)
        #Tracking back the source from the destination by tracking the parent
        while popNode.parent is not None:
            route.append(popNode.parent.name)
            popNode = popNode.parent
        route.reverse()
        count=0
        # Tracking back the route to get the distance
        while count < len(route)-1:
            for Trace in getData:
                if route[count] == Trace[0] and route[count + 1] == Trace[1]:
                    print (Trace[0], "to", Trace[1] + ",", Trace[2] + "km")
            count = count + 1



def InformSearch(source, destination):
    Fringe = [] #creating a list to store the fringe values
    getData = readInputData()
    readheuristics = getheuristics()
    nodespopped = 0 #Initialising the number of nodes popped
    nodesExpanded = 0 #Initilising the number of nodes expanded
    nodesgenrated =1 #Initialising the number of nodes generated
    closedSet = [] #Creating a closed set list to check if the city is already visited or not
    Fringe.append(node(source,0,0))
    flag = 0 
    lengthOfFringe = len(Fringe)
    noRange = 0
    # Expanded = []
    while 1 :
        #checking if the fringe is not empty
        if len(Fringe) != 0:
            #popping out the first node in the fringe
            nodePopped = Fringe.pop(0)
            nodespopped += 1
            # checking if the popped node is the destination 
            if nodePopped.name == destination:
                print("Goal Reached")
                break
            else:
                if nodePopped.name not in closedSet:
                    nodesExpanded += 1
                    for succ in getData:
                        if succ[0] == nodePopped.name:
                            for h in readheuristics:
                                #getting the heuristics value
                                if h[0] == succ[1]:
                                    hval = h[1]
                            #adding the total heuristic cost
                            hValtot = nodePopped.cost + int(succ[2]) + int(hval)
                            tot_cost = nodePopped.cost + int(succ[2])
                            #creating a successor node with total cost and heuristic value
                            crNode = node(succ[1],tot_cost,hValtot)
                            nodesgenrated += 1 
                            crNode.parent = nodePopped
                            Fringe.append(crNode)
                            Fringe = sorted(Fringe, key = lambda node:node.depth)
                    closedSet.append(nodePopped.name)
         #if no route printing the following information
        else :
            noRange = 1
            break 
    #if no route printing the following information
    if (noRange == 1):
        # print("infintiy")
        print("nodes popped",str(nodespopped))
        print ("nodes expanded: " , str(nodesExpanded))
        print("nodesgenrated",str(nodesgenrated))
        print("Route")
        print('None')
    else:
        print("nodes popped",str(nodespopped))
        print ("nodes expanded: " , str(nodesExpanded))
        print("nodesgenrated",str(nodesgenrated))
        print ("distance: " , str(nodePopped.cost))
        path = []
        path.append(destination)
        #Tracking back the source from the destination by tracking the parent
        while nodePopped.parent is not None:
            path.append(nodePopped.parent.name)
            nodePopped = nodePopped.parent
        path.reverse()
        count1=0
        # Tracking back the route to get the distance
        while count1 < len(path)-1:
            for TracePath in getData:
                if path[count1] == TracePath[0] and path[count1 + 1] == TracePath[1]:
                    print (TracePath[0], "to", TracePath[1] + ",", TracePath[2] + "km")
            count1 = count1 + 1

if __name__ == "__main__":
    main()





