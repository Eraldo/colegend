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
    //toolbar: [
    //    {
    //        name: "bold",
    //        action: SimpleMDE.toggleBold,
    //        className: "fa fa-bold",
    //        title: "Bold"
    //    },
    //    {
    //        name: "italic",
    //        action: SimpleMDE.toggleItalic,
    //        className: "fa fa-italic",
    //        title: "Italic"
    //    },
    //    {
    //        name: "heading",
    //        action: SimpleMDE.toggleHeadingSmaller,
    //        className: "fa fa-header",
    //        title: "Heading"
    //    },
    //    "|", // Separator
    //    {
    //        name: "quote",
    //        action: SimpleMDE.toggleBlockquote,
    //        className: "fa fa-quote-left",
    //        title: "Quote"
    //    },
    //    {
    //        name: "unordered-list",
    //        action: SimpleMDE.toggleUnorderedList,
    //        className: "fa fa-list-ul",
    //        title: "Generic List"
    //    },
    //    {
    //        name: "ordered-list",
    //        action: SimpleMDE.toggleOrderedList,
    //        className: "fa fa-list-ol",
    //        title: "Numbered List"
    //    },
    //    "|", // Separator
    //    {
    //        name: "link",
    //        action: SimpleMDE.drawLink,
    //        className: "fa fa-link",
    //        title: "Create Link"
    //    },
    //    {
    //        name: "image",
    //        action: SimpleMDE.drawImage,
    //        className: "fa fa-picture-o",
    //        title: "Insert Image"
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
    //        title: "Toggle Preview"
    //    },
    //    {
    //        name: "side-by-side",
    //        action: SimpleMDE.toggleSideBySide,
    //        className: "fa fa-columns no-disable no-mobile",
    //        title: "Toggle Side by Side"
    //    },
    //    {
    //        name: "fullscreen",
    //        action: SimpleMDE.toggleFullScreen,
    //        className: "fa fa-arrows-alt no-disable no-mobile",
    //        title: "Toggle Fullscreen"
    //    },
    //    "|", // Separator
    //    {
    //        name: "guide",
    //        action: "http://nextstepwebs.github.io/simplemde-markdown-editor/markdown-guide",
    //        className: "fa fa-question-circle",
    //        title: "Markdown Guide"
    //    }
    //]
    previewRender: function renderer(text) {
        // replace user links
        text = text.replace(/@(\w+)/g, "<a href='/legends/$1' target='_blank'>$1</a>");
        return SimpleMDE.prototype.markdown(text)
    }
};

if (!!simplemdeJQuery) {
    simplemdeJQuery(function () {
        simplemdeJQuery.each(simplemdeJQuery('.simplemde-box'), function (i, elem) {
            // Use the fixed local settings from the code above
            var simplemde_options = simplemdeOptions;

            // Load and update the default values from django settings
            var django_simplemde_options = JSON.parse(simplemdeJQuery(elem).attr('data-simplemde-options'));
            var options = simplemdeJQuery.extend(simplemde_options, django_simplemde_options);

            // Update the options based on user dependent per field settings
            var spellchecker = simplemdeJQuery(elem).attr('spellchecker');
            if (spellchecker == 'True') {
                var options = simplemdeJQuery.extend(simplemde_options, {spellChecker: spellchecker});
            }

            options['element'] = elem;
            var simplemde = new SimpleMDE(options);
            elem.SimpleMDE = simplemde;
        });
    });
}
