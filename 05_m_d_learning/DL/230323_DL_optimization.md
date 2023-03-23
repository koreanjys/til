# Model Optimization

## 2. weight regularization (쎄타값을 규제)
- 모델이 복잡할 수록 쎄타 갯수가 많아지고, 쎄타 크기가 커지는데, 이를 이용해서 과대적합을 피하는 방법이다.(모델이 복잡해 진다는 것은 과대적합이 발생할 확률이 높다는 뜻)
- 기존 MSE공식에 + 람다R(쎄타) 공식을 추가. MSE가 낮으면 낮아질 수록 오류가 적어지나 모델 복잡. 과대적합 발생 확률 상승, 그러나 람다R(쎄타)(복잡도가 높아질수록 커짐) 공식으로 너무 크기가 커지는걸 방지
- MSE + 람다R(쎄타) == 규제합이라고 함
- 규제합 공식의 종류는 2개. L1 == Lasso(절대값사용), L2 == Ridge(제곱 사용), L1+L2 == ElasticNet.  이중에 구글이 L2를 권장한다고 한다.
- 람다는 HPO고, 람다를 조정하는것을 Weight Decay를 줄이거나 올린다고 말을 하는데, 가중치를 줄여서 MSE를 중시(정확도를 중시)하거나 가중치를 높여서 과대적합을 더 조심하던가 한다.

## 3. Advanced Gradient Descent
- 딥러닝에서 데이터가 큰것(많은)을 다루기 때문에, Gradient Descent를 진행하면 속도가 상당히 느려질 수 있다. 만약 데이터가 10만개면 1 Epoch 마다 10만번 계산을 하고 쎄타값을 찾고, 2 Epoch로 넘어가서 반복을 하고 . . 이러기 때문이다.
- 그래서 10만개의 데이터를 학습할 때 몇 토막으로 나눠서 (몇 토막으로 나눌지는 사용자가 정한다. HPO) 한 토막을 학습하고, 쎄타값들을 수정하고 하는 방법으로 오류를 줄여나간다.
- 한번 학습하고 쎄타값 수정하는걸 Stochastic(확률적) Gradient Descent(경사 하강법) => SGD 라고 한다. Batch == 1
- Batch는 몇개를 학습하고 쎄타값을 수정할지 정하는것 . HPO
- 여러개를 Batch로 설정하면 Mini-Batch Stochastic Gradient Descent라고 한다.
- 기존 방법인 한번에 모든 데이터를 학습하고 수정하는걸 Full-Batch SGD 라고 한다.
- 1 Epoch => 총 데이터를 1회 돌림.
- 1 iteration => 한 토막을 1회 돌림 == 1 Gradient Descent
- 한 토막을 1 Batch size 라고 한다.
---
- Gradient Descent(이하 GD)의 Learning Rate(이하 LR)를 scheduling(조절) 하는 방법도 발전하고있는데, 그중 권장하는 알고리즘으로 Adam, RMSProp, Adagrad 가 있다. 셋중에 하나 골라쓰길 권장하고, 큰 차이는 없다.
- 작동 방식은, 초기 LR를 GD가 진행 될 수록 수치를 줄여나간다거나, 여러 방법으로 가장 정확도가 높은 지점으로 조절하는 방법이다. 그것을 LR Scheduling이라고 한다.

## Avoid Over Fitting
1. `Drop out (성능 향상에 좋다. 보통 마지막 1개나 2개의 Hidden Layer에서 사용. 학습이 끝나면(train 데이터 학습) Drop out을 걷어준다.(test 데이터에서는 Drop out을 사용하지 않음))` => HPO (0.5 는 50% 적용 한다는 말). 활성화 된 perceptron의 비율을 매 GD 마다 랜덤으로 변화시킴. 효과로는 이미지를 다양하게 학습시키는 모델앙상블의 효과가 있다. 그래서 어떤 값이 들어와도 유동적으로 예측이 가능.

2. `Batch Normalization (이걸 사용하면 워낙 강력해서, HE와 L2 이런것을 적용하지 않아도 됨. 결국 Drop out 과 Batch Normalization 두가지만 사용해도 될 정도)` => Hidden Layer에서 계산 된 perceptron에 적용시켜준다. 이미지 학습에서는 사용하지 않아도 된다고 알고있음. 행렬곱들의 합 => Batch Norm => ReLU 이런 순서로 적용이 일반적임. Batch Norm은 일반적인 std에 추가적으로 std * r(감마) + b(베타) 를 적용한다 => 이유는 이렇게 해줘야 Activation Function을 사용했을 때 비선형으로 변화되어 단순계산을 벗어나게 해준다. 


## 번외
1. Tree 기반 모델은 Normalization 안써도 된다고 함. 큰 효과 없어서.
2. 전이학습 => 기존 모델에 학습된것을 마지막 부분에 Layer 몇개만 추가해서 사용하는 방법


## HPO
1. Epoch(에포크) => 가능하면 많이 주고, 에러값이 바닥을 찍고 올라가는걸 보면, 올라가기 전 값으로 지정
2. Batch size => 보통 2의x제곱 토막을 내거나 10토막을 낸다.
3. Learning rate => 0.01 or 0.001
4. Normalization => 필요에 의해 사용 (데이터 수치 분포가 클때. 이미지 데이터에는 잘 사용 안한다고 함)
5. Layer size, Perceptron => 정해진게 없다.
6. loss function (손실함수) => MSE , Cross Entropy 같은것
7. 규제합 L1, L2 => 사용 잘 안한다고 한다.
8. Drop out => 마지막 히든레이어의 1개나 2개정도에 사용한다고 한다.
