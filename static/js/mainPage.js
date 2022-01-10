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

function handleClickBookmark(cardId, boolean) {
    console.log(boolean)
    $.ajax({
        type: "POST",
        url: "/api/list/bookmark",
        data: {'card_id_give': cardId, 'bookmark_give': boolean },
        success: function (response) {
            alert(response['msg'])
        }
    })
}