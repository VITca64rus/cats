num = 1;
count_pagination = 5;

function Change(number) {
    num = number;
}

function ft_add_pagination(length)
{
    var dop = 0;
    document.getElementById('pagination').innerHTML = '';
    if (length % count_pagination != 0)
        dop = 1
    for (var i = 0; i < Math.floor(length/count_pagination) + dop; i++)
        $('#pagination').append(`<li id="${i}" onClick="pres(this.id)">${i+1}</li>`);
}

function ft_add_cats(data)
{
    for(var i = 0; i < data.length; i++)
    {
        $('#cats').append(`<div class="post">
                                <img class="post_info" src=${data[i].photo}>
                                <div class="post_info">
                                    <div class="post_text">
                                        <div id="name">Имя: ${data[i].name}</div>
                                        <div>Порода: ${data[i].breed}</div>
                                        <div>Возраст: ${data[i].age} мес.</div>
                                        <p class="info">${data[i].info}</p>
                                        <a href=/admin/cat?id=${data[i].id}>Подробнее</a>
                                    </div>
                                </div>
                           </div>`);
    }
}

function $_GET(key) {
    var p = window.location.search;
    p = p.match(new RegExp(key + '=([^&=]+)'));
    return p ? p[1] : false;
}

function pres(pageNum=null)
{
    document.getElementById('cats').innerHTML = '';
    let input = document.querySelector('input');
    if (num == null)
        num = 1
    $.getJSON('http://' + window.location.hostname + ':3000/list?sort='+num+'&find='+ input.value, function(data)
    {
        ft_add_pagination(data.length);
        slice_data = data.slice(pageNum * count_pagination, pageNum * count_pagination + count_pagination);
        ft_add_cats(slice_data);
    });
}
