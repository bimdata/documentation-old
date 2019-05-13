const toggleSwitch = document.querySelector('#themeSwitch');
const html = document.querySelector('html');
let isDark = '';

document.addEventListener('DOMContentLoaded', function(){
  isDark = localStorage.getItem('state-dark');
  if(isDark == 'Dark'){
    toggleSwitch.setAttribute('checked', true);
    html.classList.add('theme-dark');
  }
  else{
    toggleSwitch.removeAttribute('checked');
    html.classList.remove('theme-dark');
  }

  toggleSwitch.onchange = (e) => {
    if(e.currentTarget.checked){
      html.classList.add('theme-dark');
      isDark = 'Dark';
    }
    else{
      html.classList.remove('theme-dark');
      isDark = '';
    }
    localStorage.setItem('state-dark', isDark);
  }
});
