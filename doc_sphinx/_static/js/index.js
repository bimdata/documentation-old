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

// fix expand nav spectacle
const elements = document.querySelectorAll('#nav section');
for(let element of elements){
  element.addEventListener('click', () => {
    element.classList.toggle('expand');
  });
}

// theme switch
// const toggleSwitch = document.querySelector('#themeSwitch');
// const currentTheme = localStorage.getItem('theme');

// if (currentTheme) {
//   document.documentElement.classList.add(currentTheme);

//   if (currentTheme === 'theme-dark') {
//     toggleSwitch.checked = true;
//   }
// }

// function switchTheme(e) {
//   if (e.target.checked) {
//     document.documentElement.classList.add('theme-dark');
//     document.documentElement.classList.remove('theme-light');

//     localStorage.setItem('theme', 'theme-dark');
//   } else {
//     document.documentElement.classList.add('theme-light');
//     document.documentElement.classList.remove('theme-dark');

//     localStorage.setItem('theme', 'theme-light');
//   }
// }

// toggleSwitch.addEventListener('change', switchTheme, false);