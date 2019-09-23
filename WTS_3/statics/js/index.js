$(document).ready(function(){
  //上方 Slider =====================================================
  $('.TS_slider').slick({
    autoplay: true,
    dots: true
  });
  //下方 Carousel 效果的 Slider ======================================
  $('.news_slider').slick({
    autoplay: true,
    dots: false,
    vertical: true,
    slidesToShow: 3,
    slidesToScroll: 1
  });
  //負責中央下方 Tabs 功能的設計========================================
  //一開始找到每個.tabs對應到.current標籤的內容淡入顯示--------------------
  $('.tabs').each(function(i,obj){
    var no = $(this).children('ul').children('.current').index();
    // console.log(no);
    $(this).children('div').children('div').eq(no).fadeIn();
  });
  //滑鼠滑入標籤時對應顯示內容-------------------------------------------
  $('.tabs>ul>li').hover(function(){
    //先移除目前這一組.tabs中所有<li>的current類別名稱=>滑入的<li>加上current類別名稱
    $(this).parents('.tabs').find('li').removeClass('current');
    $(this).addClass('current');
    //目前這一組.tabs中所有第二層的<div>淡出=>對應滑入標籤的內容(第二層div)淡入顯示
    var obj = $(this).parents('.tabs').children('div').children('div');
    $(obj).fadeOut();
    $(obj).eq($(this).index()).fadeIn();
  });
});