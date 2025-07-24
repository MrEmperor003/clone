"""
Task 1: Jos Food and Culture Festival Menu (Modified)
You're part of the planning team for the Jos Food and Culture Festival hosted by Blockfuse Labs Cohort III. A list of traditional Plateau meals was created for display on the second day of the event:
meals = ["Gwote", "Masa", "Tuwon Acha", "Fura da Nono", "Kunu", "Miyan Kuka"]

1.⁠ ⁠The event manager wants "Miyan Taushe" to be included right before the meal "Kunu", to reflect proper cultural order.
2. One of the vendors called to say that "Masa" will not be available, so it should be taken off the list.
3.⁠ ⁠Due to cold storage issues, "Fura da Nono" needs to be moved to the end of the list so it can be served last.
4.⁠ ⁠The program coordinator asks you to find out which meal is exactly at the center of the list now.
5. Arrange the Meals in alphabetical order
→ Modify the list as required and print the final list and the center meal.
"""

# Original list of meals
meals = ["Gwote", "Masa", "Tuwon Acha", "Fura da Nono", "Kunu", "Miyan Kuka"]

# 1. Insert "Miyan Taushe" before "Kunu"

meals.insert(4, "Miyan Taushe")
print(meals)

# 2. Remove "Masa"
meals.remove(meals[1])
print(meals)

# 3. Move "Fura da Nono" to the end
meals[2], meals[5] = meals[5], meals[2]
print(meals)

# 4. Find the center meal
middle_index = len(meals) // 2
center_meal = meals[middle_index]
print(meals)

# 5. Arrange meals in alphabetical order
meals.sort()


print("Final Meals List:", meals)
print("Center Meal:", center_meal)

