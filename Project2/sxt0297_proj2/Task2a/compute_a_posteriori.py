import sys 
# Defineing the probability values of Prior probability 
h1Prior =0.10  # Converting from Percent to Decimal
h2Prior = 0.20
h3Prior = 0.40
h4Prior = 0.20
h5Prior = 0.10 

#Declaring the Prior Probability Values of Cherry 
h1Cherry = 1.0 
h2Cherry = 0.75
h3Cherry = 0.50
h4Cherry = 0.25 
h5Cherry = 0.0 

#Declaring the Prior Probability Values of Lime
h1Lime = 0.0 
h2Lime = 0.25
h3Lime = 0.50 
h4Lime = 0.75
h5Lime = 1.0 

#main function 
def main():
    # opening the file in write mode
    file = open('result.txt', 'w')
    # Displaying and writing the Observation Sequence in console and in result.txt
    print('Observation Seqeunce Q: ',sys.argv[1])
    file.write('Observstion Sequence Q: ' +str(sys.argv[1]))
    observation = sys.argv[1]
    print(observation)
    print ('Length of Q: ', len(sys.argv[1]))
    file.write('Length Of Q: ' + str(len(sys.argv[1])))
    # params : outputFile and Command Line Argument (observation sequence)
    calculatePosteriorProbability(observation,file)

#Function to Display the Probability Values on the Command Line 
def printOnConsole(counter,h1Prob,h2Prob,h3Prob,h4Prob,h5Prob,probability_Cherry,probability_Lime,i):
        print ('\nAfter observation ', counter , ' = ', i, ':')
        print('P(h1 | Q) = ', h1Prob)
        print('P(h1 | Q) = ', h2Prob)
        print('P(h1 | Q) = ', h3Prob)
        print('P(h1 | Q) = ', h4Prob)
        print('P(h1 | Q) = ', h5Prob),'\n'
        print('Probability that the next candy we pick will be C, given Q: ', round(probability_Cherry, 5))
        print('Probability that the next candy we pick will be L, given Q: ', round(probability_Lime, 5))

#Function to write the Probability Values on the file result.txt 
def writeOnFile(counter,h1Prob,h2Prob,h3Prob,h4Prob,h5Prob,probability_Cherry,probability_Lime,file,i):
    file.write('\nAfter observation ' + str(counter) + ' = ' + i + ':\n')
    file.write('P(h1 | Q) = ' + str(h1Prob) + '\n')
    file.write('P(h2 | Q) = ' + str(h2Prob) + '\n')
    file.write('P(h3 | Q) = ' + str(h3Prob) + '\n')
    file.write('P(h4 | Q) = ' + str(h4Prob) + '\n')
    file.write('P(h5 | Q) = ' + str(h5Prob) + '\n')
    file.write('Probability that the next candy we pick will be C, given Q: ' + str(probability_Cherry) + '\n')
    file.write('Probability that the next candy we pick will be L, given Q: ' + str(probability_Lime) + '\n')

#Fucntion to compute the posterior probability 
def calculatePosteriorProbability(observation,file):
    #Initial Iteration 
    counter = 0 # Declaring counter variable to keep track of each Iteration
    global h1Prior, h2Prior, h3Prior ,h4Prior,h5Prior
    #Calculating the probability of cherry and Lime using the formula p(Q)= SUM(P(Q-i|h-i)*p(h-i)) [Reference : Prior and Posterior Probability Slides ]
    probability_Cherry = round(h1Cherry * h1Prior + h2Cherry * h2Prior + h3Cherry * h3Prior + h4Cherry * h4Prior + h5Cherry * h5Prior ,5)
    probability_Lime = round(h1Lime * h1Prior + h2Lime * h2Prior + h3Lime * h3Prior + h4Lime * h4Prior + h5Lime * h5Prior ,5)
    #Iterating Through each character from the sequence given in the command Line and calculate its probablity for each iteration 
    for i in observation:
        #Incrementing the counter after every iteration 
        counter += 1 
        # checking if the sequence is either 'C' or 'L'
        if i == 'C':
            #calculating P(h-i) using the formula P(h-i)= (P(Q-j|h-i)*P(h-i))/P(Q) [Refence : Prior and Posterior Probability Slides]
            # rounding the probability to 5 decimal places using the round()
            h1Prior = round((h1Cherry * h1Prior) / probability_Cherry,5)
            h2Prior = round((h2Cherry * h2Prior) / probability_Cherry,5)
            h3Prior = round((h3Cherry * h3Prior) / probability_Cherry,5)
            h4Prior = round((h4Cherry * h4Prior) / probability_Cherry,5)
            h5Prior = round((h5Cherry * h5Prior) / probability_Cherry,5)
        elif i == 'L':
            h1Prior = round((h1Lime * h1Prior) / probability_Lime,5)
            h2Prior = round((h2Lime * h2Prior) / probability_Lime,5)
            h3Prior = round((h3Lime * h3Prior) / probability_Lime,5)
            h4Prior = round((h4Lime * h4Prior) / probability_Lime,5)
            h5Prior = round((h5Lime * h5Prior) / probability_Lime,5)

        #Calculating the updated probability values after iteration using the same formula done above p(Q)= SUM(P(Q-i|h-i)*p(h-i)) [Reference : Prior and Posterior Probability Slides ]
        # rounding the probability to 5 decimal places using the round()
        probability_Cherry = round(h1Cherry * h1Prior + h2Cherry * h2Prior + h3Cherry * h3Prior + h4Cherry * h4Prior + h5Cherry * h5Prior,5)
        probability_Lime = round(h1Lime * h1Prior + h2Lime * h2Prior + h3Lime * h3Prior + h4Lime * h4Prior + h5Lime * h5Prior ,5)
        printOnConsole(counter,h1Prior,h2Prior,h3Prior,h4Prior,h5Prior,probability_Cherry,probability_Lime,i)
        writeOnFile(counter,h1Prior,h2Prior,h3Prior,h4Prior,h5Prior,probability_Cherry,probability_Lime,file,i)


if __name__ == "__main__":
	main()
