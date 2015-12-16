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

data <- dbGetQuery(con, "SELECT operatingSystem, CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)) as percentFirefox, CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) as percentChrome from testtable1 GROUP BY operatingSystem ORDER BY operatingSystem;")

#names(data)

#data.m <- as.matrix(data)

#data.t <- as.table(data.m)

#data.df <- as.data.frame(data.m)

# http://stackoverflow.com/questions/25322263/r-grouped-histogram
#automatically groups the first column
groupingField = names(data)[1]
groupingField = 'operatingSystem'

ddf2 = melt(data, id='operatingSystem')

ggplot(ddf2, aes(x=operatingSystem, y=value, fill=variable))+geom_bar(stat='identity', position='dodge')
