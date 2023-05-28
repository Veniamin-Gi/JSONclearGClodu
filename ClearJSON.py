import sys
import json

def my_filtering_function(pair):
    wanted_keys = ['Id', 'Code']
    key, value = pair
    if key in wanted_keys:
        return True  
    else:
        return False  
 
def loadJSON():
    with open('YourJSON.json', 'r') as file:
        return json.load(file) 

def SaveJSON(data):
    with open('newJSON.json', 'w') as file:
        json.dump(data, file)  

# MAIN
def main():
    
    newList = []
    gradest = loadJSON()
 
    for grades in gradest: 
        newList.append(dict(filter(my_filtering_function, grades.items())))
 
    SaveJSON(newList) 

if __name__ == "__main__":
    main()





