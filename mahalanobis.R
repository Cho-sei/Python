# データ入力
train.data = read.csv("learn_data_B.csv",header = F)
test.data = read.csv("test_data.csv",header = F)

# 正解ラベル
correct.label = test.data[,63]

# 列名操作
x=1:62
colnames(train.data) = c(x,"y")
colnames(test.data) = c(x,"y")

# F;"-1",T:"1"に分類
Dtrain.F = train.data[train.data$y == "-1",]
Dtrain.T = train.data[train.data$y == "1",]
Dtest = test.data[,1:62]

# m:平均,v:分散共分散行列
Dtrain.F.m = apply(Dtrain.F[,1:62],2,mean)
Dtrain.T.m = apply(Dtrain.T[,1:62],2,mean)
Dtrain.F.v = var(Dtrain.F[,1:62])
Dtrain.T.v = var(Dtrain.T[,1:62])

# マハラノビス距離の測定
D1 = mahalanobis(Dtest,Dtrain.F.m,Dtrain.F.v)
D2 = mahalanobis(Dtest,Dtrain.T.m,Dtrain.T.v)

# 結果の出力
cbind(D1,D2)
result = ifelse(D1<D2,-1,1) # FALSEだと非目的刺激（"-1"）

# 結果の集計
table(correct.label,result)
