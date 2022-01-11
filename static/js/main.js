$(document).ready(function () {
    // sortList();
})

function handleClickDeleteCard(cardId) {
    console.log(cardId)
    $.ajax({
        type: "POST",
        url: "/api/list/delete",
        data: {'card_id_give': cardId},
        success: function (response) {
            alert(response['msg'])
            window.location.reload();
        }
    })
}

function getCardList() {
    $.ajax({
        type: "GET",
        url: "/api/list",
        data: {},
        success: function (response) {
            const result = response['msg']
            console.log(result);
        }
    })
}

function handleClickBookmark(cardId) {
    $.ajax({
        type: "POST",
        url: "/api/list/bookmark",
        data: {'card_id_give': cardId},
        success: function () {
            window.location.reload();
        }
    })
}

function handleClickSelect(action) {
    // const action = $(this).val();
    console.log(action);
    ajaxListSort(action)
}

function getListHtmls(data, idx) {

    return `<div aria-label="card-item" class="card-item">
                {% if card.card_bookmark == 1 %}
                    <div onclick="handleClickBookmark('${data._id.$oid}')" class="bookmark-button click">
                        <i class="bi bi-bookmark-fill"></i>
                    </div>
                {% else %}
                    <div onclick="handleClickBookmark('${data._id.$oid}')" class="bookmark-button click">
                        <i class="bi bi-bookmark"></i>
                    </div>
                {% endif %}
                <div class="info-wrapper">
                    <div class="inline">
                        <div>회사</div>
                        <div>${data.card_company}</div>
                    </div>
                    <div class="inline">
                        <div>이름</div>
                        <div>${data.card_name}</div>
                    </div>
                    <div class="inline">
                            <div>직책</div>
                            <div>${data.card_role}</div>
                        </div>
                        <div class="inline">
                            <div>전화번호</div>
                            <div>${data.card_tel}</div>
                        </div>
                        <div class="inline">
                            <div>이메일</div>
                            <div>${data.card_email}</div>
                        </div>
                        <div onclick="handleClickDeleteCard('${data._id.$oid}')" class="delete-button click">
                            <i class="bi bi-trash-fill"></i>
                        </div>
                </div>
            </div>`
}

function getAllLists(listArr) {
    return listArr.reduce((html, item, idx) => {
        return html += getListHtmls(item, idx)
    }, '')
}

function ajaxListSort(action) {
    $.ajax({
        type: "POST",
        url: "/api/sort",
        data: {
            action_give: action
        },
        success: function (response) {
            const data = JSON.parse(response.result);

            const allListHtmls = getAllLists(data);

            $('#card-list').html(allListHtmls);
        }
    })
}
