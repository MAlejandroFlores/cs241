
numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

numbers.insert(0,5)
print(numbers)

print("Removing item 2348 from list...")
print(numbers.index(2348))
numbers.remove(2348)
print(numbers)
print("Adding new list")
numbers.extend([1,2,3,4,5]) 
print(numbers)
print("Sorting list...")
numbers.sort()
print(numbers)
numbers.sort(reverse= True)
print("Sorting reverse list...")
print(numbers)
print("Counting how mamy 12s in the list...")
print(numbers.count(12))
print("Finding the index of number 96...")
print(numbers.index(96))
print("Spliting the list in halves")
print("First half: ")
print(numbers[:(len(numbers)//2)])
print("Second half: ")
print(numbers[(len(numbers)//2):])
print("Printing every other element...")
print(numbers[::2])
print("Printing last 5 items...")
print(numbers[-1:-6:-1])