import csv
from decimal import Decimal


csvfile = "data/temps_small.csv"

with open(csvfile) as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

# refaceți funcția get_average_temp()
# pentru a folosi csv.reader()
# (în loc de a face split manual)

def get_average_temp(file):
    total = Decimal(0)
    count = 0

    with open(file, "r", encoding = 'utf-8') as f:
      reader = csv.reader(f)
      for hour, temp in reader:
           temp = Decimal(temp)

           total += temp
           count += 1

    return total / count

print(get_average_temp("data/temperatures.csv"))

# task: parsăm temperaturile,
#       scriem raportul într-un csv nou
from d4_vineri_2_working_with_data_part_1 import get_hourly_averages

averages = get_hourly_averages("data/temperatures.csv")

with open("hourly_averages.csv", "w") as fout:
    writer = csv.writer(fout)

    # varianta 1: scriem explicit linie cu linie
    #for item in averages:
    #    writer.writerow(item)

    # varianta 2: scriem toată colecția
    writer.writerows(averages)
