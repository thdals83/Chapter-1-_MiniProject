function modal_open_btn() {
    $("#modal").css("display", "inline");
    $("html").css("overflow", "hidden");
}

function closebtn() {
    $("#modal").css("display", "none")
}

function cardclick_closebtn() {
    $("#modaledit").css("display", "none")
}

function cardclick(id) {
    $("#modaledit").css("display", "inline");
    $("html").css("overflow", "hidden");

    $.ajax({
        type: "POST",
        url: "/api/getcard",
        data: {'getcard_id': id},
        success: function (response) {
            let cardinfo = response["cardinfo"]
            document.getElementById("use_card_nameid").value = cardinfo[0]["card_name"]
            document.getElementById("use_card_emailid").value = cardinfo[0]["card_email"]
            document.getElementById("use_card_telid").value = cardinfo[0]["card_tel"]
            document.getElementById("use_card_companyid").value = cardinfo[0]["card_company"]
            document.getElementById("use_card_roleid").value = cardinfo[0]["card_role"]
            document.getElementById("use_card_positionid").value = cardinfo[0]["card_position"]
            document.getElementById("use_card_addressid").value = cardinfo[0]["card_address"]
            document.getElementById("use_card_descid").value = cardinfo[0]["card_desc"]
            document.getElementById("hide_id").value = cardinfo[0]["_id"]
        }
    })
}

function editbtn() {
    let use_card_nameid = $("#use_card_nameid").val()
    let use_card_emailid = $("#use_card_emailid").val()
    let use_card_telid = $("#use_card_telid").val()
    let use_card_companyid = $("#use_card_companyid").val()
    let use_card_roleid = $("#use_card_roleid").val()
    let use_card_positionid = $("#use_card_positionid").val()
    let use_card_addressid = $("#use_card_addressid").val()
    let use_card_descid = $("#use_card_descid").val()
    let hide_id = $("#hide_id").val()


    if (use_card_nameid === "") {
        $("#use_helpname").text("이름을 입력해주세요.")
        return;
    } else {
        $("#use_helpname").text("")
    }

    if (use_card_emailid === "") {
        $("#use_helpemail").text("이메일을 입력해주세요.")
        return;
    } else {
        $("#use_helpemail").text("")
    }

    if (use_card_telid === "") {
        $("#use_helptel").text("전화번호를 입력해주세요.")
        return;
    } else {
        $("#use_helptel").text("")
    }

    if (use_card_companyid === "") {
        $("#use_helpcompany").text("회사를 입력해주세요.")
        return;
    }
    $.ajax({
        type: "POST",
        url: "/api/editcard",
        data: {
            use_card_nameid: use_card_nameid,
            use_card_emailid: use_card_emailid,
            use_card_telid: use_card_telid,
            use_card_companyid: use_card_companyid,
            use_card_roleid: use_card_roleid,
            use_card_positionid: use_card_positionid,
            use_card_addressid: use_card_addressid,
            use_card_descid: use_card_descid,
            // use_card_bookmarkid: use_card_bookmarkid,
            hide_id: hide_id
        },
        success: function (response) {
            alert(response['msg']);
            window.location.reload()
        }
    })

}

function checkbtn() {
    let useremail = "bbb@naver.com"
    let card_nameid = $("#card_nameid").val();
    let card_companyid = $("#card_companyid").val();
    let card_roleid = $("#card_roleid").val();
    let card_positionid = $("#card_positionid").val();
    let card_telid = $("#card_telid").val();
    let card_addressid = $("#card_addressid").val();
    let card_descid = $("#card_descid").val();
    let card_emailid = $("#card_emailid").val();
    let card_bookmarkid = 0

    let fileInput = document.getElementsByClassName("file");
    let filename = fileInput[0].files[0].name
    let file = $('#file')[0].files[0]

    let form_data = new FormData()

    form_data.append("file",file)
    form_data.append("filename",filename)

    form_data.append("useremail",useremail)
    form_data.append("card_nameid",card_nameid)
    form_data.append("card_companyid",card_companyid)
    form_data.append("card_roleid",card_roleid)
    form_data.append("card_positionid",card_positionid)
    form_data.append("card_telid",card_telid)
    form_data.append("card_addressid",card_addressid)
    form_data.append("card_descid",card_descid)
    form_data.append("card_emailid",card_emailid)
    form_data.append("card_bookmarkid",card_bookmarkid)


    if (card_nameid === "") {
        $("#help-name").text("이름을 입력해주세요.")
        return;
    } else {
        $("#help-name").text("")
    }
    if (card_emailid === "") {
        $("#help-email").text("이메일을 입력해주세요.")
        return;
    } else {
        $("#help-email").text("")
    }
    if (card_telid === "") {
        $("#help-tel").text("전화번호를 입력해주세요.")
        return;
    } else {
        $("#help-tel").text("")
    }
    if (card_companyid === "") {
        $("#help-company").text("회사를 입력해주세요.")
        return;
    }

    $.ajax({
        type: "POST",
        url: "/api/pluscard",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response['msg']);
        }
    })
    window.location.reload()
}

function find_address() {
    new daum.Postcode({
        oncomplete: function (data) {
            document.getElementById("card_addressid").value = data.address
        }
    }).open();
}

function find_address2() {
    new daum.Postcode({
        oncomplete: function (data) {
            document.getElementById("use_card_addressid").value = data.address
        }
    }).open();
}

function loadFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            document.getElementById('preview').src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
    }
}