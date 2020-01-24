
=== Object orientation 

We're going to make a program that represents animals in a zoo.

At some point in the future this will also include visitors who can interact with the animals.

But for now

===

In your `main.py` program file

* Create a class that represents a Tiger

A Tiger has
- orange fur
- four legs
- big size
- when it is startled it will "Snarl!"
- when is is angered it will "Roar!"

* When you have specified your Tiger class

- Create Tiger object from it.
- Make the tiger Roar
- Make the tiger Snarl

* Can you make a second tiger?
- and make it Roar?
- and make it Snarl?

* Print the fur for an exisitng tiger
* Can you make a "white" Tiger by chainging one of the existing tiger's fur?
* can you see that the change only affects that tiger

===

* Read about the ```__init__(self)``` magic function for classes

* Alter your Tiger class 
- so that when you make one, you can pass the colour you want as a parameter
- and then so that if you DONT pass a colour, it defaults to one.

===

Alter your `main.py` 
* Make a copy of your Tiger class and name it HouseCat

A HouseCat has
- black fur
- four legs
- small size
- when it is startled it will "Meow!"
- when is is angered it will "Hiss!"

* When you have specified your HouseCat class

- make a housecat with black fur
- make another housecat with tortoiseshell fur
- print both cats' fur

===

Note that Tigers and HouseCats are kinda similar, 

* Read about "inheritance".

* Create a new class called FelineTerror

- move the _common_ parts of HouseCat and Tiger into it
- set HouseCat and Tiger to inherit from it

Hopefully, your code that makes a big pile of animals still works!