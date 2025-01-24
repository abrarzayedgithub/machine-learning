import numpy as np

#(1,2,3) - tuple
#[1,2,3] - list
#{1,2,3} - sets
initial_array = np.array([1,2,3])
print(initial_array)
print("type of dataset is: \n",type(initial_array))
print(".............")
second_array = np.array([[1,2,3],
                         [4,5,6]])
print(second_array.shape)
print("type of dataset is: \n",type(second_array))
print(".........")
second_array = np.array([[[1,2,3],
                         [4,5,6]],
                         [[1,2,3],
                         [4,5,6]]])
print(second_array.shape)
print("type of dataset is: \n",type(second_array))
print("............")
print(second_array.size)
print("type of dataset is: \n",type(second_array))

z_data = np.zeros((2,2))
print(z_data)
print("........")
o_data = np.ones((2,3))
print(o_data)
print("........")
f_data = np.full((2,3),4)
print(f_data)
print(".............")

e_data = np.eye(3)
print(e_data)   #identity matrix
print(".........")

a_data = np.arange(4) #its arange not arrange
print(a_data)
print(".......")
a_data = np.arange(4,4) #its arange not arrange
print(a_data)
print("........")
a_data = np.arange(4,4.5,0.1) #(start,end,step size)
print(a_data)
print(".........")
l_data = np.linspace(1,3,4)
print(l_data)

print("........")
import numpy as np
array_data = np.array(np.arange(2,50,2))
print(array_data[5])
print("...........")
#array_data = np.array(np.arange(2,50,2))
#print(array_data[5,:])#it should be use in multidimensional array. 

array_data = np.array([np.arange(2,50,2),np.arange(2,50,2)])
print(array_data[1, :])

print("..........")

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a = a1 + a2
print(a)
print("...-...")

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a = np.dot(a1,a2)
print(a)
print(".......")
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a = np.var(a1)
print(a)
print("....")
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a = np.min(a1)
print(a)
print(".......")
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
a3 = a2 >4.5
print(a3)
print(".........")
a1 = np.array([1,2,3,4.5,5,6])
a2= [3,0,2] #multi indexing 
a3 = a1[a2]
print(a3)
print("...............")
randomdata = np.random.randint(1,11)
print(randomdata)
print("...........")
randomdata = np.random.randint(1,11, size = (2,2))
print(randomdata)
print(".........")
randomdata = np.random.rand(1,11)
print(randomdata)