import pdb
from database import database
from Game2_remastered import game_2


class FileExplorer:
    def __init__(self):
        self.commands = {'read': self.read, 'cd': self.cd, 'ls': self.ls, 'run': self.run, 'help':self.help}
        self.files = { 'Folder':{'hi.txt':'Hello there'}, 'myDiary.db': database, 'riddle.exe':game_2}
        self.filenames = self.files.keys()
        self.current_files = self.files
        self.current_directory = []
        self.event = ''

    #commands go here
    #list files

    def ls(self,context):
        print('------- FILES -------')
        for file in self.current_files:
            print(file)
    #go into folder
    def cd(self,context):
        if context == '':
            if self.current_directory:
                self.current_directory.pop()
                self.get_files(self.current_directory)

        elif self.file_type(context) == 'folder':
            if context in self.current_files.keys():
                self.current_directory.append(context)
                self.current_files = self.current_files[context]
            else: print('The specified folder does not exist')
        else: print('You can only use this command on a folder!')

    #reads a text file
    def read(self,context):
        if self.file_type(context) == 'txt':
            text =self.current_files.get(context,False)
            if text:
                print('*******\n\n' + text + '\n\n*******')
                self.openfile = context
            else: print('Specified file does not exist')

            if context == 'entry5.txt' and text:
                self.event = 'end'

        else: print('File is not in txt format.')


    def help(self,context):
        print("")
        print("cd <Folder>: Change directory to specified folder. Type cd without context to move out of folder.")
        print("ls: Lists files in current directory.")
        print("run <file>: Runs an executable file or database")
        print("read <file>: Reads a text file.")
        print("")

    #reads a text file
    def run(self,context):
        if self.file_type(context) == 'db' or self.file_type(context) == 'exe':
            exe = self.current_files.get(context,False)
            if exe:
                exe(self)
            else: print('Specified file does not exist')

        else: print('File is not able to be run.')


    def hint(self,context):
        print(self.hints[0])
    ###############


    def file_type(self,filename):
        if filename:
            if len(filename.split('.')) > 1:
                extension = filename.split('.')[1]
            else: extension = 'folder'
            return extension
        else: return None


    def print_files(self):
        print('------- FILE EXPLORER -------')
        for file in self.filenames:
            print(file)


    def parse_text(self, text):
        terms = text.split()
        command = terms[0]
        if len(terms) >= 2:
            context = terms[1]
        else: context = ''

        if command in self.commands:
            self.commands[command](context)
        else: print('Command {} not recognized'.format(command))

        pass


    def get_files(self,directory):
        temp_dict = self.files
        for string in directory:
            temp_dict = temp_dict.get(string,False)
            if not temp_dict:
                print('Get file error, please troubleshoot')
        self.current_files = temp_dict


    def directory_string(self, directory):
        output_string = '\\'
        for item in directory:
            output_string += item
            output_string += '\\'
        return output_string[:-1]

    def add_file(self, filename, file):
        self.files[filename] = file
