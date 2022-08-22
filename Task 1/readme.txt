UTA ID : 1001830297
Name : Sujitraj Thirumurthy
CSE5360 - Artificial Intelligence - I 
Project 1 
Task - 1

Code written in Python 3.8.9

Compilation: 
1) For Uninformed Search run the following command 

    python find_route.py input1.txt Bremen Kassel

2) For Informed Search run the following command 

    python find_route.py input1.txt Bremen Kassel h_kassel.txt

Code Structure 

-> The Search is done based on the number of arguments given by the user , if argv is 4 then uninformed search is done
    else informed search is done 

-> The input1.txt file is read to get the map  and h_kassel.txt file is read to get the heuristics data 

-> function UnInformSearch performs the Uninformed Search 
-> function InformSearch performs the Informed Search with the given heuristic value retrieved from the given heuristic file