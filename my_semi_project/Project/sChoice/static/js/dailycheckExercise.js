$(function(){
    $.ajax({
        url:"/static/exercisetest.json",
        dataType:"json",
        success:function(data){
            let note = ''
            note+='<tr><td><progress  id="ex1B" value="'+ data[9].ex1 +'" max="100"></progress></td>'
            note+='<td><progress id="ex2B" value="'+ data[9].ex2 +'" max="100"></progress></td>'
            note+='<td><progress id="ex3B" value="'+ data[9].ex3 +'" max="100"></progress></td></tr>'
            note+='<tr><td>운동1 : '+ data[9].ex1+'kcal</td><td>운동2 : '+ data[9].ex2+'kcal</td><td>운동3 : '+data[9].ex3+'kcal</td></tr>'
            note+='<tr><td></td><td></td><td></td></tr>'
            note+='<tr><td style="color:#ff0000">0분</td><td style="color:#419e46">0분</td><td style="color:#43419e">0분</td></tr>'
            note+='<tr><td>총 운동 시간</td><td>운동 횟수</td><td>1회 평균 운동 시간</td></tr>'

            $("#progressbars").html(note)

            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'doughnut', 
                data: {
                    labels: ['done','remain'],
                    datasets: [{
                        label: '칼로리',
                        data: [80,(100-80),0,0,0],
                        backgroundColor: ['#7CCAAE','#eee'],
                        hoverOffset: 0
                    },
                    {
                        label: '운동1 이름',
                        data: [data[9].ex1,(100-data[9].ex1),0,0,0],
                        backgroundColor: ['#ECEC84','#eee'],
                        hoverOffset: 0
                    },
                    {
                        label: '운동2 이름',
                        data: [data[9].ex2,(100-data[9].ex2),0,0,0],
                        backgroundColor: ['#FFB69B','#eee'],
                        hoverOffset: 0
                    },
                    {
                        label: '운동3 이름',
                        data: [data[9].ex3,(100-data[9].ex3),0,0,0],
                        backgroundColor: ['#A299CA','#eee']
                    },
                ],
                    labels: ['burned','remain']
                },//data.
                options: {
                    aspectRatio: 1,
                    layout: {
                        padding: {
                            left: 70,
                            right: 70,
                            top: 0,
                            bottom: 10,
                        }
                    },
                    responsive: true,
                    cutoutPercentage: 40,
                    legend: {
                        display: false,
                    },
                    title: {
                        display: false,
                    },
                    rotation: 1.5 * Math.PI,
                    borderColor: false,
                    borderRadius: 10,
                    

                    
                }
            });//chart
            
            
        },
                    
        error:function(){

        }
    })//ajax




})//function



