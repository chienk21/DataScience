# Python program explaining 
# around() function 
# Rounds to nearest decimal place given and if no decimal place given rounds to 0 decimal places/nearest integer
  
import numpy as np 
  
in_array = [.555, 1.534, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", in_array) 
  
round_off_values = np.around(in_array, decimals = 1) 
print ("\nRounded values : \n", round_off_values) 
  
  
in_array = [.53, 1.54, .71] 
print ("\nInput array : \n", in_array) 
  
round_off_values = np.around(in_array) 
print ("\nRounded values : \n", round_off_values) 
  
in_array = [.5538, 1.33354, .71445] 
print ("\nInput array : \n", in_array) 
  
round_off_values = np.around(in_array, decimals = 3) 
print ("\nRounded values : \n", round_off_values)


# Python program explaining 
# around() function 
  
import numpy as np 
  
in_array = [1 ,4, 7, 9, 12] 
print ("Input array : \n", in_array) 
  
round_off_values = np.around(in_array) 
print ("\nRounded values : \n", round_off_values) 
  
  
in_array = [133 ,344, 437, 449, 12] 
print ("\nInput array : \n", in_array) 
  
round_off_values = np.around(in_array, decimals = -2) 
print ("\nRounded values upto 2: \n", round_off_values) 
  
in_array = [133 ,344, 437, 449, 12] 
print ("\nInput array : \n", in_array) 
  
round_off_values = np.around(in_array, decimals = -3) 
print ("\nRounded values upto 3: \n", round_off_values) 




# Python program explaining 
# rint() function 
# rounds to nearest integer/0 decimal places
import numpy as np 
  
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", in_array) 
  
rintoff_values = np.rint(in_array) 
print ("\nRounded values : \n", rintoff_values) 
  
  
in_array = [.53, 1.54, .71] 
print ("\nInput array : \n", in_array) 
  
rintoff_values = np.rint(in_array) 
print ("\nRounded values : \n", rintoff_values) 
  
in_array = [.5538, 1.33354, .71445] 
print ("\nInput array : \n", in_array) 
  
rintoff_values = np.rint(in_array) 
print ("\nRounded values : \n", rintoff_values)

# Python program explaining 
# rint() function 
import numpy as np 
  
in_array = [1 ,4, 7, 9, 12] 
print ("Input array : \n", in_array) 
  
rintoff_values = np.rint(in_array) 
print ("\nRounded values : \n", rintoff_values) 
  
in_array = [133 ,344, 437, 449, 12] 
print ("\nInput array : \n", in_array) 
  
rintoff_values = np.rint(in_array) 
print ("\nRounded values upto 2: \n", rintoff_values) 
  
in_array = [133 ,344, 437, 449, 12] 
print ("\nInput array : \n", in_array) 
  
rintoff_values = np.rint(in_array) 
print ("\nRounded values upto 3: \n", rintoff_values) 




# Python program explaining 
# fix() function 
# rounds nearest integer towards 0/cuts off the rounding of integer at whatever the integer is
  
import numpy as np 
  
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", in_array) 
  
fixoff_values = np.fix(in_array) 
print ("\nRounded values : \n", fixoff_values) 
  
  
in_array = [.53, 1.54, .71] 
print ("\nInput array : \n", in_array) 
  
fixoff_values = np.fix(in_array) 
print ("\nRounded values : \n", fixoff_values) 
  
in_array = [.5538, 1.33354, .71445] 
print ("\nInput array : \n", in_array) 
  
fixoff_values = np.fix(in_array) 
print ("\nRounded values : \n", fixoff_values) 




# Python program explaining 
# ceil() function 
# ceiling of a number is the next greatest integer
import numpy as np 
  
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", in_array) 
  
ceiloff_values = np.ceil(in_array) 
print ("\nRounded values : \n", ceiloff_values) 
  
  
in_array = [.53, 1.54, .71] 
print ("\nInput array : \n", in_array) 
  
ceiloff_values = np.ceil(in_array) 
print ("\nRounded values : \n", ceiloff_values) 
  
in_array = [.5538, 1.33354, .71445] 
print ("\nInput array : \n", in_array) 
  
ceiloff_values = np.ceil(in_array) 
print ("\nRounded values : \n", ceiloff_values) 




# Python program explaining 
# floor() function 
# floor of a number is the next smallest integer
import numpy as np 
  
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", in_array) 
  
flooroff_values = np.floor(in_array) 
print ("\nRounded values : \n", flooroff_values) 
  
  
in_array = [.53, 1.54, .71] 
print ("\nInput array : \n", in_array) 
  
flooroff_values = np.floor(in_array) 
print ("\nRounded values : \n", flooroff_values) 
  
in_array = [.5538, 1.33354, .71445] 
print ("\nInput array : \n", in_array) 
  
flooroff_values = np.floor(in_array) 
print ("\nRounded values : \n", flooroff_values) 




# Python program explaining 
# trunc() function 
# truncates the value of the number to the integer before the decimal place
  
import numpy as np 
  
in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", in_array) 
  
truncoff_values = np.trunc(in_array) 
print ("\nRounded values : \n", truncoff_values) 
  
  
in_array = [.53, 1.54, .71] 
print ("\nInput array : \n", in_array) 
  
truncoff_values = np.trunc(in_array) 
print ("\nRounded values : \n", truncoff_values) 
  
in_array = [.5538, 1.33354, .71445] 
print ("\nInput array : \n", in_array) 
  
truncoff_values = np.trunc(in_array) 
print ("\nRounded values : \n", truncoff_values) 



# Python program explaining 
# numpy.add() function 
# when inputs are scalar 

import numpy as np 
in_num1 = 10
in_num2 = 15

print ("1st Input number : ", in_num1) 
print ("2nd Input number : ", in_num2) 
	
out_num = np.add(in_num1, in_num2) 
print ("output number after addition : ", out_num)

# Python program explaining 
# numpy.add() function 
# when inputs are array 
# adds arrays in a similar manner as matrices

import numpy as geek 

in_arr1 = geek.array([[2, -7, 5], [-6, 2, 0]]) 
in_arr2 = geek.array([[5, 8, -5], [3, 6, 9]]) 

print ("1st Input array : ", in_arr1) 
print ("2nd Input array : ", in_arr2) 
	
out_arr = geek.add(in_arr1, in_arr2) 
print ("output added array : ", out_arr) 


# Python program explaining 
# numpy.negative function 
# makes numbers in array opposite sign than before (towards neg)

import numpy as geek 

in_arr = geek.array([[2, -7, 5], [-6, 2, 0]]) 

print ("Input array : ", in_arr) 
	
out_arr = geek.negative(in_arr) 
print ("negative of array elements: ", out_arr) 




# Python program explaining 
# power() function 
#output is int
# first array to the power of the second array
import numpy as np 

# input_array 
arr1 = [2, 2, 2, 2, 2] 
arr2 = [2, 3, 4, 5, 6] 
print ("arr1		 : ", arr1) 
print ("arr1		 : ", arr2) 

# output_array 
out = np.power(arr1, arr2) 
print ("\nOutput array : ", out) 

# Python program explaining 
# power() function 
#NEG EXPONENTS NOT ALLOWED
import numpy as np 

# input_array 
arr1 = np.arange(8) 
exponent = 2
print ("arr1		 : ", arr1) 

# output_array 
out = np.power(arr1, exponent) 
print ("\nOutput array : ", out) 




# Python program explaining 
# true_divide() function 
# first array divided by the second array
import numpy as np 

# input_array 
arr1 = [6, 7, 2, 9, 1] 
arr2 = [2, 3, 4, 5, 6] 
print ("arr1		 : ", arr1) 
print ("arr1		 : ", arr2) 

# output_array 
out = np.true_divide(arr1, arr2) 
print ("\nOutput array : \n", out) 



# Python program explaining 
# true_divide() function vs floor_divide()
#floor_divide truncates to the smallest integer
import numpy as np 

# input_array 
arr1 = np.arange(5) 
arr2 = [2, 3, 4, 5, 6] 
print ("arr1		 : ", arr1) 
print ("arr1		 : ", arr2) 

# output_array 
out = np.floor_divide(arr1, arr2) 
out_arr = np.true_divide(arr1, arr2) 
print ("\nOutput array with floor divide : \n", out) 
print ("\nOutput array with true divide : \n", out_arr) 


print ("\nOutput array with floor divide(//) : \n", arr1//arr2) 
print ("\nOutput array with true divide(/) : \n", arr1/arr2) 




# Python3 code demonstrate reciprocal() function 
# input array elements must be floats or else recipricols will get 0
# importing numpy 
import numpy as np 

in_arr = [2., 3., 8.] 
print ("Input array : ", in_arr) 
	
out_arr = np.reciprocal(in_arr) 
print ("Output array : ", out_arr) 




# Python program explaining 
# divide() function 
# outputs actual division values
import numpy as np 

# input_array 
arr1 = [2, 27, 2, 21, 23] 
arr2 = [2, 3, 4, 5, 6] 
print ("arr1		 : ", arr1) 
print ("arr2		 : ", arr2) 

# output_array 
out = np.divide(arr1, arr2) 
print ("\nOutput array : \n", out) 



# Python program explaining 
# expm1() function 

import numpy as np 

in_array = [1, 3, 5] 
print ("Input array : \n", in_array) 

exp_values = np.exp(in_array) 
print ("\nExponential value of array element : "
	"\n", exp_values) 

expm1_values = np.expm1(in_array) 
print ("\n(Exponential value of array element) - (1) "
	": \n", expm1_values) 


# Python program explaining 
# log1p() function 
# output is ln(1+x) where x is an element in input array
import numpy as np 

in_array = [1, 3, 5] 
print ("Input array : ", in_array) 

out_array = np.log1p(in_array) 
print ("Output array : ", out_array) 



# Python3 code demonstrate logaddexp() function 
# Calculates log(exp(arr1) + exp(arr2))
# importing numpy 
import numpy as np 

in_num1 = 2
in_num2 = 3
print ("Input number1 : ", in_num1) 
print ("Input number2 : ", in_num2) 

out_num = np.logaddexp(in_num1, in_num2) 
print ("Output number : ", out_num) 


# Python program explaining 
# numpy.random.sample() function 
  
# importing numpy 
import numpy as geek 
  
# output random value 
out_val = geek.random.random_sample() 
print ("Output random float value : ", out_val)




# Python program explaining 
# log() function 
import numpy as np 
  
in_array = [1, 3, 5, 2**8] 
print ("Input array : ", in_array) 
  
out_array = np.log(in_array) 
print ("Output array : ", out_array) 
  
  
print("\nnp.log(4**4) : ", np.log(4**4)) 
print("np.log(2**8) : ", np.log(2**8)) 


