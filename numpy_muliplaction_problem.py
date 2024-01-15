import numpy

arr=numpy.array([[1,2,3],[4,5,6]])
arr_1=numpy.array([[10,20,30],[40,50,60],[70,80,90]])

a=list(arr.shape)
b=list(arr_1.shape)

if a[1]==b[0]:
    mulit=numpy.dot(arr,arr_1)
    print(mulit)