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

    if (id === "") {
        $('#check-id').show()
        $('#userid').focus()
        return;
    } else {
        $('#check-id').hide()
    }

    if (password === "") {
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
            if (response['result'] === 'success') {
                $.cookie('mytoken', response['token']);
                alert('로그인 완료!')

                window.location.replace('/')
            // } else if (id === '' || pw === '') {
            } else if (id === '' || password === '') {
                alert('아이디 또는 비밀번호를 입력해주세요')

            } else {
                //로그인 실패시
                alert(response['msg']);
                // /register 페이지로 이동을 주석처리한 이유는 로그인에 실패해도 본인 아이디나 비밀번호를 잘못 입력했을 수 있기 때문에 로그인 페이지를 유지한다.
                // window.location.replace('/register')

                // /login 페이지로 이동 주석 처리 이유 : replace로 페이지를 다시 리로드 할 경우 본인이 입력하고 있던 아이디나 비밀번호가 모두 사라지기 때문.
                // window.location.replace('/login')
            }
        }
    })
}

$(function () {
        $('.input').keyup(function (e) {
            if (e.keyCode == 13) {
                logIn();
            }
        });
    });