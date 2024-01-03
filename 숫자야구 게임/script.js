//게임 초기화
//시도 가능한 횟수 설정
const submitBtn = document.querySelector('.submit-button');
const inputNum1 = document.getElementById("number1");
const inputNum2 = document.getElementById("number2");
const inputNum3 = document.getElementById("number3");
let attempt = 6;
submitBtn.addEventListener('click',()=>{
    attempt = attempt-1;
    inputNum3.value = '';
    inputNum1.value = '';
    inputNum2.value = '';
    console.log(attempt);
})
//중복 아닌 숫자 3개 설정
function getRandomNumbers() {
    let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let randomNumbers = [];
  
    while (randomNumbers.length < 3) {
      let randomIndex = Math.floor(Math.random() * 10);
      let randomNumber = numbers[randomIndex];
      
      if (!randomNumbers.includes(randomNumber)) {
        randomNumbers.push(randomNumber);
      }
    }
  
    return randomNumbers;
  }  
let [num1, num2, num3] = getRandomNumbers();
let numList = [num1, num2, num3];
//input 결과창 비우기
const checkResults = document.querySelectorAll('.check-result');//querySelectorAll 클래스 요소 전체
for(let i=0; i<3; i++){
    checkResults[i].style.display = 'none'
}
console.log(num1,num2,num3);

//숫자 확인
const resultDisplay = document.querySelector('.result-display');

function check_numbers() {
    
    let inputNumList = [Number(inputNum1.value), Number(inputNum2.value), Number(inputNum3.value)];   
    let countBall = 0; 
    let countStrike = 0;
    if (inputNum1.value === "" || inputNum2.value === "" || inputNum3.value === "") {
        document.getElementById("number1").value = "";
        document.getElementById("number2").value = "";
        document.getElementById("number3").value = "";
        attempt = attempt+1;
    }
    else{
        if (!numList.includes(inputNumList[0]) && !numList.includes(inputNumList[1]) && !numList.includes(inputNumList[2])){
            //out일 때 HTML 쓰기
            console.log("out");
            const checkResult = document.createElement('div');
            checkResult.className = 'check-result';
            const left = document.createElement('div');
            left.innerText = inputNumList.join(" ");
            const right =document.createElement('div');
            right.className = 'right';
            const out = document.createElement('div');
            out.className = 'out num-result';
            left.className = 'left';
            out.innerText = 'O';
            const colone = document.createElement('span');
            colone.innerText = ':';
            checkResult.appendChild(left); 
            checkResult.appendChild(colone);           
            checkResult.appendChild(right);
            right.appendChild(out);
            resultDisplay.appendChild(checkResult);
        }
        else{
            for(let i=0; i<3; i++){
                if(numList.includes(inputNumList[i])){//i인덱스의 숫자가 numList 안에 존재하는지
                    if(numList[i]==inputNumList[i]){//위치가 같은지 보기
                        countStrike++;
                        console.log("strike"+countStrike);
                    }
                    else {
                        countBall++;
                        console.log("Ball"+countBall);
                    }
                }
            }
            if(countStrike == 3){
                const resultImg = document.querySelector('#game-result-img');
                resultImg.src = 'success.png'
                submitBtn.disabled = true;
                submitBtn.style.cursor="default";
            }
            //strike ball HTML에 나오도록
            const checkResult = document.createElement('div');
            checkResult.className = 'check-result';
            const left = document.createElement('div');
            left.className = 'left';
            left.innerText = inputNumList.join(" ");
            const right = document.createElement('div');
            right.className = 'right';
            const strike = document.createElement('div');
            strike.className = 'strike num-result';
            strike.innerText = 'S';
            const ball = document.createElement('div');
            ball.className = 'ball num-result';
            ball.innerText = 'B';
            const colone = document.createElement('span');
            colone.innerText = ':';
            const strikeNum = document.createElement('span');
            strikeNum.innerText = countStrike+' ';
            const ballNum = document.createElement('span');
            ballNum.innerText = ' '+countBall+' ';
            right.appendChild(strikeNum);
            right.appendChild(strike);
            right.appendChild(ballNum);
            right.appendChild(ball);
            checkResult.appendChild(left);
            checkResult.appendChild(colone);
            checkResult.appendChild(right);
            resultDisplay.appendChild(checkResult);  
        }
    }
    if(attempt == 1){
        submitBtn.disabled = true;
        submitBtn.style.cursor="default";
        if(countStrike == 3){
            const resultImg = document.querySelector('#game-result-img');
            resultImg.src = 'success.png'
        }
        else{
            const resultImg = document.querySelector('#game-result-img');
            resultImg.src = 'fail.png'
        }
    }    
}
