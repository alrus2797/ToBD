import csv
class Data:
    def __init__(self, _file):
        if _file.mode != 'r':
            return           

        self.data = {}
        self.reader = csv.reader(_file, quoting=csv.QUOTE_ALL)
        self.relations = []
        for row in self.reader:
            # Headers
            if self.reader.line_num == 1:
                for header in row[1:]:
                    self.data[header.strip('"')] = {}
            # Data
            else:
                relation = row[0]
                self.relations.append(relation)
                for idx, name in enumerate(self.data.keys()):
                    if row[idx + 1] == '':
                        continue
                    self.data[name][relation] = float(row[idx + 1])
            print(row)
    
    def distances(self, p1, p2):
        return Data.Distances(self, p1, p2)

    
    class Distances:
        def __init__(self, parent, p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.parent = parent
            self.data1 = parent.data[p1]
            self.data2 = parent.data[p2]
            print(self.data1, self.data2)
            self.iterator = map(self.data1, self.data2)
            self.d1 = 0
            self.d2 = 0

        def points_are_valid(self):
            return self.d1 != None and self.d2 != None
        
        def unit_manhattan(self, r = None):
            return abs(self.d1 - self.d2)

        def unit_euclidean(self, r = None):
            return (self.d1 - self.d2) ** 2

        def unit_minkowski(self, r):
            # print("udata:",(self.d1 - self.d2) ** r)
            return abs(self.d1 - self.d2) ** r

        def calculate(self, unit_function, res_function = None, r = 1):
            res = 0
            for relation in self.parent.relations:
                # print("fdata:",self.d1, self.d2)
                self.d1, self.d2 = self.data1.get(relation), self.data2.get(relation)
                if self.points_are_valid():
                    res += unit_function(r)
            return res_function(res, r) if res_function else res

        def manhatan(self):
            return self.calculate(self.unit_manhattan)
        def euclidean(self):
            return self.calculate(self.unit_euclidean, pow, 0.5)
        def minkowski(self, r):
            return self.calculate(self.unit_minkowski, lambda v,x: v**(1/x), r)


a = Data(open('lab1.csv'))