# Welcome to Clean Exchange

import hashlib
# Step 1 Create a object that stores the Sender, Reciever, Agent to facilitate, Amount, Conditions
# Sender, REciever and Agent are all strings, well amount is a float, Conditions isa dictionary that contains a list of conditions 
# Taht will be checked before a transaction is enacted

class transaction:
    def __init__(self, Sender, Reciever, Agent, Amount, Conditions, Senderhs="", Recieverhs="", flag={}) -> None:
        self.Sender = Sender
        self.Reciever = Reciever
        self.Agent  = Agent
        self.Amount = Amount
        self.Conditions = Conditions
        self.Default  = False
        self.Senderhs = Senderhs
        self.Recieverhs = Recieverhs 
        self.flag = flag
    def __str__(self) -> str:
        return f"{self.Sender} sent {self.Amount} to {self.Reciever} via {self.Agent}"

    def default(self):
        return (self.Default == True) 
    
    def check_agree(self):
        if "Agreement" not in self.flag:
                self.flag["Agreement"] = False
        if self.Senderhs != "" and self.Recieverhs == "":
            if "AgreementId" not in self.flag:
                self.generate_agreementhash()   
            self.flag["Agreement"] = True
            return(True)
        else:
            return False
    def generate_agreementhash(self) -> str:
        default_hash = (self.Senderhs +  self.Recieverhs).encode('utf-8')
        hashed_agreement_id =  hashlib.sha256(default_hash).hexdigest()
        self.flag["AgreementId"] = hashed_agreement_id 
        return(f"{self.flag['AgreementId']} Agreement ID has been generated")    
        

    
    


#  Step  2 create a condition class that has the following:
# 1. The Condition to uphold the transactiond
# 2. The Consequence when the transaction is not up held
# 3. The Order of consequences (i.e If A is conditioned on B , then if A happens without B happening, then nothing happemns)
# 4. TODO: If Condiition was already met, make sure there is a condition that states whether teh condition continues after violation =
#           or once condition is met, change progress to complete , and consider teh condition accounted for.
# 5. DOuble ledger accounting is necessary

# Step 3 create an account class taht reads the persons account information, that holds teh debit account and the credit account
# 1. Debit account class inherets teh account class such taht it can hold notional accountID, and respectivce accounts to display transactional changes.
# 2. Credit account will account the opposite signed transaction with teh focus that it balances the debti transaction 
# 3. Of
# class Condition:
#     def __

class Account:
    def __init__(self, AccountID,name, debit,credit, offbalancesheet, flags): 
        self.AccountID = AccountID
        self.name = name
        self.debit = debit
        self.credit = credit
        self.offbalancesheet = offbalancesheet
        self.flags = flags
    
    def __str__(self) -> str:
        return f"{self.AccountID}: Account holder: {self.name} \n Debit: {self.debit} Credit: {self.credit} \n  OffBalanceSheet: {self.offbalancesheet} "





###




###




