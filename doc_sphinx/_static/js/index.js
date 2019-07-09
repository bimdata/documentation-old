import '../scss/style.scss';

$(function () {
  $(document).ready(function () {

    $('a').click(function(){
      var divId = $(this).attr('href');
       $('html, body').animate({
        scrollTop: $(divId).offset().top - 60
      }, 100);
    });

    $("#sidebar #nav section a").click(function () {
      $("#sidebar #nav section a.active").removeClass("active");
      $(this).addClass("active");
    });

    $('.toctree-expand').on('click', function () {
      $(this).closest('section').toggleClass('expand');
    });
  });
});