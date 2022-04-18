let num = prompt('숫자를 입력하세요.','0');
// num이 짝수이면 짝수입니다. 홀수이면 홀수 입니다. 출력하시오.
// 입력한 값의 7로 나눠서 몫을 출력하시오.
if (num%2==0)
    document.write('짝수입니다.'+'<br>')
else
    document.write('홀수입니다.'+'<br>')

let result=parseInt(num/7)
let result1=num%7
document.write('7로 나눈 몫 : '+result+'<br>')
document.write('7로 나눈 나머지 : '+result1+'<br>')

// let num=20
// if (num>10)
// document.write('10보다 큽니다.'); // if문 한줄코드할때는 중괄호를 쓰지 않아도 에러나지 않음
// // document.write('111보다 큽니다.'); //중괄호없이 두줄이상 쓰면 에러남
// else
// document.write('10보다 작습니다.');
