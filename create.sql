CREATE TABLE TotalCases (
    country VARCHAR(30) NOT NULL PRIMARY KEY,
    total_cases INT NOT NULL REFERENCES Rank (total_cases),
	new_cases INT NOT NULL
    );

CREATE TABLE TotalDeath (
    country VARCHAR(30) NOT NULL PRIMARY KEY,
    total_deaths INT NOT NULL,
	new_deaths INT NOT NULL
    );
	
CREATE TABLE Rank (
    total_cases INT NOT NULL PRIMARY KEY,
	rank INT NOT NULL
    );
