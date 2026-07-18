from notes.storage import save_notes, load_notes
from datetime import datetime 

def add_note(title, content):
    notes = load_notes()
    if not notes:
        new_id = 1
    else :
        new_id = max(note["id"]for note in notes) + 1
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    new_note = {
        "id" : new_id,
        "title" : title,
        "content" : content,
        "created_at" : created_at
    }

    notes.append(new_note)
    save_notes(notes)
    print(f"Note '{title}' added successfully!")
    return new_note

def delete_note(note_id):
    notes = load_notes()

    #check if this note is actually in the list
    if note_id not in [note["id"] for note in notes]:
        print(f"Note with id {note_id} not found!") 
        return False
    
    #creates a new list (notes) of the same name to update using list comprehension
    #take each note, keep them only if their id is not note_id.
    notes = [note for note in notes if note["id"]!= note_id] 
    
    save_notes(notes)
    print(f"Note with id {note_id} deleted successfully!")
    return True


def search_notes(keyword):
    notes = load_notes()

    results = []
    for note in notes:
        if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower():
            #or even results = [note for note in notes if keyword.lower() in note['title'] or keyword.lower() in note['content']]
            results.append(note)
    return results
