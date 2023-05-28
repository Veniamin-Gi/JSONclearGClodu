import sys
import json

def my_filtering_function(pair):
    wanted_keys = ['Id', 'Code']
    key, _ = pair
    if key in wanted_keys:
        return True
    else:
        return False

def load_JSON(file_name: str):
    with open(file_name, 'r') as file:
        return json.load(file)

def save_JSON(data):
    with open('newJSON.json', 'w') as file:
        json.dump(data, file)

# MAIN
def main(file_name: str):

    newList = []
    gradest = load_JSON(file_name)

    for grades in gradest:
        newList.append(dict(
            filter(my_filtering_function, grades.items())
            ))

    save_JSON(newList)

if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)




