$(function() {

  // 設定變數
  // $el=>被click展開的<dt>, $parentCol=>$el的parent的parent也就是info-col, $otherCols是沒有展開的info-col
  // $allDt預設是所有的<dt>, $allCells預設是所有的<dd>
  var $el, $parentCol, $otherCols, 
      $allDt = $("dt"),
      $allCells = $("dd");
    
  $("#page-wrap a.image").on("click", function(e) { 
        
        if ( !$(this).parent().hasClass("curCol") ) {         
            e.preventDefault(); 
            $(this).next().find('dt:first').click(); 
        } 
        
    });
    
  $("#page-wrap dt").on("click", function() {
        
        $el = $(this);
        
        if (!$el.hasClass("current")) {
        
      $parentCol = $el.parent().parent();
      $otherCols = $(".info-col").not($parentCol);
            
            // remove current cell from selection of all cells
      $allDt = $("dt").not(this);
            
            // close all info cells
            $allCells.slideUp();
            
            // return all titles (except current one) to normal size
      $allDt.animate({
        fontSize: 15
            });
            
            // animate current title to larger size            
      $el.animate({"font-size": "20px"}).next().slideDown();
            
            // make the current column the large size
      $parentCol.animate({width: '40%'}).addClass("curCol");
            
            // make other columns the small size
      $otherCols.animate({width: '15%'}).removeClass("curCol");
            
            // make sure the correct column is current
      $allDt.removeClass("current");
            $el.addClass("current");  
        
        }
        
    });
    
    $("#starter").trigger("click");
    
});