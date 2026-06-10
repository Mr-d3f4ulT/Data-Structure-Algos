#if __name__==__main__ : (this script can be imported OR run standalone)
#                        Functions and classed in this module can be reused
#                        without the main block of code executing

# if __name__ == "__main__": — Notes

# In Python, every file automatically gets a special built-in variable called __name__. The value of this variable depends on how the file is being used. If the file is executed directly using the Python interpreter, Python sets __name__ to "__main__". However, if the file is imported into another Python file as a module, Python sets __name__ to the name of that module (usually the filename without the .py extension).

# The statement if __name__ == "__main__": is used to check whether the current file is being run directly or imported. Code written inside this block executes only when the file is run directly and does not execute when the file is imported. This helps prevent test code, debugging code, or program entry-point code from running unintentionally when the module is used by another program.

# Syntax
# if __name__ == "__main__":
#     # code to execute only when run directly
# Example
# def greet():
#     print("Hello!")

# if __name__ == "__main__":
#     greet()
# Running python app.py → Output: Hello!
# Importing app in another file → No output
# Why It Is Used
# To separate reusable functions/classes from executable code.
# To prevent test code from running during imports.
# To define the main entry point of a program.
# To make modules reusable in larger projects.