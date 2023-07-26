# 오늘 배운 DL tensorflow & keras 의 처리 순서를 쭉 나열해 보자.

## 모델 생성 1. 도화지 가져오기
1. model = model.Sequention() => 순차적으로 모델을 쌓는것 (그림 그리기 전에 도화지를 놓는 것)

## 모델 생성 2. 도화지에 채워넣기
2. model.add(layers.Dense(input_dim=`데이터의 열 갯수(당연히 첫 layer만 값을 줌)`, units=`perceptron 갯수`, activation=`None(논으로 준 이유가 바로 활성화 하지 않고 중간에 Batch_Norm을 쓸까봐)`, kernel_initializer=`initializers.he_normal() 이것은 쎄타값 초기화 해주는것. 좋은값으로 정해줌`))
3. model.add(layers.BatchNormalization())  # 계산 된 값을 standard scaler 해주는것 . 필요하면 사용
4. model.add(layers.Activation='elu')  # 선형을 비선형으로 바꿔주기 위해서 껍데기 함수를 덮어 씌우기

## 모델 생성 3. output 그리기
5. model.add(layers.Dense(units=`정답의 열 갯수`, activation=`'softmax'`))

## 모델 생성 4. compile
6. model.compile(optimizer=`optimizers.Adam(0.01) Gradient Descent의 발전형 모델인 Adam(learning_rate)`, loss=`losses.categorical_crossentropy 이것은 에러값을 정하는건데 카테고리컬은 이걸쓰고, 뉴메리컬은 mse쓰면 될듯`, metrics=`[metrics.categorical_accuracy] 점수 매기기`)

이 다음엔
```
tf.keras.callbacks.ModelCheckpoint
```
```
history = model.fit(train_data, train_label, batch_size=100, epochs=20, validation_split=0.3) 
```
```
 "Evaluate" the model on test data

result = model.evaluate(test_data, test_label)

print('loss (cross-entropy) :', result[0])
print('test accuracy :', result[1])
```
시각화 해보고, 새로운 데이터 있으면 입혀보고~~~~

오늘은 이만!