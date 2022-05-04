from stumanage.studef01 import *

while True:
    choice=screePrint()
    
    if choice==1:
        stuInput()
        
    elif choice==2:
        stuOuput()
        
    elif choice==3:
        stuSearch
        
    elif choice==4:
        stuModify()
        
    elif choice==5:
        stuDelete()
        
    elif choice==6:
        stuRank()
        
    elif choice==0:
        print('프로그램을 종료합니다.')
        break