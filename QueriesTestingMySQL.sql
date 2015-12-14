#CREATE DATABASE test;

#CREATE TABLE testtable1;

#DROP TABLE testtable1;

#USE test;

#SELECT * FROM testtable1;

#INSERT INTO testtable1 SET participant=45, primaryBrowser='Firefox', browserVersion='31',operatingSystem='Windows 7';

#SELECT primaryBrowser, browserVersion, COUNT(*) from testtable1 GROUP BY primaryBrowser, browserVersion ORDER BY primaryBrowser, browserVersion;

SELECT primaryBrowser, operatingSystem, COUNT(*) from testtable1 GROUP BY primaryBrowser, operatingSystem ORDER BY primaryBrowser, operatingSystem;