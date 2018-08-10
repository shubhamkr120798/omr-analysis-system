#Solution for part 2, We are trying to use Bayesian Networks and then find the largest 
#subset which are all independent from each other, so these will be the main concepts 
#which are the root cause of all errors. d-separation in bayesian networks can also be a solution

def solveBayes():
    #Bayesian Method
    dictt={}
    sums=0
    for i in len(d):
        for j in len(d[i-1]):
            dictt[d[i-1][j-1]]+=1
            sum+=1
    
    prob=[]
    for key, value in dictt.items():
            prob[key]=(value)/sum
    pcond=[]
