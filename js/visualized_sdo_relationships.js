$(document).ready(function() {
    $('img.relationshipGraph').hide();
    $('img.relationshipIcon').bind('click', function() {
        $('img.relationshipGraph').fadeOut("fast");
        $('#'+$(this).attr('data-tag')).fadeIn("fast");
    });
});
