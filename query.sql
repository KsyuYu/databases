---QUERY 1
SELECT
    TotalCases.country,
    TotalCases.total_cases
 FROM
    TotalCases
ORDER BY
    total_cases DESC;

---QUERY 2	
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
GROUP BY
    TotalCases.country,
    t.total;
 
 ---QUERY 3
 SELECT
    TotalCases.total_cases,
    TotalDeaths.total_deaths
 FROM
    TotalCases INNER JOIN TotalDeaths ON TotalCases.country = TotalDeaths.country
ORDER BY
    total_cases DESC;
