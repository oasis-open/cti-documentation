$(document).ready(function($) {
  $("h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = $('<i class="glyphicon glyphicon-link"></i>');
    if (id) {
      return $el.prepend($("<a />").addClass("header-link").attr("href", "#" + id).html(icon
        .css('top', '50%')
        .css('transform', 'perspective(1px) translateY(-50%)')
        .css('-webkit-transform', 'perspective(1px) translateY(-50%)')
        .css('-ms-transform', 'perspective(1px) translateY(-50%)')
      ));
    }
  });
});
