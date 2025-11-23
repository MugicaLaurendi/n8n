import random
import datetime
import csv

# Génération comptes (5000)
with open("accounts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id","account_code", "account_name", "account_type"])
    types = ["Actif", "Passif", "Produit", "Charge"]

    for i in range(5000):
        id = i
        code = f"ACCT{i:04d}"
        name = f"Compte numéro {i}"
        acc_type = random.choice(types)
        writer.writerow([id, code, name, acc_type])

# Génération écritures comptables (5000)
with open("journal_entries.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["entry_date", "account_id", "description", "debit", "credit"])

    for i in range(5000):
        date = datetime.date(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 365))
        acc_id = random.randint(1, 5000)
        desc = f"Ecriture automatique {i}"

        # Simuler des lignes équilibrées
        if random.random() < 0.5:
            debit = round(random.uniform(10, 1000), 2)
            credit = 0
        else:
            debit = 0
            credit = round(random.uniform(10, 1000), 2)

        writer.writerow([date, acc_id, desc, debit, credit])
