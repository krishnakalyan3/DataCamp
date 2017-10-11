# Scatterplot of weight vs. weeks
ncbirths

ggplot(data = ncbirths, aes(y = weight, x = weeks)) + geom_point() 

# Boxplot of weight vs. weeks
ggplot(data = ncbirths, 
       aes(x = cut(weeks, breaks = 5), y = weight)) + geom_point()
