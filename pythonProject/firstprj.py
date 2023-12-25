from prettytable import PrettyTable
table = PrettyTable()
table.add_column("city",["kmm","hyd"])
table.add_column("pin",["190","191"])
table.align = 'r'
print(table)