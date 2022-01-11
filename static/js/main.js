function handleClickDeleteCard(cardId) {
    $.ajax({
        type: "POST",
        url: "/api/list",
        data: {'card_id_give': cardId},
        success: function (response) {
            alert(response['msg'])
        }
    })
}

function handleClickBookmark(cardId) {
    $.ajax({
        type: "POST",
        url: "/api/list/bookmark",
        data: {'card_id_give': cardId },
        success: function (response) {
            alert(response['msg'])
        }
    })
}