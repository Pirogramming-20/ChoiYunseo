// minus 버튼 클릭 시
document.getElementById("minus").addEventListener("click", function() {
    // 현재 like 값 가져오기
    let currentLike = parseInt(document.querySelector(".like").getAttribute("data-like"));

    // 값 감소
    let newLike = currentLike - 1;

    // 서버에 업데이트된 값 전송
    updateLike(newLike);
});

// plus 버튼 클릭 시
document.getElementById("plus").addEventListener("click", function() {
    // 현재 like 값 가져오기
    let currentLike = parseInt(document.querySelector(".like").getAttribute("data-like"));

    // 값 증가
    let newLike = currentLike + 1;

    // 서버에 업데이트된 값 전송
    updateLike(newLike);
});

// 서버에 업데이트된 값 전송하는 함수
function updateLike(newLike) {
    // Ajax 요청 생성
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/update-like", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // 업데이트된 값 전송
    xhr.send(JSON.stringify({ like: newLike }));

    // 응답 처리
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // 응답이 성공적으로 도착하면 화면 업데이트
            document.querySelector(".like").setAttribute("data-like", newLike);
            document.querySelector(".like").textContent = newLike;
        }
    };
}
