names = ["gio","ika","ika","nana","ika","nana","gio"]
a={}         
set1 = set(names)                
def countNames():
        for i in set1:
            a[i]= names.count(i)
        print(a)          
        
countNames()        

                                                                                                                                                                                                                                  
def countNames1():
        for i in set1:
            c=0
            for j in names:
                if i==j:
                    c+=1
            a[i]= c
        print(a)          
        
countNames1()                                                                                                                                                                                                                                   