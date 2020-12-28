from fileexplorer import FileExplorer
import states

c = FileExplorer()
machine = states.StateMachine(c)

machine.runMachine('')
