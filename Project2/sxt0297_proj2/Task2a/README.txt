Sujitraj Thirumurthy 
1001830297
CSE 5360 Artificial Intelligence - I 

Programming Language Used : Python 3.8.9 

To execute the program, run the following command:
    $ python compute_a_posteriori.py [sequence]

Example:
    $ python compute_a_posteriori.py LCLCL


Code Structure : 
We take the user input from the command line and pass the observation to the calculatePosteriorProbability function to calculate (p-i). 
we First compute probability of cherry and lime using base case formula p(Q)= SUM(P(Q-i|h-i)*p(h-i)). 
Then we take each character from the input and calculate P(h-i) using the formula P(h-i)= (P(Q-j|h-i)*P(h-i))/P(Q).
Since h-i is updated in previous step we compute probability of cherry and lime using updated values h and q to give results for every iteration

Reference : Prior and Posterior Probability Slides 
