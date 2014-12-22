/**
 * Created by eraldo on 14-12-16.
 */

// Helper variables and functions.
var item_class = "nav-item";
var selection_class = "selected";

function _get_selected_item() {
    return $('.' + item_class + '.' + selection_class)[0];
}
function _select_item(item) {
    if (item) {
        _deselect_item();
        $(item).addClass(selection_class);
    }
}
function _deselect_item() {
    var item = _get_selected_item();
    if (item) {
        $(item).removeClass(selection_class);
    }
}

function _click_selected_or_global_button(button_class) {
    // click the complete button of the selected item
    // or click on the first found non-item complete button
    var item = _get_selected_item();
    if (item) {
        var button = item.getElementsByClassName("item-" + button_class)[0];
    } else {
        // Get the top most non-item complete button.
        var button = $("." + button_class)[0];
    }
    if (button) {
        button.click();
    }
}

function keyboard_help() {
    // Redirect to the keyboard tutorial.
    window.open(keyboard_tutorial_url); // This variable needs to be set before this script.
}
function keyboard_deselect() {
    // Deselect currently selected item.
    _deselect_item();
    // Unfocus the active element if it is an input field.
    var element = document.activeElement;
    var tag = element.tagName;
    // If the active element is a nav-item or input element.
    if (tag == "INPUT" || tag == "SELECT" || tag == "TEXTAREA" || tag.isContentEditable) {
        element.blur();
    }
}
function keyboard_refresh() {
    location.reload();
}
function keyboard_menu(main) {
    if (main) {
        // focus the main menu
        $("#menu a")[0].focus();
    } else {
        // focus the page menu
        var page_menu = $("#page-menu .btn")[0];
        if (page_menu) {
            page_menu.focus();
        }
    }
}

function keyboard_new() {
    _click_selected_or_global_button("new-button");
}
function keyboard_show() {
    // open the detail page of the selected item
    // or open the open-button
    var item = _get_selected_item();
    if (item) {
        var url = item.getAttribute("data-url");
        if (url) {
            window.location.href = url;
        }
    } else {
        _click_selected_or_global_button("open-button");
    }
}
function keyboard_edit() {
    _click_selected_or_global_button("edit-button");
}
function keyboard_delete() {
    _click_selected_or_global_button("delete-button");
}
function keyboard_complete() {
    _click_selected_or_global_button("complete-button");
}

function keyboard_save() {
    _click_selected_or_global_button("save-button");
}
function keyboard_cancel() {
    _click_selected_or_global_button("cancel-button");
}

function keyboard_quick_command() {
    $('#quickCommandModal').modal('toggle');
}

function keyboard_navigate(direction) {
    var item = _get_selected_item();
    if (item) { // selection exists
        if (direction == "down") {
            var next = $(item).next('.' + item_class)[0];
        } else if (direction == "up") {
            var next = $(item).prev('.' + item_class)[0];
        }
    } else {
        if (direction == "down") {
            var next = $('.' + item_class).first()[0];
        } else if (direction == "up") {
            var next = $('.' + item_class).last()[0];
        }
    }
    if (next) {
        $(item).removeClass(selection_class);
        $(next).addClass(selection_class);
        // scroll to item
        $('html, body').animate({
            scrollTop: $(next).offset().top - ($(window).height() / 2) + 'px'
        }, 0);
    }
}

// Keyboard related functions
$('.' + item_class).hover(
    function () {
        _select_item(this);
//        $(this)
    },
    function() {
        _deselect_item(this);
//        $(this).removeClass('hover')
    }
);
