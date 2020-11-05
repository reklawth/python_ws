# %%
val1 = 1 # Integer
val2 = 1.2 # float
val3 = 1 + 3j #complex number

# %%
# Let us print out the types
print(type(val1)) # should be integer
print(type(val2)) # should be float
print(type(val3)) # should be complex

# %%
a = 'hello world!'
print(a)
print(a[2:3])

# %%
print(a[2:])
print(a[2:4] + a[7:8])
print(a[0] * 5)

# %%
# Lists are surrounded by brackets are are an ordered sequence
mylist = ['abc', 1, 2.5]
print(mylist[0])
mylist[1:]

# %%
# Tuples are immutable
mytuple = (1, 'hi', 2.5)
#mytuple[1] = 'bye' # Error! Can't change tuple value
mytuple[1]

# %%
# Dictionaries are key-value paiers, similar to maps, hases or associative arrays in other languages
d = {} # This is an empty dictionary
d['one'] = 1 # assignment
d_new ={'name': 'Tim', 'address':'123 Main Street', 'city':'Seattle'}
[d_new.keys(), d_new.values()]

# %%
# Functions
def printme(whtattoprint):
    print(whtattoprint)
    return

printme("hello")

def mymax(first, second):
    if (first > second):
        return first
    return second

printme(mymax(1,2))

# %%
# Lambda functions are anonymous functions, that we pass as arguments
names = [(1, 'Mary'), (2, 'Bob'), (3, 'Zahra'), (4, 'Lu')]
names.sort(key = lambda name: name[1])
names

# %%
