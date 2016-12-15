library(randomForest)
library(foreign)
# train data : ~,~,rate
# predict data : ~,~ 
training <- toCal[2:31]
predicting <- toPre[2:30]

ind<-sample(2,nrow(training),replace=TRUE,prob=c(0.8,0.2))#/对数据分成两部分，70%训练数据，30%检测数据/
traindata<- training [ind==1,]
testdata<- training [ind==2,]
#begin randoforest. 
data.rf <- randomForest(rate ~ ., data=training, ntree=1000,mtry=7, proximity=TRUE)
# table(predict(rf), training$rate)
print(data.rf)
plot(data.rf)
importance(data.rf)

data.pred <-  predict(data.rf, predicting)

predrate <- as.data.frame(data.pred)
colnames(predrate)<- c('prate')
predresult <- cbind(toPre[1],predrate)
p.result <- as.data.frame(predresult)
p.sub <- subset(p.result, prate>6)

View(p.sub)


