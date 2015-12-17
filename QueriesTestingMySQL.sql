#CREATE DATABASE test;

#USE test;

#DROP TABLE IF EXISTS testtable1;

#CREATE TABLE testtable1;

SELECT * FROM testtable1;

#INSERT INTO testtable1 SET participant=45, primaryBrowser='Firefox', browserVersion='31',operatingSystem='Windows 7';

#SELECT primaryBrowser, browserVersion, COUNT(*) FROM testtable1 GROUP BY primaryBrowser, browserVersion ORDER BY primaryBrowser, browserVersion;

#SELECT primaryBrowser, operatingSystem, COUNT(*) FROM testtable1 GROUP BY primaryBrowser, operatingSystem ORDER BY primaryBrowser, operatingSystem;

#SELECT SUM(primaryBrowser='Chrome') FROM testtable1;

#SELECT SUM(primaryBrowser='Firefox') FROM testtable1;

#SELECT operatingSystem, CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome from testtable1 GROUP BY operatingSystem ORDER BY operatingSystem;

#SELECT AVG(secondsTOT) FROM testtable1 WHERE primaryBrowser='Firefox';

#SELECT AVG(secondsTOT) FROM testtable1 WHERE primaryBrowser='Chrome';

#I shouldn't be doing this manually. There's got to be a way to automate this...
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, youtubeFrequency FROM testtable1 GROUP BY youtubeFrequency ORDER BY FIND_IN_SET(youtubeFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, netflixFrequency FROM testtable1 GROUP BY netflixFrequency ORDER BY FIND_IN_SET(netflixFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, vimeoFrequency FROM testtable1 GROUP BY vimeoFrequency ORDER BY FIND_IN_SET(vimeoFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, funnyOrDieFrequency FROM testtable1 GROUP BY funnyOrDieFrequency ORDER BY FIND_IN_SET(funnyOrDieFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, facebookFrequency FROM testtable1 GROUP BY facebookFrequency ORDER BY FIND_IN_SET(facebookFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, yahooFrequency FROM testtable1 GROUP BY yahooFrequency ORDER BY FIND_IN_SET(yahooFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, liveleakFrequency FROM testtable1 GROUP BY liveleakFrequency ORDER BY FIND_IN_SET(liveleakFrequency, 'Never,Monthly,Weekly,Daily');
SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, huluFrequency FROM testtable1 GROUP BY huluFrequency ORDER BY FIND_IN_SET(huluFrequency, 'Never,Monthly,Weekly,Daily');

SELECT COUNT(*), primaryBrowser, browserSwitchFrequency FROM testtable1 GROUP BY primaryBrowser, browserSwitchFrequency;

SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, browserSwitchFrequency FROM testtable1 GROUP BY browserSwitchFrequency ORDER BY browserSwitchFrequency;

SELECT COUNT(*), primaryBrowser, flashBlockFrequency FROM testtable1 GROUP BY primaryBrowser, flashBlockFrequency;

SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, flashBlockFrequency FROM testtable1 GROUP BY flashBlockFrequency ORDER BY flashBlockFrequency;
