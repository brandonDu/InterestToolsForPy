

data <- read.csv("D:/gitStockPy/stock_2015_05_28.csv", header=FALSE)

mode(data)

# todStarPri, yesEndPri, nowPri, todMaxPri, todMinPri, nowBuyPri, nowSelPri, dealNum, dealMoney, buyOneNum, buyOnePri, buyTwoNum, buyTwoPri, buyThrNum, buyThrPri, buyForNum, buyForPri, buyFivNum, buyFivPri, selOneNum, selOnePri, selTwoNum, selTwoPri, selThrNum, selThrPri, selForNum, selForPri, selFivNum, selFivPri
dataYes <- data[1:33]
dataTod <- data[34:66]
name <- data[1]
colnames(name) <- c("name")
dataYes <- dataYes[2:30]
dataTod <- dataTod[2:30]
rate <- (dataTod[4]-dataYes[3])/dataTod[2]*100
colnames(rate) <- c("rate")

rate <- round(rate, digits = 2)

rate <- cbind(name,rate)

rawdata <- cbind(dataYes,rate[2])


colnames(rawdata) <- c("todStarPri", "yesEndPri", "nowPri", "todMaxPri", "todMinPri", "nowBuyPri", "nowSelPri", "dealNum",
                       "dealMoney", "buyOneNum", "buyOnePri", "buyTwoNum", "buyTwoPri", "buyThrNum", "buyThrPri",
                       "buyForNum", "buyForPri", "buyFivNum", "buyFivPri", "selOneNum", "selOnePri", "selTwoNum", "selTwoPri", 
                       "selThrNum", "selThrPri", "selForNum", "selForPri", "selFivNum", "selFivPri","rate")
colnames(dataTod) <- c("todStarPri", "yesEndPri", "nowPri", "todMaxPri", "todMinPri", "nowBuyPri", "nowSelPri", "dealNum",
                       "dealMoney", "buyOneNum", "buyOnePri", "buyTwoNum", "buyTwoPri", "buyThrNum", "buyThrPri",
                       "buyForNum", "buyForPri", "buyFivNum", "buyFivPri", "selOneNum", "selOnePri", "selTwoNum", "selTwoPri", 
                       "selThrNum", "selThrPri", "selForNum", "selForPri", "selFivNum", "selFivPri")

rawdata <- cbind(name,rawdata)

rawdataPre <- cbind(name,dataTod)

d.rawdata <- as.data.frame(rawdata)
d.rawdatapre <- as.data.frame(rawdataPre)

d.sub <- subset(d.rawdata, selOneNum>0)
d.subpre <- subset(d.rawdatapre,selOneNum>0)

toCal <- d.sub
toPre <- d.subpre

View(toPre)
View(toCal)
mode(d.rawdata)

