from fileexplorer import FileExplorer
from prologue import prologue_start
from game_3 import game_3
from end import end_game

class StateMachine:
    def __init__(self, explorer):
        self.explorer = explorer
        self.currentState = Prologue(explorer)
        self.currentState.run()
    # Template method:
    def runMachine(self, i):
        while True:
            self.currentState = self.currentState.next('')
            self.currentState.run()


class State:
    def __init__(self, explorer):
        self.explorer = explorer

class SampleState:
    def run(self):
        #run a function
        pass

    def next(self,input):
        #transition to next stage rules
        return None

class Prologue(State):
    def run(self):
        prologue_start()
    def next(self,input):
        #transition to next stage rules
        return FileMode(self.explorer)

class FileMode(State):
    def run(self):
        c = self.explorer
        c.openfile = ''
        current_command = input('C:\Jerry\Documents' + c.directory_string(c.current_directory)+ '>' )
        c.parse_text(current_command)
    def next(self, input):
        #transition to next stage rules
        c = self.explorer

        if c.event == 'end':
            return end(self.explorer)

        return FileMode(self.explorer)


class end(State):
    def run(self):
        end_game()

    def next(self,input):
        #transition to next stage rules
        return FileMode(self.explorer)
