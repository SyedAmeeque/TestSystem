


var radiobtn = document.querySelectorAll('input[name="answer"]');
var save_answer_btn = document.getElementById('save_answer');

radiobtn.forEach(btn =>{
    btn.addEventListener('change', ()=>{
        save_answer_btn.classList.remove('disabled');
    });
});

var form = document.getElementById('mcqs_form');

save_answer_btn.addEventListener('click', function(){
    form.submit();
});







var timer_number = document.querySelector('.timer_number');
var timer_width = document.querySelector('.timer-bg');

function timer(){
    var a = setTimeout(timer, 60000)
    timer_number.innerHTML -= 1;
    var value = timer_number.innerHTML;

    if (value){
        timer_width.style.width = `${value * 1.4}%`;
    }
    


    if (timer_number.innerHTML == 0){
        clearTimeout(a)
        timer_width.style.width = '0%';
        timer_width.style.transform = 'scale(0)';
        window.location.href='exam/completed/successfully/page/Thanks/';
    }
} 

timer();