print("""
========== Password Manager ============
[1] View
[2] Add
[3] Quit
========================================
""")

while True:
    user_inp = int(input("Option: "))

    if user_inp == 1:
        with open("data.txt", "r") as f:
            data = f.read()
        print(f"Your Password: {data}")

    if user_inp == 2:
        add = input("Enter Password: ")
        add = str(add)

        with open("data.txt", "w") as f:
            f.write(add)

        print("Password Saved!")

    if user_inp == 3:
        break    
