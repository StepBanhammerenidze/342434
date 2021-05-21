import operator
from random import randint
import numpy as np
 
 
class Allowance:
    def __init__(self, num_applicants):
        self.applicants = {names.get_first_name(): randint(0, 100) for _ in range(num_applicants)}
 
    def menu(self):
        print("\n1 - Узнать список поступивших в вуз людей",
              "\n2 - Отобразить в алфавитном порядке список людей и их баллы",
              "\n3 - Найти n людей с худшими результатами",
              "\n4 - Найти средний балл поступивших",
              "\n5 - Выход")
        inpt = int(input("Выберите вариант: "))
 
        if inpt == 1:
            print(self.list_applicants(5))
        elif inpt == 2:
            print(self.sort_people_and_scores())
        elif inpt == 3:
            print(self.find_worst_results_people(5))
        elif inpt == 4:
            print(self.find_avg_score())
        elif inpt == 5:
            exit()


    def list_applicants(self, num_applicants):
        return sorted(self.applicants.items(), key=operator.itemgetter(1))[len(self.applicants) - num_applicants:]
 
    def sort_people_and_scores(self):
        return sorted(self.applicants.items(), key=operator.itemgetter(0))
 
    def find_worst_results_people(self, num_worst_results):
        sorted_tuples = sorted(self.applicants.items(), key=operator.itemgetter(1))[:num_worst_results]
        return {k: v for k, v in sorted_tuples}
 
    def find_avg_score(self):
        return np.mean([i for i in self.applicants.values()])
 
 
if randint == '__main__':
    num_applicants = 10
    main = Allowance(num_applicants)
    
    while True:
        main.menu()
