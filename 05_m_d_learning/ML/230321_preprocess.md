## Preprocessing 중요

1. Numerical 의 각 Columns 의 수치 분포가 너무 크다면 MinMaxScaler나 StandardScaler 로 수치 편차를 줄여주는게 성능향상에 매우 좋다. 그중에서도 StandardScaler를 쓰는게 좋다고 한다.
2. Cartegorical Columns 는 Label Encoder와 One-Hot Encoder가 있는데, One-Hot Encoder가 성능에 더 좋다고 한다.

3. train_test_split 도 중요한데, Feature 값과 Target 값의 적절한 비율로 분포를 해서 나눠주는게 안정적인 성능에 기여한다. 특히 데이터가 적을때 유용


## 번외 Feature_importance

- Permutation importance(퍼뮤테이션 임포턴스) : 학습 모델 종류와 상관없이 모델을 설명할 때 사용할 수 있는 모델 애그노스틱 방법임. 잘 쓰임. 물론 딥러닝 같은 불투명한 모델엔 사용 힘듦