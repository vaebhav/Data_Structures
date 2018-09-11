# Linked List

A Linked List is a data structure that consists of many mini-data structures called ‘Nodes.’ The Nodes link together to form a list.

# Big O Time Complexity Analysis

‘n’ = the amount of elements inside the Linked List.

Inserting to the back of the Linked List— We go through all n elements to find the tail and insert our new node. O(n)

Inserting to the front of the Linked List — We simply create the new node and set its nextNode to the head. No need to traverse the list. O(1)

Inserting to the end of the Linked List — We simply create the new node and set its nextNode to the head. No need to traverse the list. O(1)

Traversing — We go through all n elements once. O(n)

Deleting — Worst case scenario, the node we’re deleting is the last node, causing us to traverse through the entire list. O(n)

# References -

[a link](http://treasurytoday.com/2003/11/credit-risk-modelling-techniques)
