#!/usr/local/bin/python3

class Node:
	def __init__(self,data=None,next_node=None):
		self.data = data
		self.next_node = next_node

	def getData(self):
		return self.data

	def setData(self,data):
		 self.data = data

	def nextNode(self):
		return self.next_node


class LinkedList:
	size = 0
	def __init__(self,head = None):
		self.head = head

	def addNode(self,data):
		newNode = Node(data,self.head)
		self.head = newNode
		self.size +=1

		return True

	def prepend(self, data):
		"""
		Insert a new element at the beginning of the list.
		Takes O(1) time.
		"""
		self.head = Node(data=data, next_node=self.head)
		LinkedList.size += 1

	def dumpNode(self):
		curr = self.head

		while curr:
			print(curr.data)
			curr = curr.nextNode()

	def getSize(self):
		return LinkedList.size

	def append(self, data):
		"""
		Insert a new element at the end of the list.
		Takes O(n) time.
		"""
		if not self.head:
			self.head = Node(data=data)
			LinkedList.size += 1
			return
		curr = self.head
		while curr.nextNode():
			curr = curr.nextNode()
		curr.next_node = Node(data=data)
		LinkedList.size += 1

	def find(self, key):
		"""
		Search for the first element with `data` matching
		`key`. Return the element or `None` if not found.
		Takes O(n) time.
		"""
		curr = self.head
		while curr and curr.data != key:
			curr = curr.next_node
		return curr  # Will be None if not found

	def reverse(self):
		"""
		Reverse the list in-place.
		Takes O(n) time.
		"""
		curr = self.head
		prev_node = None
		next_node = None
		while curr:
			next_node = curr.next_node
			curr.next_node = prev_node
			prev_node = curr
			curr = next_node
		self.head = prev_node

		return self

myList = LinkedList()
myList.append(5)
myList.append(15)
myList.append(25)
myList.append(4)
myList.append(6)
myList.prepend(78)

print("Printing")
myList.dumpNode()
print("Size -",myList.getSize())
