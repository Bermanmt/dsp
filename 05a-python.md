# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Both lists and Tuples are an ordered sequence of values. Both are indexed by integers, which means that the values inside can be accesed the same way in both cases. 

In both cases, the slice operator works and is used in the same way, however, the other operators such as Sort, reverse, etc. won't work on tuples.

The main difference between lists and tuples is that tuples are immutable, which means that they can't be changed or modified. 

The ones that work as keys in a dictionary are tuples due to the fact that they are immutable and this is a requirement dictionary keys have.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Both lists and sets are an ordered sequence of values, however, sets store only unique values. In the case of a list they can have a value repeat itself several times while sets can't. Also, as tuples, sets are immutable, so you can't assign items or manipulate its contents in any way. 

The performance between lists and sets, depends on what you are trying to do with them. When it comes to iterating through the element, lists are more efficient. However, when you want to check to see if a value exists inside the element, the process is more efficient with sets. This is due to the fact that sets work as an index and therefore it will be easier to find wether or not a value exists. 

An example of both would be if you have a website and are recording the user's activity. Everytime a user realizes an action, you want to record it and save it, therefore it would be good to use a list of actions, due to the fact that later you'll be able to see the amount of times a user realized an action inside the site. However, if you want to determine how many unique users have been interacting with the site, you might want convert the list of users into a set, therefore eliminating all of the noise and being able to determine if a specific user was on the site on a determined day. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's 'lambda' is a function that allows you to use functions without having to define them first (anonymous functions). Also it allows to apply functions within other built-in functions. For example, using it with the apply() function in the Pandas library or the map() and filter() functions.

Example: 

Lets say you have a list of integers and you realize your values are all wrong and they have to be 3 times larger and incremented by 4 (3x+4). To do this you can use the map function, but before you'd have to define a function:

myList = [1,2,4,4,6,2,7,5,8,54,74,24]

def changeValue(x):
	return 3*x+4

and then use the map function:

map(changeValue, myList)

or you could also use a loop and create a new list: 


newList= []
for i in myList:
	newList.append(3*i+4)

However, this takes space on your program and the changeValue() function might only be used once and its not efficient to have to do this. This is where the lambda function proves to be useful. The above can be simplified as follows: 

myList = map(lambda x: 3*x+4, myList)
	

Example with 'key' in 'sorted':

A perfect example for this would be if you'd like to sort a list of tuples by their last elements (like in q7_lists.py). In order to do this you could use the following lamda function:

tuplesList = [(1,2), (3,4), (8,3), (1,1)]

sorted(tuplesList, key= lambda tup: tup[-1])

what's happening here is the sorted function takes the tuplesList as argument. Then you use the 'key' argument to define the function you'd like to use to determine the key that the function will use to sort the list. In this case, the lambda function is used to indicate that you want to sort it by the last element of each tuple on the list. 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a way of constructing and manipulating lists within Python. They allow us to create lists from scratch or from existing sequences.

An example of this would be as follows: 

myList = [x*2 for x in range(10)]

This would create a list of the following form: 

myList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

Doing this is equivalent to building a list with a loop: 

myList = []
for i in range(10):
	myList.append(i*2)

With list comprehension you can build lists from existing lists also: 

myList = [x*2 for x in range(10)]
myOtherList = [x for x in myList if x%3 == 0 and x!=0]

This returns: 

myList= [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
myOtherList = [6, 12, 18]

In this case, myOtherList will contain all of the elements present in myList as long as they are divisible by 3 and they are different than 0. 

This would be the equivalent of using the filter() function on myList: 

filter(lambda x: x%3==0 and x!=0, myList)


Another way you can use list comprehension is for the same you'd use the map() function. Lets say you have a list of strings and you want to build another list in which all of the strings are uppercase: 

This is the initial list with strings: 

textList = ['The', 'wheels', 'on', 'the', 'bus', 'go', 'round', 'and', 'round']

If you use list comprehensions, you can create a new list with all of the strings in uppercase: 

upperTextList = [x.upper() for x in textList]

The result would be: 

['THE', 'WHEELS', 'ON', 'THE', 'BUS', 'GO', 'ROUND', 'AND', 'ROUND']

You can do the same thing with the map() function as follows and get the same result: 

map(lambda x: x.upper(), textArray)

List comprehensions in many cases substitute the map() and filter() functions, however, it is possible that sometimes what you can do with one might not be achieved by the other. Therefore, each of their capabilities depend on the situation you are exposed to. 

Dictionary and set comprehensions: 

Dict comprehensions and set, work in the same way that list comprehensions do: 

myDict = {x:'a'*x for x in [1,2,3,4]}

This will return a dictionary of the following form: 

{1: 'a', 2: 'aa', 3: 'aaa', 4: 'aaaa'}

You can also build a dict from two lists by using list comprehension and the zip() function: 

keys = ['a', 'b', 'c', 'd']
values = [x for x in range(30,35)]

myDict ={x:y for x,y in zip(keys,values)}

This returns a dictionary of the following form: 

{'a': 30, 'c': 32, 'b': 31, 'd': 33}

Using the same sintax as with dict comprehensions, you can create set comprehensions, which gives us a list of unique answers that might come in handy for certain operations: 

Lets say we have a string and we want to get all of the letters that the string contains but we want to leave out the vowels, we could do something like this: 

letters = {x for x in 'The wheels on the bus go round and round' if x not in 'aeiouAEIOU' and x!= ' '}

This returns a set with all the letters that are in the string that arent vowels or blank spaces: 

set(['b', 'd', 'g', 'h', 'l', 'n', 's', 'r', 'T', 'w', 't'])

If you would do this with list comprehensions it would still work, but you would get every single char that isn't a vowel and even if they repeat themselves: 

lettersList = [x for x in 'The wheels on the bus go round and round' if x not in 'aeiouAEIOU' and x!= ' ']

this will result in: 

['T', 'h', 'w', 'h', 'l', 's', 'n', 't', 'h', 'b', 's', 'g', 'r', 'n', 'd', 'n', 'd', 'r', 'n', 'd']



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

82

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





