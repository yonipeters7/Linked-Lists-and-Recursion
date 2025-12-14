from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    ll = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    print("=== Inserting Employee IDs ===")
    ll.insert_at_end(101)
    ll.insert_at_end(205)
    ll.insert_at_end(310)
    ll.insert_at_front(50)
    ll.insert_at_end(415)

    # TODO: 3) Display the list to verify insertion
    print("\nCurrent Employee ID List:")
    ll.display()

    # TODO: 4) Call recursive_sum and print the result
    total = ll.recursive_sum()
    print(f"\nSum of all Employee IDs: {total}")

    # TODO: 5) Call recursive_search with a target and print result
    search_id = 310
    found = ll.recursive_search(search_id)
    print(f"\nSearching for Employee ID {search_id}: {'Found' if found else 'Not Found'}")

    search_id = 999
    found = ll.recursive_search(search_id)
    print(f"Searching for Employee ID {search_id}: {'Found' if found else 'Not Found'}")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("\n=== Reversing the List ===")
    ll.recursive_reverse()
    print("Reversed Employee ID List:")
    ll.display()
