
/*
JAVASCRIPT ERROR FORM
THERE ARE TWO ERRORS ON THIS FILE
FIND THEM KARIM
*/

//1A
const u1a = document.getElementById('U1A');
const b1a = document.getElementById('B1A');
const r1a = document.getElementById('R1A');
b1a.onclick = function evenOdd(){
    let num = u1a.value;
    num = Number(num);
    if (num % 2 === 0){
        r1a.textContent = 'Number is even.';
    }
    else{
        r1a.textContent = 'Number is odd.';
    }
}

//1B
const u1b = document.getElementById('U1B');
const b1b = document.getElementById('B1B');
const r1b = document.getElementById('R1B');
b1b.onclick = function voting(){
    let age = u1b.value;
    age = Number(age);
    if (age < 18){
        r1b.textContent = 'You are not eligible to vote.'
    }
    else{
        r1b.textContent = 'You are eligible to vote.'
    }
}

//1C

//2A

//2B

//2C

//3A

//3B

//3C

//4A

//4B

//4C 