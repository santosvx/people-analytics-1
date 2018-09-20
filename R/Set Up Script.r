library(readxl)
library(tidyverse)
data1 <- read_excel("~/Workforce Queries/WF Query_training.xlsx")

#replace all NA and blanks
data1[is.na(data1)]<-0 

#changing 'oo' to 'SES'
data2 <- data1
data2$Grade <- as.character(data2$Grade)
data2$Grade[data2$Grade == "00"] <- "SES"

#get back to just original and working data
originaldata <- data1
data <- data2
remove(data1)
remove(data2)

#create smaller dataset
smalldata <- filter(data,Center=='HQ')

#Export to excel
library(writexl)
write_xlsx(x = revisedwfdata, path = "~/Coding/Mock Attrition Data/revised_mock_workforce_data_2.xlsx", col_names = TRUE)