filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as f:
        content = f.read()
        print(content)
except Exception as e:
    print(f"Error reading file: {e}")
else:
    try:
        with open("modified_" + filename, 'w') as f:
            f.write(content.upper()) 
        print("Modified file saved as:", "modified_" + filename)
    except Exception as e:
        print(f"Error writing file: {e}")


