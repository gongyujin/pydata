var age =0;
age = (prompt('당신의 나이는?','0')); // 숫자로 입력되지 않으면 NaN으로 들어감 
alert(typeof age); 
if (age>=20){ // 숫자랑 비교하게 되면 문자형이여도 자동으로 형변환을 해줌 ==> 문자형이여도 에러나지 않음
    document.write('당신은 성인입니다.');
}else{
    document.write('당신은 미성년자입니다.'); // else안에 NaN도 포함되기 때문에 결과값이 나오게됨(에러나지 않음)
}