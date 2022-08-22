
import sys
EndOfFile = 'END OF INPUT'
path = []
Heuristics = []
def readInputData():
    inputFileFromUser = sys.argv[1]
    openInputFile = open(inputFileFromUser)
    for row in openInputFile:
        if EndOfFile not in row:
            city = row.split()
            Origin = city[0]
            Destination = city[1]
            Distance = city[2]
            forwardPath = [Origin,Destination,Distance]
            path.append(forwardPath)
            reversePath = [Destination,Origin,Distance]
            path.append(reversePath)
        else :
            break
    #print(path)
    return path
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
    if lengthOfcmdArgs == 4 :
        print("UninformedSearch")
        USearch(source,destination)
    else:
        print("InformedSearch")
        ISearch(source,destination)


def USearch(source,destination):
    Fringe = []
    getData = readInputData()
    nodespopped = 0
    nodesExpanded = 0
    nodesgenrated =1
    closedSet = []
    Fringe.append(node(source,0,0))
    flag = 0 
    lengthOfFringe = len(Fringe)
    print(lengthOfFringe)
    while 1:
        if len(Fringe) != 0 :
            popNode = Fringe.pop(0)
            nodespopped += 1
            if popNode.name == destination:
                print("Goal State reached")
                break
            # else:
            if popNode.name not in closedSet  :
                    nodesExpanded += 1 
                    for successor in getData:
                        if successor[0] == popNode.name:
                            cost = popNode.cost + int(successor[2])
                            newSuccessorNode = node(successor[1],cost,popNode.depth+1)
                            nodesgenrated+=1
                            newSuccessorNode.parent = popNode
                            Fringe.append(newSuccessorNode)
                            Fringe = sorted(Fringe, key = lambda node:node.cost)
                    closedSet.append(popNode.name)
        else :
            flag = 1
            break
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
        path = []
        path.append(destination)
        while popNode.parent is not None:
            path.append(popNode.parent.name)
            popNode = popNode.parent
        path.reverse()
        Loc=0
        while Loc < len(path)-1:
            for Trace in getData:
                if path[Loc] == Trace[0] and path[Loc + 1] == Trace[1]:
                    print (Trace[0], "to", Trace[1] + ",", Trace[2] + "km")
            Loc = Loc + 1



def ISearch(source, destination):
    Fringe = []
    getData = readInputData()
    readheuristics = getheuristics()
    nodespopped = 0
    nodesExpanded = 0
    nodesgenrated =1
    closedSet = []
    Fringe.append(node(source,0,0))
    flag = 0 
    lengthOfFringe = len(Fringe)
    noRange = 0
    Expanded = []
    while 1 :
        if len(Fringe) != 0:
            nodePopped = Fringe.pop(0)
            nodespopped += 1
            if nodePopped.name == destination:
                print("Goal Reached")
                break
            else:
                if nodePopped.name not in Expanded:
                    nodesExpanded += 1
                    # Expanded.append(nodePopped.name)
                    for succ in getData:
                        if succ[0] == nodePopped.name:
                            for h in readheuristics:
                                if h[0] == succ[1]:
                                    hval = h[1]
                            hValtot = nodePopped.cost + int(succ[2]) + int(hval)
                            tot_cost = nodePopped.cost + int(succ[2])
                            crNode = node(succ[1],tot_cost,hValtot)
                            nodesgenrated += 1 
                            crNode.parent = nodePopped
                            Fringe.append(crNode)
                            Fringe = sorted(Fringe, key = lambda node:node.depth)
                    Expanded.append(nodePopped.name)
        else :
            noRange = 1
            break 
    if (noRange == 1):
        # print("infintiy")
        print("nodes popped",str(nodespopped))
        print ("nodes expanded: " , str(nodesExpanded))
        print("nodesgenrated",str(nodesgenrated))
        print("Route")
        print('None')
    else:
        print("nodes popped",str(nodesExpanded))
        print ("nodes expanded: " , str(nodesExpanded))
        print("nodesgenrated",str(nodesgenrated))
        print ("distance: " , str(nodePopped.cost))
        path = []
        path.append(destination)
        while nodePopped.parent is not None:
            path.append(nodePopped.parent.name)
            nodePopped = nodePopped.parent
        path.reverse()
        Loc=0
        while Loc < len(path)-1:
            for TracePath in getData:
                if path[Loc] == TracePath[0] and path[Loc + 1] == TracePath[1]:
                    print (TracePath[0], "to", TracePath[1] + ",", TracePath[2] + "km")
            Loc = Loc + 1


def noRoute(nodespopped):
    print ("nodes expanded:", str(nodespopped))
    print ("distance: infinity")
    print ("route:\nnone")

if __name__ == "__main__":
    main()





