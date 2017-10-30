$(document).ready(function() {
    $('object.relationshipGraph').hide();
    $('img.relationshipIcon').bind('click', function() {
        $('object.relationshipGraph').hide();
        $('#'+$(this).attr('data-tag')).fadeIn("fast");
    });
});
