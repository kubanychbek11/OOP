data = ("O", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)


operators = {}
c = 0
while len(operators) != len(designations):
    operators[designations[c]] = {codes[c]}
    c += 1

operators.pop('Katel')
del operators['Fonex']

operators['Megacom'].add('0999')
operators['O'].add('0700')
operators['Beeline'].add('0222')

for key, value in operators.items():
    print(f'{key} - {value}')

