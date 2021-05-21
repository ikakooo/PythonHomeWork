def applyToEach(L,f):
    a=[]
    for i in range(len(L)):
        a.append( f(i))
    return a

def f(k):
    return k*5

print(applyToEach([1,5,7,8]),f)
print(map(abs,[1,-2,3,-7]))

def sdfjhskdf():
     a=[]
     for i in map(abs,[1,-2,3,-7]):
         a   .append(i)
         
     print(a)    
     
sdfjhskdf()  

   
      
def sdfuhsdgf():
    a=[]
    l1 = [34,54,456,56]
    l2= [534,546,67,68,64]
    for i in map(min, l1,l2):
          a.append(i)          
    print(a)      
sdfuhsdgf()  


# thisset = {"apple", "banana", "cherry"}
# 
# thisset.add("orange")  
# print(thisset)
#   
# # name = ['ana','jpogd', 'dsf','sdf']
# # grade = ['B','A+','A','A']
# # cource = [2.00,6.0001,20.0002,9.01]
# 
# import random 
# a= {}
# for i in range(0,10):
#     a[random.randint(0,9)]=random.randint(0,9)
#     
# print (a["ika"])
# a["axali"] = 200
# for i,j in a.items():
#     print (i,j)  