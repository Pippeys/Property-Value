## Scott and jordans excellent adventure
library(tidyr)
library(dplyr)
library(ggplot2)

## Read data 
data <- read.csv("/Users/magicsoccer10/Dropbox/twerk werk/Guuuuuuud Datar.csv")
# Jordan 
data <- read.csv("/Users/jorda_000/Dropbox/twerk werk/Guuuuuuud Datar.csv")
## Remove incomplete rows if you want to  
any(is.na(data) == T)

data_test <- na.omit(data)
## Create a new data frame without poopie
data_test<-select(data, Zip.Code, Prop.Sale.GRM, Square.Footage, City, Last.Price)

data %>%
  group_by(Zip.Code) %>% 
  summarise(mVal = mean(Last.Price,na.rm = T)) %>% 
  ggplot(aes(x = factor(Zip.Code), y = mVal)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=90, size=8))
## city
data %>%
  group_by(City) %>% 
  summarise(mVal = mean(Last.Price,na.rm = T)) %>% 
  ggplot(aes(x = factor(City), y = mVal)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=90, size=8))
## Ratio of cost and sq footage
data %>%
  group_by(City) %>% 
  summarise(ratchet = mean(Last.Price,na.rm = T)/mean(Square.Footage, na.rm = T)) %>% 
  ggplot(aes(x = factor(City), y = ratchet)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=90, size=8))
## Hone in on Danville
data %>% 
  filter(City == "Danville")

data %>% 
  ggplot(aes(x = Last.Price, y = Square.Footage)) + 
  geom_point() +
  stat_smooth(method = "lm")

