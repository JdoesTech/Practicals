filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as f:
        content = f.read()
        print(content + "\n")
except Exception as e:
    print(f"Error reading file: {e}")
else:
    try:
        with open("modified_" + filename, 'r+') as f:
            f.write(content.upper()) 
            f.seek(0)
            print(f.read())
        print("\n Modified file saved as:", "modified_" + filename)
    except Exception as e:
        print(f"Error writing file: {e}")


