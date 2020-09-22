function get_recomendation(path) {

    if(path == undefined){
        path = "";
    }
    var content = $('#recommendations');

    $.ajax({
        url: `/api/recommendations/${path}`,
        type: "GET",
        contentType: "json",
        dataType:"json",
        data: {
            user: Cookies.get('dimension2')
        },
    })
    .done(function (data) {
        content.prepend('<div class="col"><ul>')
        data.forEach(element => {
            content.prepend(`<li>${element.title}</li>\
                <li><b>SKU:</b> ${element.sku}</li>\
                <li><b>R$ </b>${element.price},99</li>`
            )
        });
        content.prepend('</ul></div>')
    })
    .fail(function (jqXHR, textStatus) {
        console.log(jqXHR);
        console.log(textStatus);
    });

};

$(window).on('load', function () {
    $('.level-bar-inner').each(function () {
        var itemWidth = $(this).data('level');
        $(this).animate({
            width: itemWidth
        }, 800);
    });
});

jQuery(document).ready(function ($) {

    /*======= Skillset *=======*/
    $('.level-bar-inner').css('width', '0');

    /* Bootstrap Tooltip for Skillset */
    $('.level-label').tooltip();
});