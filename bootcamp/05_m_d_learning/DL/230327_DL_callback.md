# 콜백함수
1. 콜백함수 정의
```
callback_checkpoint = tf.keras.callback.ModelCheckpoint(filepath='저장 할 파일위치', monitor='val_loss' # 이건 default, save_best_onlt=True, verbose=0)
```
2. 콜백함수 호출 & 모델 학습
```
history = model.fit(train_data, train_label, batch_size=100, epochs=100, validation_split=0.3, verbose=0, callbacks=[ callback_checkpoint ] # 콜백함수는 리스트로 받는다. 그말은 즉슨 여러가지 동시에 받을 수 있다는 말)
```
3. 콜백함수로 저장된 모델을 불러와서 성능 검증
```
model = models.load_model('경로및 파일이름')
result = model.evaluate(test_data, test_label)

result[0] == 에러 수치 # (낮아야 좋음)
result[1] == 평가 점수 # (높아야 좋음)
```