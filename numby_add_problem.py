import numpy

arr=numpy.array([[1,2,3],[4,5,6]])
arr_1=numpy.array([[10,20,30],[40,50,60]])

a,b=list(arr.shape),list(arr_1.shape)

if a==b:
    output=arr+arr_1
    print(output)