FILEPATH =  "todo.txt"
def get_todos(file_path = FILEPATH):
    """
    Reads a text file and return a to-do items
    """
    with open(file_path, "r") as file:
        todos_local = file.readlines()
    return todos_local
#print(help(get_todos))

def write_todos(todos_arg, file_path = FILEPATH):
    """
    Write the to-do items list in the text file
    """    
    with open(file_path, "w") as file:
        file.writelines(todos_arg)
        
        #if you observe we didnt return any value for this function
        #this was because this functions doesnt need to return anything 
        #i.e its is only for the execution of a function

#print(__name__)
if __name__ == "__main__":
    print("hey josh")  
    print(get_todos())      



