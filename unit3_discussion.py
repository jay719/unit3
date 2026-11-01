"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Existing values at and after that index shift one position to the right
    lst.insert(index, value)

    # Inserting at the beginning or middle takes more work because values shift
    # Adding to the end is usually faster since no existing values need to shift



def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check if the index is valid before removing anything
    # This prevents an IndexError if the index doesn't exist
    if index < 0 or index >= len(lst):
        return None

    # Remove the value at the index and return it
    # Values after the deleted item shift one position to the left
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Search through the list one value at a time
    # This is a linear search because we check each index in order
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 if the value wasn't found
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.
    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    numbers = [10, 20, 30, 40]
    print(f"Original list: {numbers}")

    # Insert 5 at the beginning
    insert_at(numbers, 0, 5)
    print(f"After inserting 5 at the beginning: {numbers}")

    # Insert 25 in the middle
    insert_at(numbers, 3, 25)
    print(f"After inserting 25 in the middle: {numbers}")

    # Insert 50 at the end
    insert_at(numbers, len(numbers), 50)
    print(f"After inserting 50 at the end: {numbers}")
    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    # Use the updated list from the insertion tests
    print(f"Current list: {numbers}")

    # Remove the first value
    removed = delete_at(numbers, 0)
    print(f"Removed from beginning: {removed}")
    print(f"Updated list: {numbers}")

    # Remove a value from the middle
    removed = delete_at(numbers, 2)
    print(f"Removed from middle: {removed}")
    print(f"Updated list: {numbers}")

    # Remove the last value
    removed = delete_at(numbers, len(numbers) - 1)
    print(f"Removed from end: {removed}")
    print(f"Updated list: {numbers}")
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    print(f"Current list: {numbers}")

    # Search for a value that exists in the list
    result = search_value(numbers, 30)
    print(f"Searching for 30: Found at index {result}")

    # Search for a value that isn't in the list
    result = search_value(numbers, 100)
    print(f"Searching for 100: Index {result} (not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")



if __name__ == "__main__":
    main()