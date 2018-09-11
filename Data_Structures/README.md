# Linked List

A Linked List is a data structure that consists of many mini-data structures called ‘Nodes.’ The Nodes link together to form a list.

# Big O Time Complexity Analysis

‘n’ = the amount of elements inside the Linked List.

Inserting to the back of the Linked List— We go through all n elements to find the tail and insert our new node. O(n)

Inserting to the front of the Linked List — We simply create the new node and set its nextNode to the head. No need to traverse the list. O(1)

Inserting to the end of the Linked List — We simply create the new node and set its nextNode to the head. No need to traverse the list. O(1)

Traversing — We go through all n elements once. O(n)

Deleting — Worst case scenario, the node we’re deleting is the last node, causing us to traverse through the entire list. O(n)

# Source
The dataset is available at the Center for Machine Learning and Intelligent Systems, Bren School of Information and Computer Science, University of California, Irvine: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

Extract from the dataset information section : "This research aimed at the case of customers' default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients."

# References -

[a link](http://treasurytoday.com/2003/11/credit-risk-modelling-techniques)
