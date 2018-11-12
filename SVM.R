# ライブラリ呼び出し
library(kernlab)

# データ入力
train.data = read.csv("learn_data_B.csv",header = F)
test.data = read.csv("test_data.csv",header = F)

# 正解ラベル
Correct.label = test.data[,63]

# 列名操作
x = 1:62
colnames(train.data) = c(x,"y")
colnames(test.data) = c(x)

# ラベルを名義尺度に変更
train.data$y = as.factor(train.data$y)

# SVM判別モデルの作成
svm_model = ksvm(y~.,data=train.data)

# 判別結果
result = predict(svm_model,test.data)
table(Correct.label,result)