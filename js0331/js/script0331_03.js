// alert('test')

let num1=10;
let num2=5;
let num3='10';
let result=0;

document.write(num1>num2);
document.write('<br>');
document.write(num1==num2);
document.write('<br>');
document.write(num1==num3); // 타입관계없이 데이터만 비교하기 때문에 True
document.write('<br>');
document.write(num1===num3); // 데이터 타입이 같은지 비교하기 때문에 False

// document.write('num1+num2의 결과값 : '+(num1+num2))