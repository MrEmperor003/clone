"""
    You're cleaning up your phone's contact list and organizing your close friends from Jos.
    Your friends list is: friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
    
    1. You made a new close friend "Kemi" and want to add her between "John" and "Mary".
    2. "Daniel" moved to Lagos and you don't talk anymore, so remove him from your close friends list.
    3. "Aisha" got married and now goes by "Aisha_M". Update her name in the list.
    4. You want to add your cousin "Zainab" at the end of the list.
    5. Create a new list with only the first 3 friends from your updated list and display it.
    6. Find out what position "Paul" is in your final friends list (remember: position counting starts from 1 for humans!).
    7. arrange your contacts in Descending Alphabetical Order using.
"""
# task 5	
# Initial friends list
friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]

# 1. Add "Kemi" between "John" and "Mary"

friends.insert(3, "Kemi")
print(friends)
# 2. Remove "Daniel"
friends.remove(friends[1])
print(friends)
# 3. Update "Aisha" to "Aisha_M"

friends[0] = "Aisha_M"
print(friends)

# 4. Add "Zainab" at the end
friends.append("Zainab")
print(friends)
# 5. New list with only the first 3 friends
close_three = friends[:3]
print("First 3 close friends:", close_three)

# 6. Find position of "Paul" (starting from 1)
paul_position = friends.index("Paul") + 1
print("Paul's position in the list:", paul_position)

# 7. Arrange (sort) the final friends list alphabetically
friends.sort()
print("Alphabetically sorted friends list:", friends)

