from fin_struct import transaction
from testing_mod import get_random_string
import random

def create_cases(numcases, lee=10):
    listofnames = ["" for _ in range(numcases)]
    
    # Generate transactions up to the number of cases=
    for i in range(numcases):
        listofnames[i] = get_random_string(lee)
        
    listofcases = [{} for _ in range(numcases)]

    for j in range(len(listofcases)):
        listofcases[j] = transaction(Sender = random.choice(listofnames),Reciever = random.choice(listofnames), Agent= "HOST",
            Amount = random.randint(1000,5000), Conditions={})
    
    return(listofcases)


# Generate Cases 

cases = create_cases(10)

list(map(print,cases))
    
    

