# XPATH

## XPATH 기본

xpath=//tagname[@attribute='value']

- // : 현재 노드 선택
- tagname : 특정 노드의 tagname
- @ : 속성 선택
- attribute : 속성 이름
- value : 속성 값(내용)

## OR 과 AND

- OR과 AND도 가능하다.
```
xpath=//tagname[@id='submit or @name='btn']
xpath=//tagname[@id='submit and @name='btn']
```

## XPATH 함수들

1. `local-name(node-set)`

- 주어진 노드 집합의 각 노드의 로컬 이름을 반환합니다.
- 찾아지지 않는 'svg'태그 같은걸 찾는데 쓰임?
```
//*[local-name()='svg']
```

2. `name(node-set)`

- 주어진 노드 집합의 각 노드의 전체 이름(네임스페이스 접두사를 포함한 이름)을 반환합니다.

3. `contains(string, substring)`

- 문자열 string이 부분 문자열 substring을 포함하는지 여부를 반환합니다.
```
//*[contains(@속성이름, '포함되는 일부 text')]  # 여기서 *은 모든 태그를 의미
```

4. `starts-with(string, prefix)`

- 문자열 string이 접두사 prefix로 시작하는지 여부를 반환합니다.
```
//*[starts-with(@id, '시작text')]
```

5. `ends-with(string, suffix)`

- 문자열 string이 접미사 suffix로 끝나는지 여부를 반환합니다.

6. `string-length(string)`

- 문자열 string의 길이를 반환합니다.

7. `normalize-space(string)`

- 문자열 string의 공백을 정규화하여 앞뒤 공백을 제거하고 연속된 공백을 하나로 축약합니다.

8. `translate(string, from, to)`

- 문자열 string에서 from에 해당하는 모든 문자를 to로 변환합니다.

9. `substring(string, start, length)`

- 문자열 string에서 시작 위치 start와 길이 length에 해당하는 부분 문자열을 반환합니다.

10. `substring-before(string, delimiter)`

- 문자열 string에서 delimiter 이전의 부분 문자열을 반환합니다.

11. `substring-after(string, delimiter)`

- 문자열 string에서 delimiter 이후의 부분 문자열을 반환합니다.

12. `text()`

- 텍스트를 찾음. text()='행사' 의 경우 '행사'라는 텍스트를 찾음

## XPATH 축 메서드

- 복잡하거나 동적요소를 찾는데 쓰인다고 한다.

1. `fallowing : 현재 노드 다음에 오는 노드들 선택?`

```
//*[@type='text']//following::input  # input은 tagname
```
2. `fallow-sibling : 현재 노드 다음에 오는 형제 노드들 선택`

3. `preceding : 현재 노드 이전에 오는 노드들 선택?`

4. `ancestor : 현재 노드의 모든 조상(부모 조부모 등)요소 선택`

5. `descendent : 현재 노드의 모든 자손(자식 손자 등)요소 선택`

6. `parent : 현재 노드의 모든 부모 요소 선택`

- 등등 이 외에도 사용 방법이 있을 것으로 봄