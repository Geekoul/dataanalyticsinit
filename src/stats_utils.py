import csv

def calculer_statistiques(fichier_csv):
   
  ventes = []
  with open(fichier_csv, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      ventes.append(float(row["ventes"]))

  total = sum(ventes)
  moyenne = total / len(ventes) if ventes else 0
  return total, moyenne

if __name__ == "__main__":
  fichier = "../data/sales.csv"
  total, moyenne = calculer_statistiques(fichier)
  print(f"Total des ventes : {total}")
  print(f"Moyenne des ventes : {moyenne:.2f}")
