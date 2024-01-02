
//Fetch the items from the JSON file 동적으로 data.JSON파일 받아오기
function loadItems() {
    return fetch('data/data.json')
        .then(response => response.json())
        .then(json => json.items);
}

//main 
loadItems() 
    .then(items => {
        console.log(items);
        //displayItems(items);
        //setEventListeners(items)
    })
    .catch(console.log)
