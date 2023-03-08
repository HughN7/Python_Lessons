# Try Except

Sometimes you want python to test a piece of code for errors and catch it: 

Let's say for some weird reason, you think we can divide stuff by 0
```python
some_number = 10 / 0
print(some_number)
```

Obviously this won't work. Then you'll crash and burn the app you're making with this piece of code.
Therefore, python has a way to test our piece of code first AND if there are any errors, python let's us do something about it. 

```python
try:
	some_number = 10/0
	print(some_number)
except:
	print("Error encountered! You can't do this you dumb dumb")

```

## Optional Add-Ons to Try and Except:
With the try-except block, you can also add an `else` statement or a `finally` statement

The else statement basically says:
- If there was no errors, let's do something

```python
try:
	some_number = 10/2
	print(some_number)
except:
	print("Error encountered! You can't do this you dumb dumb")
else:
	print("There wasn't anything wrong with the code")
```

The `finally` statement basically says:
- Even if there was or wasn't an error - run this piece of code

```python
try:
	some_number = 10/0
	some_number2 = 10/2
	print(some_number)
	print(some_number2)

except:
	print("Error encountered! You can't do this you dumb dumb")
finally:
	print("You better have double-checked your work!")

```


## Raising An Error

Sometimes you can also force python to say "There's an error in this piece of code". This is called raising / throwing an exception. 

You use the raise keyword to do this:

```python
test_number = 2
if test_number != 9000:
	raise Exception("Why isn't this 9000?") 

```

This is useful if you're inside a function and want to throw an error so that you can do something outside of it.

```python
def cookies():
	cookies = 2
	if cookies != 9000:
		raise Exception("Why aren't there 9000 cookies?!") 
	print(cookies)


try:
	cookies() #calling / summoning the function
except:
	print("There wasn't enough cookies")
```

You can also raise or throw specific types of exceptions. 
- You can see some built in errors / exceptions in python here: https://www.geeksforgeeks.org/built-exceptions-python/

Here's an example below
```python
try:
    x = int("not a number") #trying to convert "not a number" into a number
except ValueError:
    print("Cannot convert string to integer!")
```

You can also create your own custom exceptions. But we'll leave that for another day. 
