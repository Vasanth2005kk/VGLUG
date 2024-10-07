prabha=[3,6,5,4,1,2]

prabha=[a,b,c,d,e,f]
prabha=[1,2,3,4,5,6]
'''

['e', 'f', 'a', 'd', 'c', 'b']
['c', 'b', 'e', 'd', 'a', 'f']
['a', 'f', 'c', 'd', 'e', 'b']
['e', 'b', 'a', 'd', 'c', 'f']
['c', 'f', 'e', 'd', 'a', 'b']
['a', 'b', 'c', 'd', 'e', 'f']

'''

arr=[3,6,5,4,1,2]
pepole=['a','b','c','d','e','f']
output=['','','','','','']

out=pepole.copy()

total=0

while True:
    for person,number in zip(out,arr):
        output[number-1]=person

    out=output.copy()
    print (out) 
    total+=1
    
    if out==pepole:
        print('answer = ',total)
        break       
        
for i in range(1,10000000):
    print(i)
