file_name = "files_exception_handling.txt"
try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("EXCEPTION ====== The file was not found.")
    print("EXCEPTION ====== Trying with uppercase filename", file_name.upper())
    try:
        with open(file_name.upper(), "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("EXCEPTION ====== The file was not found with uppercase name either.")
        print("EXCEPTION ====== Now creating file with the given file name.", file_name)
        try:
            with open(f"src/files/{file_name}", "w") as file:
                file.write("This is a newly created file.")
                print("File created successfully.")
        except Exception as e:
            print("EXCEPTION ====== An error occurred while creating the file:", str(e))
finally:
    print("FINALLY ====== Executed cleanup")