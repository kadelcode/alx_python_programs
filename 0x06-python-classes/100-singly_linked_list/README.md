- Write a class ```Node``` that defines a node of a singly linked list by:
	- Private instance attribute: ```data```:
		- property ```def data(self):``` to retrieve it
		- property setter ```def data(self, value):``` to set it:
			- ```data``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```data must be an integer```

	- Private instance attribute: ```next_node```:
		- property ```def next_node(self):``` to retrieve it:
		- property setter ```def next_node(self, value):``` to set it:
			- ```next_node``` can be ```None``` or must be a ```Node```, otherwise raise a ```TypeError``` exception with the message ```next_node must be a Node object```

	- Instantiation with ```data``` and ```next_node: def __init__(self, data, next_node=None):```

- And, write a class ```SinglyLinkedList``` that defines a singly linked list by:
