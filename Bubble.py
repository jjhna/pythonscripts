#Bubble Sort for Python
# From the website: https://learn.microsoft.com/en-us/windows/python/scripting
# cd D:\PythonProject\pythonscripts
# python .\Bubble.py

#From the Python Institute -   3.5.1.3 Sorting simple lists - the bubble sort algorithm 

my_list = []
swapped = True # Note here that we need to manually trigger the while loop before it starts
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element, one - by - one: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        print("current iteration i: ", i)
        print("current status of my_list: ", my_list)
        print("current my_list[i]: ", my_list[i], " and the other amount my_list[i + 1]: ", my_list[i+1])
        if my_list[i] > my_list[i + 1]:
            swapped = True
            # This is swapping out numbers from the right side to the left side
            # the tuple is unpacking on the left side, while the right side creates a tuple with the values from the list
            # this allows us to swap both values without the need of a temporary variable
            # So say the iteration is on i = 1 and my_list[1] = 2 (and my_list[2] = 1), so...
            # so on the right side, the tuple: (1, 2)
            # will now be my_list[1] = 1 and my_list[2] = 2
            # or my_list[i] = my_list[i + 1] and my_list[i + 1] = my_list[i]
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

            # Also note the lack of a temporary variable unlike Java which would require it

print("\nSorted:")
print("Final my_list sorted list: ", my_list)
