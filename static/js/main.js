$('table.index tbody').on('click', 'tr', function(){
    $('table.index tbody tr.active').removeClass('active');
    $('.select-required').removeAttr('disabled');
    $(this).addClass('active');
});

function confirm_delete(name) {
    return confirm("Are you sure to remove " + name + "?");
}
