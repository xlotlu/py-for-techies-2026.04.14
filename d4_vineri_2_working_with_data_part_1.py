# calculați media temperaturilor
# din fișierul temperatures.csv

from decimal import Decimal


# 0. inițializăm două variabile:
#    - în una adunăm suma
#    - în altă numărăm nr. de linii

# 1. deschidem fișierul

# 2. citim linie cu linie (iterăm în fișier)

# 3. extragem temperatura
#    temp = line.removesuffix("\n").split(",")[1]
#    temp = Decimal(temp)

# 4. adunăm temperatura la suma totală
#    și incrementăm nr. de linii

# 5. am ieșit din for

# 6. împărțim, returnăm media


def get_average_temp(file):
    total = Decimal(0)
    count = 0

    with open(file, "r", encoding = 'utf-8') as f:
      for line in f:
           temp = line.removesuffix("\n").split(",")[1]
           temp = Decimal(temp)

           total += temp
           count += 1

    return total / count

#print(get_average_temp("data/temperatures.csv"))


# scrieți o funcție
# ce returnează o listă de tuple de forma
# (oră, medie_orară)

def get_hourly_averages(file):
    averages = []

    total = Decimal(0)
    count = 0

    with open(file, "r", encoding = 'utf-8') as f:
      
        current_sum = Decimal(0)
        current_count = 0

        old_hour = None

        for line in f:
            timestamp, temp = line.removesuffix("\n").split(",")
            hour = int(timestamp.split(":")[0])
            # dacă am fi vrut să agregăm după minut:
            #minute = timestamp.rsplit(":", 1)[0]

            temp = Decimal(temp)

            # detectăm dacă s-a schimbat ora
            # !!! dar nu și dacă tocmai am intrat în fișier
            if hour != old_hour and old_hour is not None:
                # calculăm media pentru ora care a trecut!
                avg = current_sum / current_count
                # acesta este average-ul orei vechi!
                averages.append(
                    (old_hour, avg)
                )

                # resetăm
                current_sum = Decimal(0)
                current_count = 0

            # acumulăm valorile
            current_sum += temp
            current_count += 1

            old_hour = hour

        # atenție! am ieșit din for,
        # deci avem un current_sum / current_count
        # pentru ultima oră din setul de date
        averages.append(
            (old_hour, current_sum / current_count)
        )

    return averages

#for hour, avg in get_hourly_averages("data/temperatures.csv"):
#    print(hour, avg)
