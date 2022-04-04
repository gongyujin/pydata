let a=7;
let b=10;
let c=11;

// 삼항식
// let result=(a>b)? 'a가 더 큽니다':'b가 더 큽니다.';
// let result=(a>b)? a:b;
// document.write(a+','+b+'중에 더 큰수는 ?'+result+'<br>') //만약 if,for문안에 let으로 선언하면 지역변수로 인식하기 때문에 전역으로 선언해줘야함
// document.write('<hr>')
// 삼항식
let result=(a>b)? ((a>c)?a:c):((b>c)?b:c);
document.write(a+','+b+','+c+'중에 더 큰수는 ?'+result+'<br>') //만약 if,for문안에 let으로 선언하면 지역변수로 인식하기 때문에 전역으로 선언해줘야함
document.write('<hr>')

let re2=Math.max(a,b,c);
document.write(a+','+b+','+c+'중에 더 큰수는 ?'+re2+'<br>') //만약 if,for문안에 let으로 선언하면 지역변수로 인식하기 때문에 전역으로 선언해줘야함



let result1='' // 전역변수선언
if (a>b){
    result='a가 더 큽니다.'
}else{
    result='b가 더 큽니다.'
}
document.write(result+'<br>') //만약 if,for문안에 let으로 선언하면 지역변수로 인식하기 때문에 전역으로 선언해줘야함


let sum=0
for(let i=1;i<=10; i++){
    sum+=i
}

document.write('sum의 값 : '+sum)