import csv


class Nessus(object):

    def __init__(self, unknown):
        self.unknown = unknown
        self.hosts = list()

    def run(self): 
        with open('ipaddr.txt', 'r') as read_obj:
            #csv_dict_reader = DictReader(read_obj)
            csv_reader = csv.reader(read_obj, delimiter=',')
            line_count = 0
            # iterate over each line as a ordered dictionary
            for row in csv_reader:
                if line_count == 0:
            # row variable is a dictionary that represents a row in csv
                    print(row)
                else:
                    print(row)
                    try:
                        self.hosts.append((
                        row[0],
                        row[1]
                        ))
                    except AttributeError:
                        self.hosts.append((
                        row[0],
                        self.unknown
                        ))
                line_count+=1
        for elem in self.hosts:
            print(elem)
