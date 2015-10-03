class StatSerie(object):
    def __init__(self, serie):
        try:
            self.serie = [float(i) for i in serie]
        except TypeError:
            print("Error: no numeric variable in list")
        else:
            serie.sort()
            self.refresh()

    def __repr__(self):
        to_return = "; ".join(str(x) for x in self.serie)
        to_return += "\nétendue = {0}; mediane = {1}; q1 = {2}; q2 = {3}; moyenne = {4}"\
            .format(self.etendue, self.mediane, self.q1, self.q3, self.moyenne)
        return to_return

    def cal_etendue(self):
        self.etendue = max(self.serie) - min(self.serie)

    def cal_mediane(self):
        nbr_valeur = len(self.serie)
        if (nbr_valeur%2):
            self.mediane = self.serie[nbr_valeur//2]
        else:
            self.mediane = (self.serie[nbr_valeur//2] + \
                            self.serie[nbr_valeur//2 - 1])/2

    def cal_q1(self):
        q1_index = len(self.serie)//4
        self.q1 = self.serie[q1_index]

    def cal_q3(self):
        q3_index = len(self.serie)//4*3
        self.q3 = self.serie[q3_index]

    def cal_moyenne(self):
        self.moyenne = sum(self.serie)/len(self.serie)

    def refresh(self):
        self.cal_etendue()
        self.cal_mediane()
        self.cal_q1()
        self.cal_q3()
        self.cal_moyenne()

    def append(self, to_append):
        try:
            self.serie.append(float(to_append))
        except TypeError:
            print("error : no numeric variable")
        else:
            self.serie.sort()
            self.refresh()
            
    def save(self, save_file_path):
        if (type(save_file_path) != str):
            print("Bad argument please enter string")
        else:
            try:
                with open(save_file_path, 'w') as save_file :
                    save_file.write(str(self))
            except IOError:
                print("Error: save failed")
            else:
                print("Save successfully")
