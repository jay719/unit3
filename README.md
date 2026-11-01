# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirement

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   
I've worked with Python lists before, so inserting, deleting, and searching weren't entirely new to me. However, I got a better understanding of how elements shift when inserting or removing values from different positions. I also learned more about how those operations affect performance, especially when working with larger lists.

2. What challenges did you encounter, and how did you overcome them?
   
The biggest thing I had to consider was handling invalid indexes without causing errors. I added a check to make sure the index was within the list before attempting to remove anything. I also tested inserting into an empty list and deleting from one to make sure those cases behaved as expected.

3. How do list operations impact performance in real-world applications?

Insertion and deletion can take O(n) time when elements need to shift, while adding or removing items at the end is generally faster. Searching also takes O(n) time in the worst case because each value may need to be checked. I demonstrated these operations with a game inventory, where items could be added, used, or searched for. While the difference might not matter much with a small inventory, I can see how it could become more important when managing thousands of items.

