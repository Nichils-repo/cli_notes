import sys 
from notes.notes import add_note, delete_note, search_notes
from notes.storage import load_notes

# sys.argv[0] is the shell
# sys.argv[1] 
# sys.argv[2] 
# sys.argv[3] is the second argument


def run():
    if len(sys.argv) <2 :
        print("Usage : python main.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print('''Error : "add" requires both <title> and <content>''')
            print('''add <title> <content>''')
            return
        title = sys.argv[2]
        content = sys.argv[3]
        add_note(title, content)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("""Error : "delete" requires <note_id>""")
            print("""Usage : python main.py delete <note_id>""")
            return
        try:
            note_id = int(sys.argv[2])
        except ValueError:
            print("""Error : <note_id> must be a number""")
            return
        delete_note(note_id)
    
    elif command == "list":
        notes = load_notes()
        if not notes:
            print("There are currently no notes")
            return
        else:
            for note in notes:
                print(f"ID : {note['id']}, Title : {note['title']} - {note['created_at']}")
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Search requires a keyword")
            print("Usage : python main.py search <keyword>")
            return 

        keyword = sys.argv[2]
        result = search_notes(keyword)

        if not result:
            print(f"No notes found containing {keyword}")
        else:
            print(f"found {len(result)} notes containing {keyword}")
            for note in result:
                print(f"ID: {note['id']}, Title: {note['title']}, \n Content: {note['content']}")
    
    else:
        print("Invalid command")
        print("Usage : python main.py <command>")
        print("Commands : add, delete, search")
        return



    