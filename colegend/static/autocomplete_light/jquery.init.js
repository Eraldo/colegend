// Remove as soon as pull request is in: https://github.com/yourlabs/django-autocomplete-light/pull/570/files
var yl = yl || {};

if (yl.jQuery === undefined) {
    if (typeof django !== 'undefined')
        yl.jQuery = django.jQuery;

    else if (typeof $ !== 'undefined')
        yl.jQuery = $;
}
