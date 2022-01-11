function logIn() {

    let val_email = $('#userid').val()
    if (val_email.includes('@')) {
        $('#check-email').hide()
    } else
        $('#check-email').show()

    let id = $('#userid').val()
    let password = $('#userpw').val()

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
                window.location.replace('/')
            } else {
                //로그인 실패시
                alert(response['msg']);
            }
        }
    })
}