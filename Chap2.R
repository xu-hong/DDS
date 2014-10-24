setwd('/Users/xuhong/Documents/Duke/Term 1 Courses/MOOC/DDS/dds_datasets/dds_ch2_nyt')
data1 <- read.csv('nyt1.csv')

# categorize
head(data1)
data1$agecat <- cut(data1$Age, breaks=c(-Inf, 0, 18, 24, 34, 44, 54, 64, Inf))


# view
summary(data1)


# brackets
install.packages("doBy")
library("doBy")
