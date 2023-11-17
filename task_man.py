# Chaque instance de la classe taskmanager sera une to do list
# self.loop == on reste dans la boucle
# self.tasks = dico {"tâche" : bool == la tâche est faite}
# init : on rentre direct dans la boucle
# display : on affiche la to do list
# order : suit l'instruction
# Pour l'instruction, la syntaxe demandée est :
# symbole + espace + description ou id

class taskmanager:
    def __init__(self):
        self.loop = True
        self.tasks = {}

    def display(self):
        count = 1
        for task in self.tasks:
            done = ' '
            if self.tasks[task]:
                done = 'x'
            line = str(count) + ' [' + done + '] ' + task
            print(line)
            count += 1
        if count == 1:  # pas de tâche
            print("Bonjour, vous êtes dans le task manager.")
            print("tapez :")
            print("q pour quitter le task manager")
            print("+ task pour ajouter task")
            print("- task pour retirer task")
            print("x task pour marquer task accomplie")
            print("o task pour marquer task à faire")
        print('\n')

    def order(self):
        if self.instruction == 'q':  # exit
            self.loop = False
        if self.instruction[0] == 'o':  # to do
            self.tasks[self.instruction[2:]] = False
        if self.instruction[0] == 'x':  # done
            self.tasks[self.instruction[2:]] = True
        if self.instruction[0] == '-':  # remove
            self.tasks.pop(self.instruction[2:])
        if self.instruction[0] == '+':  # add
            self.tasks[self.instruction[2:]] = False

    def start(self):
        self.loop = True
        while self.loop:
            self.display()
            self.instruction = input()
            self.order()
        print('Bye, see you soon')

tm1 = taskmanager()
tm1.start()