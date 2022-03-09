# Write Python 3 code in this online editor and run it.
l=[2,2,1,7,3,2,8,3,3,3,1,5,6,6,6,9,9]
l.sort()
c=l[0]
p=0
for i in range(1,len(l)-1):
    if c^l[i]!=0 and l[i]!=l[i-1] and l[i]!=l[i+1]:
        p+=1
        
    c=c^l[i] 
if l[len(l)-2]!=l[len(l)-1]:   
    p+=1
    
print(p)
