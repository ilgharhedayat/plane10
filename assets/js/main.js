(function($){
	"use strict";
	jQuery(document).on('ready', function () {

        // Partner Slides
		$('.partner-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
            rtl: true,
			autoplayHoverPause: true,
            autoplay: true,
            margin: 30,
            navText: [
                "<i class='flaticon-left-chevron'></i>",
                "<i class='flaticon-right-chevron'></i>"
            ],
			responsive: {
                0: {
                    items: 1,
                },
                576: {
                    items: 1,
                },
                768: {
                    items: 1,
                },
                1200: {
                    items: 1,
				}
            }
        });

    });
}(jQuery));

$(document).ready(function() {
              
    /* Centering the modal vertically */
    function alignModal() {
        var modalDialog = $(this).find(".modal-dialog");
        modalDialog.css("margin-top", Math.max(0, 
        ($(window).height() - modalDialog.height()) / 2));
    }
    $(".modal").on("shown.bs.modal", alignModal);

    /* Resizing the modal according the screen size */
    $(window).on("resize", function() {
        $(".modal:visible").each(alignModal);
    });
});
$(document).ready(function(){
	$('#nav-icon').click(function(){
		$(this).toggleClass('open');
	});
    /* new codes */
    $(".side-tab .text-body").click(function(event){
        event.preventDefault();
        let dataTab = $(this).data("tab");
        $(".text-body span").css("background-color","transparent")
        $(this).children('span').css("background-color","#b6b6b6");
        $(".select-area").addClass("d-none");
        $("."+dataTab).removeClass("d-none");
    })
    $("#returnDateHotel").persianDatepicker({
        altField: '#returnDateHotel',
        altFormat: "YYYY/MM/DD",
        observer: false,
        format: 'YYYY/MM/DD',
        initialValue: false,
        initialValueType: 'persian',
        autoClose: true,
        });
    $("#goDateHotel").persianDatepicker({
        altField: '#goDateHotel',
        altFormat: "YYYY/MM/DD",
        observer: false,
        format: 'YYYY/MM/DD',
        initialValue: false,
        initialValueType: 'persian',
        autoClose: true,
    });
    $("#hotelSrc").focus(function(){
        fetch('http://localhost/php/plane/cities.json')
        .then(res => res.json())
        .then(data => getDataFromJson(data))
        function getDataFromJson(data){
            let dataCitie = data;
            let selectElemnt = document.getElementById("hotelSrc")
            dataCitie.forEach(function(value){
                selectElemnt.innerHTML +="<option value='"+value['id']+"'>"+value['title']+"</option>";
            })
        }
    })
});
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.querySelector('#mNav').style.backgroundColor="#237c8c"
 }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0"
    document.querySelector('#mNav').style.backgroundColor="#1DBBD8"
}
function rangeValFunc(rangeVal){
    let rangeWidth1 = document.getElementById("Tooltiptext1").textContent =rangeVal + ":00";
}