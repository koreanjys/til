# Deep Learning

## Activation Funcion(껍데기 함수) 종류
1. Step & sigmoid => 비선형으로 만들어주나 역전파 에러에 어려움이 있어서 쓰이지 않는다.
2. tanh => sigmoid의 결함을 보완했으나, 잘 쓰이진 않고, text모델에서 가끔 쓰인다고 한다.
3. ReLU => 현재 잘 쓰이는 Activation Funcion. ReLU류의 여러 버전들이 파생되어 나온다.

## out-put layer에서의 회귀와 분류
- 회귀문제(답이 numerical로 도출되는것)이면 out-put layer의 perceptron은 1개이고, 수치가 나온다. 처리가 필요없다.
- 분류문제(답이 categorical로 도출되는것)에서 이진분류의 경우, 두가지 방법이 있다. `첫번째는 label데이터를 sigmoid로 적용` 이 방법은 다중분류에선 다시 두번째 방법을 써야 하기 때문에 권장하는 방법은 두번째 방법이다. `두번째는 One-hot인코딩 후 softmax로 처리하는 방법이다. 이 방법은 이진분류 뿐만 아니라 다중분류에도 사용 할 수 있다. 권장되는 방법!`

## DL 모델 설정 팁
- 복잡한것은 Hidden Layer가 많은것보다(한번의 hidden layer에서 여러개의 perceptron이 있는것) 깊은게(한번의 Epoch에 hidden layer가 1개나 2개더라도, 여러번의 Epoch가 있는것) 더 복잡한 문제를 해결하는데 좋다.

## DL모델 최적화 이론 => 처음 쎄타 값을 잘 잡아줘야 학습 성공률과 빠른 학습을 해서 에러를 잘 줄인다.

1. weight(쎄타) Initialization(초기화)
- Xavier => default이고 사용하는 Activation funcion은 sigmoid와 tanh인데 잘 안쓴다. (공식은 전의 perceptron 갯수를 n에 삽입. 루트1/n)
- He(헤 혹은 허) => 권장하는 방법이고, 파라미터 쎄타 초기화를 잘해준다. 그리고 요즘 잘 사용하는 Activation funcion인 ReLU를 주로 사용한다. (공식은 전의 perceptron 갯수를 n에 삽입. 루트2/n)

## 용어들
- Capacity => 모델의 수용도, 복잡한것을 얼마나 잘 예측 하는지.
- Generalization => 일반화 오류. Overfitting으로 인하여 test 예측도가 낮게 나옴
- MLOps => 모델 성능 측정
- Augmentation => (딥러닝 이미지) 부족한 샘플을 해결하기 위해 이미지에 약간씩 변형을 가해서 샘플 수를 늘리는 방법
- 차원축소 => 때로는 개인정보 보호를 위하여 기존 정보 열을 없애고 새로운 열을 생성하는 방법도 있다.
- SoftMax => 인공신경망의 output-layer에 분류 전처리의 방법. One-Hot 인코딩과 함께 쓰인다. 

> 예시: 만약 이진분류라면 One-Hot 인코딩으로 두개의 퍼셉트론이 output-layer에 오는데, 이를 softmax로 처리를 하면 0.43, 0.57 이런식으로 더하면 1이 되게 만드는 확률적으로 변환하여 사람이 보기 쉽게 만들어준다. 그것을 out-layer의 껍데기함수(cross_entropy)로 완료시킨다.

- Activation funcion(껍데기 함수) => 딥러닝 인공신경망에서 선형을 비선형으로 바꿔주는 함수(Activation funcion이 없으면 아무리 많은 Layer를 쌓더라도 결국 선형(단순)이 되어버려서 그걸 복잡하게 바꿔줄 수 있는게 바로 껍데기함수)
- 전이학습 => 딥러닝에서 HPO를 잘 찾기가 어려워서 , 잘 찾아놓은 모델을 가져와서 사용하는것.
- Hidden Layer => Learnable Kernels
- Learning rate(학습률) => 권장 수치는 0.01 or 0.001, 얼마나 큰 폭으로 gradient descent(경사 하강법)에서 이동하는지 정하는 계수.
- Epoch => 신경망을 통과한 횟수
