# MAGIC METHODS : Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations 
#                 They allow developers to define or customize the behavior of objects

class Books:

  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self): #Defines what print(object) displays.
    return f"{self.title} by {self.author}"
  
  def __len__(self):  #Makes len() work on your object.
    return len(self.title)
  
b1 = Books("The Hobbit", "J.R.R Tolkien", 301)
b2 = Books("Harry Potter", "J.K. Rowling", 235)
b3 = Books("The Lion, The Witch, and the Wardrobe", "C.S. Lewis", 185)

print(len(b1))