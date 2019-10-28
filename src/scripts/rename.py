import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    for filename in os.listdir("./../data/output/"):
        temp = filename.split('_')
        dst =str(int(temp[2])) + ".json"
        src ='./../data/output/'+ filename 
        dst ='./../data/output/'+ dst 
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
