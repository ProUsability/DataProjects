# Need to run as ADMINISTATOR on W7 to install packages

#install.packages("ggplot2")
#library(ggplot2)

install.packages("DBI")
install.packages("RMySQL")

library(DBI)
library(RMySQL)

# http://www.r-bloggers.com/mysql-and-r/
con <- dbConnect(MySQL(), user="root", password="admin", dbname="test", host="localhost")
rs <- dbSendQuery(con, "SELECT operatingSystem, CAST(100*(SUM(primaryBrowser='Firefox')/471) as decimal(5,2)), CAST(100*(SUM(primaryBrowser='Chrome')/450) as decimal(5,2)) from testtable1 GROUP BY operatingSystem ORDER BY operatingSystem;")
data <- fetch(rs)