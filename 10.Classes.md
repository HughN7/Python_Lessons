# Classes

When you start learning classes, you'll encounter something called _object-oriented programming_. 
- Basically, it's a way/style to write code

Classes are blueprint/schematics/etc. used to create **Objects**

Think of classes like a cookie cutter or a recipe to create a cookie. 
- Cookie Cutter/Recipe == Class
- Cookie == Object

# Cookie Example 
To continue with the analogy: A cookie can have certain properties:
- Shape
- Flavor
- Topping
- and more

If we were to create a "cookie" class in python it would look like this:

```python
class Cookie:
  def __init__(self, shape, flavor, topping):
    self.shape = shape
    self.flavor = flavor
    self.topping = topping
    
  def displayProperties():
    print("Cookie properties:")
    print("Cookie shape: ", self.shape)
    print("Cookie flavor: ", self.flavor)
    print("Cookie topping: ", self.topping)
```

Once you've created the class, you can use it to create a cookie object:
- After this, you can do all sorts of things like access the properties of the object and call functions in the object
```python
strawberry_cookie = Cookie("star", "strawberry", "vanilla frosting")
strawberry_cookie.displayProperties() #I'm calling the displayProperties() function inside of the class using the .

print("Confirming that the cookie flavor is:", strawberry_cookie.flavor) #I'm now accessing the properties of the object
```

# __init__() and self

You might notice the function `__init__()` and the keyword `self` above. 

The function `__init__()` is part of every class.
- When the class is initially created, __init__() function runs to set properties of the class. 
- Technically this function is optional but generally used every time you create a class. 

The self keyword on the otherhand refers to anything that's inside of the class. Be it properties or functions. 
- This is why in the function `displayProperties()` you'll notice that I used `self.shape` since shape is part of the class instead of just `shape`

