import json 

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# do not need try except for the saving 
#because,when the notes.json file is not there, it simply creates one
def save_notes(notes):

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent= 2)

# indent is to make the json more human readable, 2 is for spaces for each level of indent 
# otherwise the full json is printed in the same line

 


