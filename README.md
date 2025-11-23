Pour generer les données au format .csv :

python3 data_generator.py

Pour entrer les donnéées .csv dans la DB :

psql -h localhost -p 5432 -U admin -d db \
  -c "\copy accounts FROM 'accounts.csv' CSV HEADER"

psql -h localhost -p 5432 -U admin -d db \
  -c "\copy journal_entries FROM 'journal_entries.csv' CSV HEADER"

