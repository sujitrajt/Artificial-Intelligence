Name : Sujitraj Thirumurthy
UTA_ID : 1001830297
CSE 5360 Artificial Intelligence - I
Programming Assignment - 2 

TOWER OF HANOI 

TWO facts are present hanoi_facts1.txt, hanoi_facts2.txt 

The initial state and goal states are represented by preconds and effects respectively. 

Predicates:
(On a b) is true if a is present at location b
(small a b) is true if a is smaller than b as in hanoi problem we need to put smaller disk on top of bigger disk
(clear a) makes sure the given location "a" is clear.

CONSTANTS: 
We define constants disk1,disk2,disk3,disk4 and disk5 to denote the disks used in the tower of hanoi problem and PEGA,PEGB and PEGC to denote the pegs in the problem. Both peg and disk are defined as objects


In the hanoi_ops.txt file we define an action moveFromSourceToDestwhich moves a disk from one location to another. It may be from a disk to top of another disk or disk to an empty peg
Second action defined in the ops file is moveFromPegToPeg which moves a peg from one place to another 
Third and last action in the ops file is moveFromDiskToDisk which moves a disk from one place to another
The remove function deletes a disk from a location and clear makes sure the given location doesn't contain anything after the action is complete

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

7PUZZLE PROBLEM

TWO facts are present 7puzzle_facts1.txt, 7puzzle_facts2.txt 

The initial state and goal states are represented by preconds and effects respectively. 

Predicates:
(On a b) will be true if the value of TILE A is PRESENT at the Location B
(adjacent a b) will be true if the TILE A is Adjacent to TILE B
(clear a) makes sure the given location "a" is clear.

CONSTANTS: 
We define constants 1,2,3,4,5,6,7,X to denote and one to nine to denote the Location in the problem. 


In the 7Puzzle_ops.txt file we define an action  moveFromL1ToL2 moves a tile from one Tile location to another Tile Location. 
del function deletes the tile from previous location after being moved to a new location 