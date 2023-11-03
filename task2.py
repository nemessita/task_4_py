with open("New Text Document.txt", "r") as f:
    lines = f.readlines()

if lines:
    first_element = lines[0]
    last_element = lines[-1]
    print("1-ci element:", first_element)
    print("Sonuncu element:", last_element)
else:
    print("Fayl boşdur.")