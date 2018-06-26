with open("inventory.txt", mode="w") as inventory:
    inventory.write("blender, 10")
    inventory.write("toaster, 20")

    # inventory.seek(0)
    # chars = inventory.read(10)
    # print(chars)