var $sw = jQuery.noConflict();

$sw(window).on('load resize scroll',function(e){
	"use strict";
	var $gallery_li = $sw('.spcard');
   $gallery_li.each(function () {
      if (isScrolledIntoView(this) === true) {
          $sw(this).addClass('in-view')
      }
   });
});


function isScrolledIntoView(elem) {
	"use strict";
    var docViewTop = $sw(window).scrollTop();
    var docViewBottom = docViewTop + $sw(window).height();

    var elemTop = $sw(elem).offset().top;
    var elemBottom = elemTop + $sw(elem).height();
    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}