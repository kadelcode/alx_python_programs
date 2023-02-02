- Write a class ```Square``` that defines a square by: (based on ```5-square.py```)
	- Private instance attribute: ```size```:
		- property ```def size(self):``` to retrieve it
		- property setter ```def size(self, value):``` to set it:
			- ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
			- If ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0

	- Private instance attribute: ```position```:
		- property ```def position(self):``` to retrieve it
		- property setter ```def position(self, value):``` to set it:
			- ```position``` must be a tuple of 2 positive integers, otherwise raise a ```TypeError``` exception with the message ```position must be a tuple of 2 positive integers```
	- Instantiation with optional ```size``` and optional ```position: def __init__(self, size=0, position=(0, 0)):```
	- Public instance method: ```def area(self):``` that returns the current square area