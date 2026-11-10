numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    callback = int(input("Choose an option (1-5): "))
    #minimum
    if callback == 1:
        crunch = numbers[0]
        for num in numbers:
            if num < crunch:
                crunch = num
            print(f"The minimum is: {crunch}")
    #maximum 
    elif callback == 2:
        crunch = 0
        for num in numbers:
            if num > crunch:
                    crunch = num
            print(f"The maximum is: {crunch}")
    #search
    elif callback == 3:
            search = int(input("Enter a number to search: "))
            target = search
            index = -1
            for i in range(len(numbers)):
                if numbers[i] == target:
                    index = i
                    break 
        
            if index != -1:
                print(f"Found {target} at index {index}")
            else:
                print(f"{search} not found")
    #sort
    elif callback == 4:
            def bubble_sort(numbers):
                swapped = True
                while swapped:
                    swapped = False
                    for i in range(len(numbers) - 1):
                        if numbers[i] > numbers[i + 1]:
                            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                            swapped = True
                return numbers
            sorted_numbers = bubble_sort(numbers)
            print(f"Sorted list: {sorted_numbers}")   
    #quit
    elif callback == 5:
            print("Thank you for using Number Cruncher!")
            break