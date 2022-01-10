function modal_open_btn() {
    $("#modal").css("display", "inline");
    $("html").css("overflow", "hidden");
}

function closebtn() {
    $("#modal").css("display", "none")
}

function checkbtn() {
    let useremail = "123@naver.com"
    let card_nameid = $("#card_nameid").val();
    let card_companyid = $("#card_companyid").val();
    let card_roleid = $("#card_roleid").val();
    let card_positionid = $("#card_positionid").val();
    let card_telid = $("#card_telid").val();
    let card_addressid = $("#card_addressid").val();
    let card_descid = $("#card_descid").val();
    let card_emailid = $("#card_emailid").val();
    let card_bookmarkid = "0"

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
        data: {
            useremail: useremail,
            card_nameid: card_nameid,
            card_companyid: card_companyid,
            card_roleid: card_roleid,
            card_positionid: card_positionid,
            card_telid: card_telid,
            card_addressid: card_addressid,
            card_descid: card_descid,
            card_bookmarkid: card_bookmarkid,
            card_emailid: card_emailid
        },
        success: function (response) {
            alert(response)
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