library(rms)

train <- read.csv("./src/data/output/train.csv")
head(train)

train$Bug<-as.factor(train$Bug)

model<-lrm(Bug~.,data=train)

dd = datadist(train) 
options(datadist='dd')

model_nomogram <- nomogram(model, fun=function(x)1/(1+exp(-x)),
                           fun.at=c(.001,seq(.1,.9,by=.5),.999),
                           lp = FALSE,
                           funlabel="BugProbability",
                           abbrev = TRUE)

png(file="./src/data/output/lr_nomogram.png",
    width=1500, height=1000)
plot(model_nomogram, xfrac=0.4, cex.var = 2.0, cex.axis = 1.2)
dev.off()