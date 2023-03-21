## Preprocessing 중요

1. Numerical 의 각 Columns 의 수치 분포가 너무 크다면 MinMaxScaler나 StandardScaler 로 수치 편차를 줄여주는게 성능향상에 매우 좋다. 그중에서도 StandardScaler를 쓰는게 좋다고 한다.
2. Cartegorical Columns 는 Label Encoder와 One-Hot Encoder가 있는데, One-Hot Encoder가 성능에 더 좋다고 한다.

3. train_test_split 도 중요한데, Feature 값과 Target 값의 적절한 비율로 분포를 해서 나눠주는게 안정적인 성능에 기여한다. 특히 데이터가 적을때 유용