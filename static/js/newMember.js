            function new_member() {
                let email1 = $('#email1').val();
                let email2 = $('#email2').val();
                let direct = $('#direct').val();
                let name = $('#name').val();
                let password1 = $('#password1').val();
                let password2 = $('#password2').val();
                let company = $('#company').val();
                let role = $('#role').val();
                let position = $('#position').val();
                let tel = $('#tel').val();
                let address = $('#address').val();

                $.ajax({
                    type: "POST",
                    url: "/newMember",
                    data: {email1:email1, email2:email2, name:name, password1:password1, password2:password2,
                        direct: direct, company: company, role:role, position:position, tel:tel, address:address},
                    success: function (response) {
                        alert(response["msg"]);
                        if(response["msg"] == '회원가입 완료'){
                            window.location.href = '/';
                        }
                        else{
                            window.location.reload()
                        }
                    }
                })
            }

            function validate_email() {
                let validate = true
                let email1 = $('#email1').val();
                let email2 = $('#email2').val();
                let email = email1 + "@" + email2;
                $.ajax({
                    type: "POST",
                    url: "/validate_email",
                    data: {email: email},
                    success: function (response) {
                        validate = response["validate"]

                        if (validate) {
                            alert("사용 가능한 이메일입니다.")
                        } else {
                            alert("이미 존재하는 이메일입니다.")
                        }
                    }
                })
            }
            function api(){
                            new daum.Postcode({
                oncomplete: function (data) {
                    document.getElementById("address").value = data.address;
                }
            }).open();
            }

            function check_pw() {

                var pw = document.getElementById('password1').value;
                var SC = ["!", "@", "#", "$", "%"];
                var check_SC = 0;
                if (pw.length < 6 || pw.length > 16) {
                    window.alert('비밀번호는 6글자 이상, 16글자 이하만 이용 가능합니다.');
                    document.getElementById('password1').value = '';
                }
                for (var i = 0; i < SC.length; i++) {
                    if (pw.indexOf(SC[i]) != -1) {
                        check_SC = 1;
                    }
                }
                if (check_SC == 0) {
                    window.alert('!,@,#,$,% 의 특수문자가 들어가 있지 않습니다.')
                    document.getElementById('password1').value = '';
                }
            if(document.getElementById('password1').value !='' && document.getElementById('password2').value!=''){
                if(document.getElementById('password1').value==document.getElementById('password2').value){
                    document.getElementById('check').innerHTML='비밀번호가 일치합니다.'
                    document.getElementById('check').style.color='blue';
                }
                else{
                    document.getElementById('check').innerHTML='비밀번호가 일치하지 않습니다.';
                    document.getElementById('check').style.color='red';
                }
            }
        }

            function email_change() {
                if (document.join.email.options[document.join.email.selectedIndex].value == '0') {
                    document.join.email2.disabled = true;
                    document.join.email2.value = "";
                }
                if (document.join.email.options[document.join.email.selectedIndex].value == '9') {
                    document.join.email2.disabled = false;
                    document.join.email2.value = "";
                    document.join.email2.focus();
                } else {
                    document.join.email2.disabled = true;
                    document.join.email2.value = document.join.email.options[document.join.email.selectedIndex].value;
                }
            }



