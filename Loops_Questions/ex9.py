# List Uniqueness Checker
#  Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)

    # explanation
    # unique_item is an empty set to track unique items we've seen so far.
    # A set automatically removes duplicates and has fast lookup.
  # in iteration 1 unique_items = {}, in iteraion 4 item = apple again, in unique items {"apple", "banana", "orange",} ✅ Already in set → print "Duplicate: apple" and break
