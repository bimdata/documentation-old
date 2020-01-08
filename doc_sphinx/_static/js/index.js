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

    $("#nav section li a").click(function(e) {
      $(this)
        .parent()
        .parent()
        .addClass("expand");
      e.stopPropagation();
    });
  });
});

const elements = document.querySelectorAll('#nav section');
for(let element of elements){
  element.addEventListener('click', () => {
    element.classList.toggle('expand');
  });
}
