'''
1) Write a program to swap two numbers without using a third variable. [2.5 marks]
x = 6
y = 7
print ("Before Swaping:  ")
print("Value of x: ", x, "and y : ",y)
x, y = y, x
print ("After Swapping: ")
print(' Value of x : ', x, " and y: ", y)
'''
'''
2) Explain overloading and overriding by writing a sample program. [2.5 marks]
Overloading: 
1)Method Overloading is feature of OOPs which makes it possible to give the same name to more than one method within a class if the arguments passed differ.
2) Two or more methods having the same name but different parameters.

Overriding:
Child class redefining methods present in the base class with the same parameters.

example:
def add(*args):
      sum = 0
      for i in args:
         sum +=i
      print(sum)

add()
add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)

Output:
0
10
30
60
100
'''

'''

3) Write a program to find the second largest number in an array. [2.5 marks]

def secondmax(arr):
      abc = [x for x in arr if x < max(abc)]
      return max(abc)

if  __name__ == '__main__':
      arr = [11, 21,  4, 45, 99 ]
      print (secondmax(arr))



OuptPut:
45
'''
'''
5) Write a program or algorithm to implement bubble sort. [5 marks]

You do not have to use any library for this.

nums = [5, 3, 8, 6, 7, 2]
def sort(nums):
for i in range(len(nums) -1, 0, -1):
      for j in range(i):
           if nums[j] > nums[j+1]:
              temp = nums[j]
              nums[j] = nums[j+1]
              nums[j+1] = temp

OuptPut:
[2, 3, 5, 6, 7, 8]
'''
'''
6) Write a JavaScript program to compute the union of two arrays. [5 marks]

Sample Data : console.log(union([1, 2, 3], [100, 2, 1, 10]));

Output: [1, 2, 3, 10, 100]
var unionArr =_.union([1, 2, 3], [100, 2, 1,10]);
console.log(unionArr);


OutPut:
[1, 2, 3, 10,100]
'''
'''
7) Write a JavaScript function to find the unique elements from two arrays. [2.5 marks]

Test Data: console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));

- Output: ["1", "2", "3", "4", "5", "6"]

const arr1 = [1, 2, 3, 4, 5]
const arr2 = [ 1, [2], [3, [[4]]],[5,6]];

let unique1 = arr1.filter((0)) => arr2.indexof(0) === -1);
let unique2 = arr2.filter((0)) => arr1.indexof(0) === -1);

const unique = unique1.cancat(unique2)
'''
'''
8) Write a query to find the name (first_name, last_name) of the employees who have a manager and worked in a USA based department. [2.5 marks]

You need to provide SQL query only

employees

- EMPLOYEE_ID

- FIRST_NAME

- LAST_NAME

- EMAIL

- PHONE_NUMBER

- HIRE_DATE

- JOB_ID

- SALARY

- COMMISSION_PCT

- MANAGER_ID

- DEPARTMENT_ID

departments

- DEPARTMENT_ID

- DEPARTMENT_NAME

- MANAGER_ID

- LOCATION_ID

locations

- location_id 

- street_address

- postal_code

- city

- state_province

- country_id
SELECT first_name, last_name FROM employees
WHERE MANAGER_ID IN (select EMPLOYEE_ID
IN (SELECT DEPARTMENT_ID FROM departments WHERE location_id
IN (select location_id from locations where country_id ='USA')));
'''
'''
9) Consider above schemas and Write a query to find the name (first_name, last_name), and salary of the employees who earns more than the average salary and works in any of the IT departments. [2.5 marks]

You need to provide SQL query only
SELECT  * FROM employees
WHERE salary >
ALL(SELECT avg(salary) FROM employees GROUP BY department_id);
'''
'''






'''10) Write a program or algorithm for Two Elements whose sum is closest to zero.
 array [-23, 12, -35, 45, 20, 36]
 '''

def minAbsSumPair(arr,arr_size):
    inv_count = 0
    if arr_size < 2:
        print('Invalid Input')
min_l = 0
min_r =1
min_sum = arr[0] +arr[1]
for l in range(0, arr_size, -1):
        for r in range(l+1, arr_size):
            sum = arr[l] +arr[r]
            if abs(min_sum)> abs(sum):
                min_sum =sum
                min_l = l
                min_r = r
print("Two Elements whos sum is minimu are ", arr[min_l], "and", arr[min_r])
'''
'''
11) From the following tables, write a SQL query to find all salespeople and customers located in the city of London. [2.5 marks]

You need to provide SQL query only

Salesman

- salesman_id

- name

- city

- commission

Customer

- customer_id

- cust_name

- city

- grade

- salesman_id
SELECT salesman_id  "ID", name, 'salesman'
FROM salesman
WHERE city = 'London'
UNION 
(SELECT customer_id "ID", cust_name, 'customer'
FROM customer
WHERE city = 'London');
'''

                
                
    
