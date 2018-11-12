# ライブラリ呼び出し
library(MASS)

# データ入力
train.data = read.csv("learn_data_B.csv",header=F)
test.data = read.csv("test_data.csv",header=F)

# 正解ラベル
correct.label = test.data[,63]

# 列名操作
x = 1:62
colnames(train.data) = c(x,"y")
colnames(test.data) = c(x)

# 判別モデル作成
Z = lda(y~.,data=train.data)

# 検定データの判別結果
Y = predict(Z,test.data)
table(test.data[,63],Y$class)

# 学習データの判別結果
table(train.data[,63],predict(Z)$class)
plot(Z,dimen=1)