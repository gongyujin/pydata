let site=parseInt(prompt('원하는 번호를 클릭하세요.\n 1.네이버 2.다음 3.구글'));

document.write(site);

switch(site){
    case 1:
        alert('네이버를 선택했습니다.');
        location.href='http://www.naver.com'
    break;
    case 2:
        alert('다음을 선택했습니다.');
        location.href='http://www.daum.net';

    break;
    case 3:
        alert('구글을 선택했습니다.');
        location.href='http://www.google.com'

    break; 
    default: //else랑 같은 의미
        alert('잘못선택하셨습니다.')

    break;
} //break문이 없으면 모든 case를 다 실행하게 됨