class StatSerie(object):
    def __init__(self, serie):
        try:
            self._serie = [float(i) for i in serie]
        except ValueError:
            print("Error: no numeric variable in list")
        else:
            self._serie.sort()
            self.refresh()

    def __repr__(self):
        to_return = "; ".join(str(x) for x in self._serie)
        to_return += "\nétendue = {0}; mediane = {1}; q1 = {2}; q2 = {3}; moyenne = {4}"\
            .format(self._etendue, self._mediane, self._q1, self._q3, self._moyenne)
        return to_return

    def _get_etendue(self):
        return self._etendue

    def _get_mediane(self):
        return self._mediane

    def _get_q1(self):
        return self._q1

    def _get_q3(self):
        return self._q3

    def _get_moyenne(self):
        return self._moyenne

    etendue = property(_get_etendue)
    mediane = property(_get_mediane)
    q1 = property(_get_q1)
    q3 = property(_get_q3)
    moyenne = property(_get_moyenne)

    def cal_etendue(self):
        self._etendue = max(self._serie) - min(self._serie)

    def cal_mediane(self):
        nbr_valeur = len(self._serie)
        if (nbr_valeur%2):
            self._mediane = self._serie[nbr_valeur//2]
        else:
            self._mediane = (self._serie[nbr_valeur//2] + \
                            self._serie[nbr_valeur//2 - 1])/2

    def cal_q1(self):
        q1_index = len(self._serie)//4
        self._q1 = self._serie[q1_index]

    def cal_q3(self):
        q3_index = len(self._serie)//4*3
        self._q3 = self._serie[q3_index]

    def cal_moyenne(self):
        self._moyenne = sum(self._serie)/len(self._serie)

    def refresh(self):
        self.cal_etendue()
        self.cal_mediane()
        self.cal_q1()
        self.cal_q3()
        self.cal_moyenne()

    def append(self, to_append):
        try:
            if (type(to_append) == list) or (type(to_append) == tuple):
                for i in to_append :
                    self.append(float(i))
            else:
                self._serie.append(float(to_append))
        except ValueError:
            print("error : no numeric variable")
        else:
            self._serie.sort()
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
