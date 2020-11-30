import datetime
segundos = int(input('Quantos segundos durou o evento? '))
tempo_total = datetime.timedelta(seconds=segundos)
print(tempo_total)
