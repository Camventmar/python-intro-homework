numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# --- Find Minimum ---
def find_min(numbers):
    crunch = numbers[0]
    for num in numbers:
        if num < crunch:
            crunch = num
    return crunch
# --- Find maximum ---
def find_max(numbers):
    crunch = numbers[0]
    for num in numbers:
        if num > crunch:
            crunch = num
    return crunch
            
    #search
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1 
   
    #sort
def bubble_sort(numbers):
    sorted_list = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_list) - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                swapped = True
    return sorted_list

def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return input("Choose an option (1-5): ")

if __name__ == "__main__":
    while True:
        choice = show_menu()

        if choice == "1":
            minimum = find_min(numbers)
            print(f"The minimum is: {minimum}")

        elif choice == "2":
            maximum = find_max(numbers)
            print(f"The maximum is: {maximum}")

        elif choice == "3":
            target = int(input("Enter a number to search: "))
            index = search(numbers, target)
            if index != -1:
                print(f"Found at index {index}")
            else:
                print("Not found")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print(f"Sorted list: {sorted_numbers}")

        elif choice == "5":
            print("Thank you for using Number Cruncher!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")