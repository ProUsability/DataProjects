# Need to run as ADMINISTATOR on W7 to install packages

#install.packages("ggplot2")
library(ggplot2)

install.packages("DBI")
install.packages("RMySQL")

library(DBI)
library(RMySQL)
library(reshape2)

# http://www.r-bloggers.com/mysql-and-r/
con <- dbConnect(MySQL(), user="root", password="admin", dbname="test", host="localhost")

#rs <- dbSendQuery(con, "SELECT operatingSystem, CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome from testtable1 GROUP BY operatingSystem ORDER BY operatingSystem;")
#data <- fetch(rs)
#names(data)
#data.m <- as.matrix(data)
#data.t <- as.table(data.m)
#data.df <- as.data.frame(data.m)

# http://stackoverflow.com/questions/25322263/r-grouped-histogram
#automatically groups the first column. Not always correct (see video services). Also ggplot won't take a string for x.
#groupingField = names(data)[1]
#operating systems x prefBrowser
data <- dbGetQuery(con, "SELECT operatingSystem, CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome from testtable1 GROUP BY operatingSystem ORDER BY operatingSystem;")
ddf2 = melt(data, id='operatingSystem')
ggplot(ddf2, aes(x=operatingSystem, y=value, fill=variable))+geom_bar(stat='identity', position='dodge')


#video watching frequency.
#fixed frequency ordering frequency! thanks to: https://kohske.wordpress.com/2010/12/29/faq-how-to-order-the-factor-variables-in-ggplot2/

#youtube
data <- dbGetQuery(con, "SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, youtubeFrequency FROM testtable1 GROUP BY youtubeFrequency ORDER BY FIND_IN_SET(youtubeFrequency, 'Never,Monthly,Weekly,Daily');")
ddf2 = melt(data, id='youtubeFrequency')
ddf2$youtubeFrequency <- factor(data$youtubeFrequency, as.character(data$youtubeFrequency))
ggplot(ddf2, aes(x=youtubeFrequency, y=value, fill=variable))+geom_bar(stat='identity', position='dodge')

#netflix
data <- dbGetQuery(con, "SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, netflixFrequency FROM testtable1 GROUP BY netflixFrequency ORDER BY FIND_IN_SET(netflixFrequency, 'Never,Monthly,Weekly,Daily');")
ddf2 = melt(data, id='netflixFrequency')
ddf2$netflixFrequency <- factor(data$netflixFrequency, as.character(data$netflixFrequency))
ggplot(ddf2, aes(x=netflixFrequency, y=value, fill=variable))+geom_bar(stat='identity', position='dodge')


#SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, vimeoFrequency FROM testtable1 GROUP BY vimeoFrequency ORDER BY FIND_IN_SET(vimeoFrequency, 'Never,Monthly,Weekly,Daily');
#SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, funnyOrDieFrequency FROM testtable1 GROUP BY funnyOrDieFrequency ORDER BY FIND_IN_SET(funnyOrDieFrequency, 'Never,Monthly,Weekly,Daily');
#SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, facebookFrequency FROM testtable1 GROUP BY facebookFrequency ORDER BY FIND_IN_SET(facebookFrequency, 'Never,Monthly,Weekly,Daily');
#SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, yahooFrequency FROM testtable1 GROUP BY yahooFrequency ORDER BY FIND_IN_SET(yahooFrequency, 'Never,Monthly,Weekly,Daily');
#SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, liveleakFrequency FROM testtable1 GROUP BY liveleakFrequency ORDER BY FIND_IN_SET(liveleakFrequency, 'Never,Monthly,Weekly,Daily');
#SELECT CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome, huluFrequency FROM testtable1 GROUP BY huluFrequency ORDER BY FIND_IN_SET(huluFrequency, 'Never,Monthly,Weekly,Daily');
