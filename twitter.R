install.packages("twitteR")
woeid = availableTrendLocations[1, "woeid"]
t1 <- getTrends(woeid)
install.packages("twitteR")
install.packages("RColorBrewer")
woeid = availableTrendLocations[1, "woeid"]
install.packages("rtweet")
library(rtweet)
get_trends("Delhi")
get_trends("Mumbai")
t1 = get_trends("Chennai")
t1["trends"]
t1["trend"]
t1 = get_trends("India")
t1["trend"]
df = as.data.frame(t1)
grep("#.*",df$trend,value = TRUE)

write.csv(df,"twitter.csv")
