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

function handleChangeSelect(action) {
    // const action = $(this).val();
    console.log(action);
    ajaxListSort(action)
}

function handleChangeBookmarkListSelect(action) {
    // const action = $(this).val();
    console.log(action);
    ajaxListSortBookmark(action)
}

function getListHtmls(data, idx) {

    const bookmark = getBookmarkIcon(data);
    const cardImg = getCardImg(data);

    return `<div aria-label="card-item" class="card-item">
            ${bookmark}
            <div></div>
            ${cardImg}
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
                <div class="btn-wrapper">
                    <div onclick="handleClickDeleteCard('${data._id.$oid}')" class="delete-button click">
                        <i class="bi bi-trash-fill"></i>
                    </div>
                    <button class="button view-detail">상세보기</button>
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
            default_list_action_give: action,
        },
        success: function (response) {
            const defaultList = JSON.parse(response.result);

            const defaultAllListHtmls = getAllLists(defaultList);
            const cardListEle = document.getElementById('card-list');
            cardListEle.style.gridTemplateColumns = '1fr 1fr 1fr 1fr';
            $('#card-list').html(defaultAllListHtmls);
        }
    })
}

function ajaxListSortBookmark(action) {
    $.ajax({
        type: "POST",
        url: "/api/sort/bookmark",
        data: {
            bookmark_list_action_give: action,
        },
        success: function (response) {
            const bookmarkList = JSON.parse(response.result);
            const bookmarkListEle = document.getElementById('bookmark-list');

            const bookmarkAllListHtmls = getAllLists(bookmarkList);
            bookmarkListEle.style.gridTemplateColumns = '1fr 1fr 1fr 1fr';
            $('#bookmark-list').html(bookmarkAllListHtmls);
        }
    })
}

function getBookmarkIcon(data) {
    if (data.card_bookmark === 1) {
        return `<div onclick="handleClickBookmark('${data._id.$oid}')" class="bookmark-button active click">
                    <i class="bi bi-bookmark-fill"></i>
                </div>`
    } else {
        return `<div onclick="handleClickBookmark('${data._id.$oid}')" class="bookmark-button click">
                    <i class="bi bi-bookmark-fill"></i>
                </div>`
    }
}

function getCardImg(data) {
    if (typeof data.card_imgs === 'undefined') {
        return `<img src="/static/images/noimg.png" class="card-image"/>`
    } else {
        return `<img src="" class="card-image"/>`
    }
}


function handleSearchKey() {
    if (window.event.keyCode === 13) {
        searchDefault();
    }
}

function handleSearchKeyBookmark() {
    if (window.event.keyCode === 13) {
        searchBookmark();
    }
}

function searchDefault() {
    const select = $("#default-search-select").val();
    const input = $("#default-search").val();

    $.ajax({
        type: "POST",
        url: "/api/search",
        data: {
            input_give: input,
            select_give: select,
        },
        success: function (response) {
            const searchList = JSON.parse(response.result);
            const cardList = document.getElementById('card-list');

            if (searchList.length === 0) {
                $('#card-list').empty();
                cardList.style.gridTemplateColumns = '1fr';
                return $('#card-list').append(getEmptyData());
            }
            const searchAllListHtmls = getAllLists(searchList);
            cardList.style.gridTemplateColumns = '1fr 1fr 1fr 1fr';
            $('#card-list').html(searchAllListHtmls);
        }
    })
}

function searchBookmark() {
    const select = $("#bookmark-search-list").val();
    const input = $("#bookmark-search").val();

    console.log(select)

    $.ajax({
        type: "POST",
        url: "/api/search/bookmark",
        data: {
            input_give: input,
            select_give: select,
        },
        success: function (response) {
            const searchList = JSON.parse(response.result);
            const bookmarkList = document.getElementById('bookmark-list');

            if (searchList.length === 0) {
                $('#bookmark-list').empty();
                bookmarkList.style.gridTemplateColumns = '1fr';
                return $('#bookmark-list').append(getEmptyData());
            }
            const searchAllListHtmls = getAllLists(searchList);
            bookmarkList.style.gridTemplateColumns = '1fr 1fr 1fr 1fr';
            $('#bookmark-list').html(searchAllListHtmls);
        }
    })
}

function getEmptyData() {
    return `<div class="no-search-data">
                <i class="bi bi-exclamation-circle"></i>
                <span>검색 결과가 없습니다.</span>
            </div>`
}