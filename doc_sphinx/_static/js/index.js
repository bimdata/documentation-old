import "../scss/style.scss";

$(function() {
  $(document).ready(function() {
    $("a").click(function() {
      var divId = $(this).attr("href");
      $("html, body").animate(
        {
          scrollTop: $(divId).offset().top - 60
        },
        100
      );
    });

    $("#sidebar #nav a").click(function() {
      $("#sidebar #nav a.active").removeClass("active");
      $(this).addClass("active");
    });

    $("section").click(function() {
      if ($("section").hasClass("expand")) {
        $("section").removeClass("expand");
      } else {
        $(this).addClass("expand");
      }
    });
    $("section li a").click(function(e) {
      $(this)
        .parent()
        .parent()
        .addClass("expand");
      e.stopPropagation();
    });
  });
});
