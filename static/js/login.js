function register() {
            window.location.href = "/register"
        }


function logIn() {

    let id = $('#userid').val()
    let password = $('#userpw').val()


    if (id.includes('@')) {
        $('#check-email').hide()
    } else if ( id == '') {
        $('#check-email').hide()
    } else
        $('#check-email').show()
        $('#userid').focus()

    if (id == "") {
        $('#check-id').show()
        $('#userid').focus()
        return;
    } else {
        $('#check-id').hide()
    }

    if (password == "") {
        $('#check-password').show()
        $('#userpw').focus()
        return;
    } else {
        $("#check-password").hide()
    }


    $.ajax({
        type: "POST",
        url: "/api/login",
        data: {
            id_give: id,
            password_give: password
        },
        success: function (response) {
            //로그인 성공시
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'});
                alert('로그인 완료!')
                window.location.replace('/index')
            } else {
                //로그인 실패시
                alert(response['msg']);
                window.location.replace('/register')
            }
        }
    })
}