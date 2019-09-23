function w3_open() {  document.getElementById("mySidebar").style.display = "block";  }
function w3_close() {  document.getElementById("mySidebar").style.display = "none";  }

$(document).ready(function(){
  //當手機版時，調整header的高度
  function setHeaderHeight(){
    if( $('#showMenu').is(':visible') ){
      var targetHeight = $('header .logo').innerHeight();
      $('header .container').css('height',targetHeight);
      var targetmt = ($('header .container').innerHeight()-$('#showMenu').outerHeight())/2;
      $('#showMenu').css('margin-top', targetmt);
      var targetRight = $('#showMenu').innerWidth()+10;
      var targetTop = ($('header .container').innerHeight()-$('.shareBtnArea').innerHeight())/2;
      $('.shareBtnArea').css('right',targetRight).css('top',targetTop);
      $('.shareBtnArea a').css('margin',0);
    }
  }
  setHeaderHeight();
  $(window).resize(function(){
    setHeaderHeight();
  });
});