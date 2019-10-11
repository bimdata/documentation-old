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

    $("section").on("click", function() {
      $(this)
        .closest("section")
        .toggleClass("expand");
    });
  });
});
