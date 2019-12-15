import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    path = "./../../../titanik_hayir/output3/"
    for filename in os.listdir(path):
        print(filename)
        temp = filename.split('_')
        dst =str(int(temp[1])) + ".json"
        src = path + filename 
        dst = path + dst 
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
