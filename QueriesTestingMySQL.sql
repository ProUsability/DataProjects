#CREATE DATABASE test;

#CREATE TABLE testtable1;

#DROP TABLE testtable1;

#USE test;

#SELECT * FROM testtable1;

#INSERT INTO testtable1 SET participant=45, primaryBrowser='Firefox', browserVersion='31',operatingSystem='Windows 7';

#SELECT primaryBrowser, browserVersion, COUNT(*) FROM testtable1 GROUP BY primaryBrowser, browserVersion ORDER BY primaryBrowser, browserVersion;

#SELECT primaryBrowser, operatingSystem, COUNT(*) FROM testtable1 GROUP BY primaryBrowser, operatingSystem ORDER BY primaryBrowser, operatingSystem;

#SELECT SUM(primaryBrowser='Chrome') FROM testtable1;

#SELECT SUM(primaryBrowser='Firefox') FROM testtable1;

SELECT operatingSystem, CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome from testtable1 GROUP BY operatingSystem ORDER BY operatingSystem;