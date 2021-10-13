class ATM(object):
    def __init__(self, cashWithdrawl, balanceEnquiry):
        self.cashWithdrawl=cashWithdrawl
        self.balanceEnquiry=balanceEnquiry
    
    def cashWithdrawl(cash):
        print(cash+"WithDrawed")
    
    def balanceEnquiry():
        print("you are looted:) have a nice day")
marx=ATM(300,600)
marx.cashWithdrawl(200)
marx.balanceEnquiry()