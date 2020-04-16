import cx_Oracle
username = 'DBLAB'
password = 'system'
database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

#QUERY 1
print("Вивести країни та загальну кількість зареєстрованих у них випадків Covid-19.\n")
query1 = """
SELECT
    TotalCases.country,
    TotalCases.total_cases
 FROM
    TotalCases
ORDER BY
    total_cases DESC
"""
cursor.execute(query1)

for row in cursor:
    print(row)

#QUERY 2
print("\nВивести країну та % зареєстрованих у ній випадків відносно усіх зареєстрованих у світі.\n")
query2 = """
SELECT
    TotalCases.country,
	round((TotalCases.total_cases + 0.0) * 100 / t.total, 2) as persent
FROM
    TotalCases,
    (SELECT
        SUM(TotalCases.total_cases) AS total
     FROM
        TotalCases
    ) t
"""
cursor.execute(query2)

for row in cursor:
    print(row)

#QUERY 3
print("\nДинаміка залежності кількості летальних випадків від загальної кількості зареєстрованих.\n")
query3 = """
 SELECT
    TotalCases.total_cases,
    TotalDeaths.total_deaths
 FROM
    TotalCases INNER JOIN TotalDeaths ON TotalCases.country = TotalDeaths.country
ORDER BY
    total_cases DESC
"""
cursor.execute(query3)

for row in cursor:
    print(row)

cursor.close()
connection.close()
