data=[
    {'id':20241001,'name':'ranjith'},
    {'id':20241002,'name':'ragupathi'},
    {'id':20241003,'name':'rishith'},
    {'id':20241004,'name':'vasanth'},
    {'id':20241005,'name':'santhosh'}
]
error_block=[]
id =int(input("Enter id to search :"))
for i in data:
    if i['id'] == id :
        print(i)
    else:
        error_block.append(False)
else:        
    if not all(error_block):
        print("your data is not in the list !")
    