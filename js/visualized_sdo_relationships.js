$(document).ready(function() {
    $('img.relationshipGraph').hide();
    $('img.relationshipIcon').bind('click', function() {
        $('img.relationshipGraph').fadeOut();
        $('#'+$(this).attr('data-tag')).fadeIn();
    });
});