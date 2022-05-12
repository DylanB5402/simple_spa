// $("#submit_button").click(() => {
//     console.log(1)
// })

function my_function() {
    console.log(1);
    console.log($("#fname").val());
    console.log($("#lname").val());
    $.post("/login", {
        fname : $("#fname").val(),
        lname : $("#lname").val()
    }, (data, status) => {
        console.log(data);
        if(data['login']) {
            $('#login_form').append(`<p> logged in as ${data['fname']}</p>`)
        }
    })
    return false;
}

function new_post() {
    $.post("/new_post", {
        post_name : $("#post_name").val(),
    }, (data, status) => {
        console.log(data);
            $('#post_form').append(`${data['posts']}</p>`)
        // }
    })
    return false
}