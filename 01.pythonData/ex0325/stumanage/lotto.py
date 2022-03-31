class Lotto:
    mynum=0
    
    def __init__(self, mynum=[]):
        self.mynum=mynum
        
    def __str__(self):
        mynumprint='로또입력번호 : {}, {}, {}, {}, {}, {}'.format(mynum[0],mynum[1],mynum[2],mynum[3],mynum[4],mynum[5])
        return mynumprint
    
    
        
    
    