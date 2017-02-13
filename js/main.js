$(document).ready(function($) {
  $("h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="glyphicon glyphicon-link"></i>';
    if (id) {
      anchor = $("<a />").addClass("header-link").attr("href", "#" + id).html(icon);
      if ($el.has('img').length) {
        anchor.css('top', el.offsetTop + 23 + 'px');
      }
      $el.prepend(anchor);
    }
  });
});
