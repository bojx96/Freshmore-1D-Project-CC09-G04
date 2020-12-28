import diary
from battleship import battleship
from Game3_remastered import game_3
def database(explorer):
    #{key: {filename: file}}
    entries = {'hello':{'hello.txt':'hi'}, '47':{'47_folder':{'entry1.txt':diary.entry1, 'battleship.exe':battleship}},'code':{'Code_folder':{'entry2.txt':diary.entry2, 'entry3.txt':diary.entry3,'sample_code.txt':diary.help,'riddle2.exe':game_3}},'time':{'Time_folder':{'entry4.txt':diary.entry4,'entry5.txt':diary.entry5}}}
    print("""

              ___  _
  __ _  __ __/ _ \(_)__ _______ __
 /  ' \/ // / // / / _ `/ __/ // /
/_/_/_/\_, /____/_/\_,_/_/  \_, /
      /___/                /___/


 """)
    while True:
        search = input("Search (type quit to escape): ").lower().strip()
        if search.lower().strip() == 'quit' or search.lower().strip() == 'q' :
            break
        value = entries.get(search,False)
        if value:
            for key, value in value.items():
                print(key + " has been added.")
                explorer.files[key] = value


        else: print('Entry not found.')
