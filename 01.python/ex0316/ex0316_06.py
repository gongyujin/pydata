foods={
    '떡볶이':'오뎅',
    '짜장면':'단무지',
    '라면':'김치',
    '피자':'피클',
    '맥주':'땅콩',
    '치킨':'치킨무',
    '삼겹살':'상추'
}

while True:
    print('-'*45)
    for food in foods:
        print(food,end=' ')
    print()
    # print(foods.keys())
    print('-'*45)
    input1= input('원하는 음식을 입력하세요.>> ')
    
    if input1 in foods:
        print('{}의 궁합이 맞는 음식은 {}입니다.'.format(input1,foods[input1]))
    else:
        print('찾고자 하는 데이터가 없습니다. 다시입력해주세요.')
        
    print()