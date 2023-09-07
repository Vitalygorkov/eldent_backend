
/*появление при скроле*/
function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
       change.target.classList.add('element-show');
      }
    });
  }
  
  let options = {
    threshold: [0.5] };
  let observer = new IntersectionObserver(onEntry, options);
  let elements = document.querySelectorAll('.element-animation');
  
  for (let elm of elements) {
    observer.observe(elm);
  }
/*модалка*/

/*// PopUp Form and thank you popup after sending message Всплывающая форма и всплывающее окно с благодарностью после отправки сообщения
var $popOverlay = $(".popup-overlay");
var $popWindow = $(".popWindow");
var $subscribeWindow = $(".subscribe_window");
var $popThankYouWindow = $(".thank_you_window");
var $popClose = $(".close-btn");
var $popOpen = $(".open-btn");

$(function() {

  // Close Pop-Up after clicking on the button "Close" Закрыть всплывающее окно после нажатия на кнопку «Закрыть»
  $popClose.on("click", function() {
    $popOverlay.fadeOut();
    $popWindow.fadeOut();
  });

  // Open
  $popOpen.on("click", function() {
    $popOverlay.fadeIn();
    // $popWindow.fadeIn();
    $subscribeWindow.fadeIn();
  });      
  

  // Close Pop-Up after clicking on the Overlay Закрыть всплывающее окно после нажатия на оверлей
  // $(document).on("click", function(event) {
  //   if ($(event.target).closest($popWindow).length) return;
  //   $popOverlay.fadeOut();
  //   $popWindow.fadeOut();
  //   event.stopPropagation();
  // });

  $($popOverlay).on("click", function(event) {
    if ($(event.target).closest($popWindow).length) return;
    $popOverlay.fadeOut();
    $popWindow.fadeOut();
    event.stopPropagation();
  });


  // Form Subscribe
  $(".subscribe-form").submit(function() {
    var th = $(this);
    $.ajax({
      type: "POST",
      url: "mail.php",
      data: th.serialize()
    }).done(function() {
      // после успешной отправки скрываем форму подписки и выводим окно с благодарностью за заполнение формы
      $subscribeWindow.fadeOut();
      $popThankYouWindow.fadeIn();
      // используем куки на 30 дней, если человек заполнил форму
      // для куки обязательно должен быть подключен jquery.cookie.min.js
      $.cookie('hideTheModal', 'true', { expires: 30 });
      // очищаем форму
      setTimeout(function() {
        th.trigger("reset");
      }, 1000);
    });
    return false;
  });
});

// используйте этот код, если нужно появление формы с куки и вы подключали jquery.cookie.min.js
$(window).load(function() {
  // задаем переменную для cookie
  // var hideTheModal = $.cookie('hideTheModal');
  // если cookie не установлено...
  // if(hideTheModal == null){
    // Через 2 секунды появляется контактная форма
    setTimeout(function() {
      $popOverlay.fadeIn();
      $subscribeWindow.fadeIn();
    }, 1000);
  // }

});*/






/*-----------меню---новое---------*/
const isMobile = {
  Android: function () {
      return navigator.userAgent.match(/Android/i);
  },
  BlackBerry: function() {
      return navigator.userAgent.match(/BlackBerry/i);
  },
  iOS: function() {
      return navigator.userAgent.match(/iPhone|iPad|iPod/i);
  },
  Opera: function() {
      return navigator.userAgent.match(/Opera Mini/i);
  },
  Windows: function() {
      return navigator.userAgent.match(/IEMobile/i);
  },
  any: function() {
      return (
          isMobile.Android() || 
          isMobile.BlackBerry() || 
          isMobile.iOS() || 
          isMobile.Opera() || 
          isMobile.Windows());
  }
};

if(isMobile.any() ) {
document.body.classList.add('_touch');

let menuArrows = document.querySelectorAll('.menu__arrowa');
if (menuArrows.length > 0) {
  for (let index = 0; index < menuArrows.length; index++) {
      const menuArrow = menuArrows[index];
      menuArrow.addEventListener("click", function (e) {
          menuArrow.parentElement.classList.toggle('_active');
      });
  }
}

} else {
  document.body.classList.add('_pc');
}


const iconMenu = document.querySelector('.menu__icona');
if (iconMenu) {
  const menuBody = document.querySelector('.menu__bodya');
  iconMenu.addEventListener("click", function (e) {
      document.body.classList.toggle('_lock');
      iconMenu.classList.toggle('_active');
      menuBody.classList.toggle('_active');
  });
}