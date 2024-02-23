stack = []
menu = """
Menu
================
0. [Exit]       
1. Add a plate  
2. Print plates 
3. Remove plates
Select [0-3]:
"""
option = input(menu)

def add_plate(size):
  if size <= 0:
    print("Error. Please enter a number greater than zero")
  elif not stack or stack[-1] >= size:
    stack.append(size)
    print("Success!")
  else:
    print(f"Cannot place a plate of size {size} on top of another plate of size {stack[-1]}.")

def print_plates():
  if not stack:
    print("There are no stacked plates.")
  else:
    for plate in reversed(stack):
      printed_plate = "#" * plate
      print(f"{printed_plate:^{max(stack)}}")
      #max(stack) is to find the correct length for center alignment

def remove_plates(num):
  if num <= 0:
    print("Error. Please enter a number greater than zero.")
  elif num <= len(stack):
    del stack[-num:]
    print("Success!")
  else:
    print(f"Cannot remove more than {len(stack)} plates. You chose {num}.")

while option != "0":
  match option:
    case "0":
      break
    case "1":
      print("\nAdd a plate")
      print("=" * 12)
      try:
        plate_size = int(input("Enter a plate size: "))
        add_plate(plate_size)
      except:
        print("Error. Invalid input.")
    case "2":
      print("\nPrint plates")
      print("=" * 12)
      print_plates()
    case "3":
      print("\nRemove plates")
      print("=" * 12)
      if len(stack) == 0:
        print("There's nothing to remove currently.")
      else:
        try:
          num_to_remove = int(input("How many plates to remove?: "))
          remove_plates(num_to_remove)
        except:
          print("Error. Invalid input.")
    case _:
      print("That's not a valid option!")
  option = input(menu)
  
    