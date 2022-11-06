var name_task = document.querySelector(".name__task");
var content_task = document.querySelector(".content__task");
// var cb_completed = document.querySelector("#checkbox_completed");
var btn_add = document.querySelector(".btn-Add .btn");

var content__item = document.querySelector(".content");

var delete_task = document.querySelector(".close")

var count_task_header = document.querySelector(".count__tasks")


btn_add.addEventListener('click', function(e){
    e.preventDefault();
    var url = "http://localhost:8000/api/postTask";
    var title = name_task.value;
    var content = content_task.value;
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify({
            title:title,
            content:content
        })
    })
    .then(function (res) {
        return res.json();
    })
    .then(function(data){
        console.log(data);
        name_task.value = "";
        content_task.value = "";
        showTask();
    })
    
})

async function Delete_Task(id_task_deleted){
    var url = "http://localhost:8000/api/deleteTask/";
    await fetch(url + id_task_deleted, {
        method: "DELETE",
    })
    .then(function (res) {
        return res.json();
    })
    .then(function (data) {
        console.log(data);
        showTask();
    })
}
// delete_task.addEventListener("click", function(e){
//     e.preventDefault();
//     console.log(delete_task.id)
// })

function showTask() {
    var url = "http://localhost:8000/api/AllTasks";
    fetch(url)
    .then((res) => res.json())
    .then((data) => {
        count_task_header.innerText = `Bạn có ${data.length} task`;
        let html = '';
        data.map((values) =>{
            html += `
            <div class="item" id = "${values.id}">
                <div class="completed"></div>
                <div class="task">
                    <div class="task__title">${values.title}</div>
                    <div class="task__content">${values.content}</div>
                </div>
                <i class="fas fa-times close" onclick="Delete_Task(${values.id})"></i>
            </div>
            `
        });
        content__item.innerHTML = html;
    })
}

showTask();

