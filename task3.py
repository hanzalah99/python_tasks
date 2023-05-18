
import os

def main():
    cmd = "lscpu"
    username="emumba"
    file_name="Summary.txt"
    file_path= "/home/emumba/Details/Summary.txt"
    directory = os.path.dirname(file_path)
    if os.path.exists(directory):
        print("Directory Already exists")

    else:
        
        os.mkdir(directory)
        print("Making Directory")

    os.system(f"{cmd} > {file_path}")   
       
if __name__ == "__main__":
    main()
