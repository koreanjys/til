# Logistic Regression (로지스틱 회귀분석)

## Confusion Matrix (혼동 행렬)

|||실제|정답|
|-|-|-|-|
|||<span style="color:yellow">Positive|<span style="color:yellow">Negative|
|예측|<span style="color:skyblue">Positive|True Positive(TP)|False Positive(FP)|
|결과|<span style="color:skyblue">Negative|False Negative(FN)|True Negative(TN)|

### Accuracy(정확성)
- TP + TN / TP + TN + FP + FN

### Recall(재현율)
- TP / TP + FN
- 안좋은 일이 일어날 것을 예측하는데 사용
   - 예시: 지진이 일어나지 않을것이라고 예측을 했는데, 실제로 일어났다면 매우 큰일이기 때문에, FN을 최대한 줄여줘야 좋은 모델로 선정. FN을 줄임으로써 신뢰도가 상승 => 일어나지 않는다고 예측 했을 때 정말로 일어나지 않은 경우가 많아야 함.

### Percision(정밀도)
- TP / TP + FP
- 맞다고 예측한게 정말로 맞아야 할때 사용
    - 예시: 스팸메일이라고 예측한게 정말로 스팸메일이어야 한다. 만약 스팸메일이라고 예측한게 스팸메일이 아닌 중요한 메일이라면 큰일나기 때문에. FP를 최대한 줄여줘야 좋은 모델로 선정. FP를 줄임으로써 신뢰도가 상승 => 맞다고 예측한게 틀리면 신뢰도가 하락.
  
### F1-Score(조화평균)
- 2 * R * P / R + P

### F-beta score
- 1 이 디폴트 값. 조화평균 공식과 같아짐.
- 수치를 조절하면 가중치 변화