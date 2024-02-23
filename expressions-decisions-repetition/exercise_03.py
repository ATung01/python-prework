name = input("What's your name?: ")
genre = input("What's your favorite music genre?: ")
rating = int(input("Favorite genre rating?: "))
input_str= input("Do you like other genres?: yes / no ").strip().lower()

print(f"Name: {name}")
print(f"Genre: {genre}")
print(f"Rating: {rating}")
if input_str == "yes":
    other_genre = True
    print(f"Other Genres?: {other_genre}")
elif input_str == "no":
    other_genre = False
    print(f"Other Genres?: {other_genre}")
else:
    print("Invalid input. Please enter 'yes' or 'no' for your other genres. ")
# 1. Run this file.
# Collect the user's (your) name.

# 2. Collect the user's favorite music genre.

# 3. Collect the user's favorite genre rating, 0-100.
# (No need to validate, but be sure to enter a valid integer.)

# 4. Ask the user if they enjoy other genres.
# The variable should be a boolean.
# You can either convert the `input` function string to a bool(input("prompt"))
# using the boolean literal "True" or "False"
# or compare strings: yes/no, y/n, etc.

# 5. Move all `input` operations to the top of the file.
# Collect the four questions.
# Print at the end.
