const watchTime = document.querySelector('.watch-time');
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');

let intervalId;
let seconds = 0;
let milliseconds =0;
let time;
let recordTime;

function updateTimer() {
    milliseconds++;
    if (milliseconds === 100) {
        seconds++;
        milliseconds = 0;
    }
    seconds = seconds.toString().padStart(2, '0');
    milliseconds = milliseconds.toString().padStart(2,'0');
    time = seconds+':'+milliseconds;
    watchTime.innerText = time;
}

startBtn.addEventListener('click',(event)=> {
    intervalId = setInterval(updateTimer, 10);
});

//멈췄을 때 기록 저장
const recordList = document.querySelector('.record-list-container');
const allSelectBtn = document.querySelector('.select-btn');
const deleteBtn = document.querySelector('.delete-btn');

stopBtn.addEventListener('click', (event)=> {
    clearInterval(intervalId);
    
    const recordTimeList = document.createElement('li');
    recordTimeList.classList.add("list-title");
    recordTimeList.style.backgroundColor = "white";

    const selectBtn = document.createElement('div');
    selectBtn.classList.add("select-btn");

    const recordNum = document.createElement('p');
    recordNum.classList.add("recordNum");

    const delBtn = document.createElement('div');
    delBtn.classList.add("delete-btn");

    //구조화
    recordTimeList.appendChild(selectBtn);
    recordTimeList.appendChild(recordNum);
    recordTimeList.appendChild(delBtn);

    recordTime = time;    
    recordNum.innerText = time;
    recordList.appendChild(recordTimeList);
    
    //기록 삭제하기
    selectBtn.addEventListener('click',(event)=>{
        event.target.classList.toggle("ri-check-line");

        deleteBtn.addEventListener('click',(e)=>{
            recordList.removeChild(recordTimeList);
        })
        if (selectBtn.classList.contains('ri-check-line')) {
            allSelectBtn.classList.add("ri-check-line");
        }
    })
});

resetBtn.addEventListener('click', (event)=> {
    seconds = 0;
    milliseconds = 0;
    watchTime.innerText = '00:00';
});

