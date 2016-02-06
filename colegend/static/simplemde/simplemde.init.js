var simplemdeJQuery = null;

if (typeof jQuery !== 'undefined') {
    simplemdeJQuery = jQuery;
} else if (typeof django !== 'undefined') {
    //use jQuery come with django admin
    simplemdeJQuery = django.jQuery
} else {
    console.error('cant find jQuery, please make sure your have jQuery imported before this script');
}

var simplemdeOptions = {
    autosave: {
        enabled: true,
        uniqueId: "simplemde_autosave_id",
        delay: 6000
    },
    indentWithTabs: false,
    previewRender: function renderer(text) {
        // replace user links
        text = text.replace(/@(\w+)/g, "<a href='/legends/$1' target='_blank'>$1</a>");
        return SimpleMDE.prototype.markdown(text)
    },
    showIcons: ["code", "table"],
    tabSize: 4,
    //toolbarTips: true,
    //toolbar: [
    //    {
    //        name: "bold",
    //        action: SimpleMDE.toggleBold,
    //        className: "fa fa-bold",
    //        title: "Bold",
    //        default: true
    //    },
    //    {
    //        name: "italic",
    //        action: SimpleMDE.toggleItalic,
    //        className: "fa fa-italic",
    //        title: "Italic",
    //        default: true
    //    },
    //    {
    //        name: "heading",
    //        action: SimpleMDE.toggleHeadingSmaller,
    //        className: "fa fa-header",
    //        title: "Heading",
    //        default: true
    //    },
    //    "|", // Separator
    //    {
    //        name: "quote",
    //        action: SimpleMDE.toggleBlockquote,
    //        className: "fa fa-quote-left",
    //        title: "Quote",
    //        default: true
    //    },
    //    {
    //        name: "unordered-list",
    //        action: SimpleMDE.toggleUnorderedList,
    //        className: "fa fa-list-ul",
    //        title: "Generic List",
    //        default: true
    //    },
    //    {
    //        name: "ordered-list",
    //        action: SimpleMDE.toggleOrderedList,
    //        className: "fa fa-list-ol",
    //        title: "Numbered List",
    //        default: true
    //    },
    //    "|", // Separator
    //    {
    //        name: "link",
    //        action: SimpleMDE.drawLink,
    //        className: "fa fa-link",
    //        title: "Create Link",
    //        default: true
    //    },
    //    {
    //        name: "image",
    //        action: SimpleMDE.drawImage,
    //        className: "fa fa-picture-o",
    //        title: "Insert Image",
    //        default: true
    //    },
    //    {
    //        name: "table",
    //        action: SimpleMDE.drawTable,
    //        className: "fa fa-table",
    //        title: "Insert Table"
    //    },
    //    "|", // Separator
    //    {
    //        name: "preview",
    //        action: SimpleMDE.togglePreview,
    //        className: "fa fa-eye no-disable",
    //        title: "Toggle Preview",
    //        default: true
    //    },
    //    {
    //        name: "side-by-side",
    //        action: SimpleMDE.toggleSideBySide,
    //        className: "fa fa-columns no-disable no-mobile",
    //        title: "Toggle Side by Side",
    //        default: true
    //    },
    //    {
    //        name: "fullscreen",
    //        action: SimpleMDE.toggleFullScreen,
    //        className: "fa fa-arrows-alt no-disable no-mobile",
    //        title: "Toggle Fullscreen",
    //        default: true
    //    },
    //    "|", // Separator
    //    {
    //        name: "guide",
    //        action: "http://nextstepwebs.github.io/simplemde-markdown-editor/markdown-guide",
    //        className: "fa fa-question-circle",
    //        title: "Markdown Guide",
    //        default: true
    //    },
    //],
};

var simplemde = null;

if (!!simplemdeJQuery) {
    simplemdeJQuery(function () {
        simplemdeJQuery.each(simplemdeJQuery('.simplemde-box'), function (i, elem) {
            var options = simplemdeOptions;
            //var options = JSON.parse(simplemdeJQuery(elem).attr('data-simplemde-options'));
            options['element'] = elem;
            simplemde = new SimpleMDE(options);
        });
    });
}
