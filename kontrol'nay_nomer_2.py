import csv

class Robber(object):

    def __init__(self, name,  product_name, count):
        self.name = name
        self.product_name = product_name
        self.count = count

    def get_dict_from_robber(self):
        return {
            'name': self.name,
            'product_name': self.product_name,
            'count': self.count
        }

    def scrounge_smthg(self, product_name, count):
        return product_name, count

class RobbersData:
    def __init__(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns

    def add_robber(self, name_robber):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow(name_robber.get_dict_from_robber())

    def get_list_of_robbers(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]


data_obj = RobbersData(
    'file_1.csv', ['name',  'product_name', 'count'])

robber1 = Robber('max', 'alchol', 15)
robber2 = Robber('jon', 'pencil', 7)
robber3 = Robber('viktor', 'computer', 2)


data_obj.add_robber(robber1)
data_obj.add_robber(robber2)
data_obj.add_robber(robber3)

print(data_obj.get_list_of_robbers())