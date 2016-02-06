var simplemdeJQuery = null;

if (typeof jQuery !== 'undefined') {
    simplemdeJQuery = jQuery;
} else if (typeof django !== 'undefined') {
    //use jQuery come with django admin
    simplemdeJQuery = django.jQuery
} else {
    console.error('cant find jQuery, please make sure your have jQuery imported before this script');
}

var simplemde = null;

function pre_renderer(text) {
    // replace user links
    return text.replace(/@(\w+)/g, "<a href='/legends/$1' target='_blank'>$1</a>")
}

if (!!simplemdeJQuery) {
    simplemdeJQuery(function () {
        simplemdeJQuery.each(simplemdeJQuery('.simplemde-box'), function (i, elem) {
            var options = JSON.parse(simplemdeJQuery(elem).attr('data-simplemde-options'));
            options['element'] = elem;

            // create a renderer based on the previewRender
            options.previewRender = function (plainText) {
                return SimpleMDE.prototype.markdown(pre_renderer(plainText));
            };

            simplemde = new SimpleMDE(options);
        });
    });
}
