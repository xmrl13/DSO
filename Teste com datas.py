import datetime
import datetimerange

entrada1 = datetime.datetime(2020, 1, 1)
saida1 = datetime.datetime(2021, 1, 1)
entrada2 = datetime.datetime(2020, 5, 5)
saida2 = datetime.datetime(2021, 6, 1)

intervalo1 = datetimerange.DateTimeRange(entrada1, saida1)
intervalo2 = datetimerange.DateTimeRange(entrada2, saida2)

print(intervalo1.is_intersection(intervalo2))