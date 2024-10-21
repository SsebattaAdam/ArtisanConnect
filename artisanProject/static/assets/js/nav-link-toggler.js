/*---------- Mobile-Navbar Nav Toggler ----------*/

$(document).ready(function(){

  $(".nav-link > .main-nav-link").click(function() {
    // Close all main-nav-links in sibling nav-links
    $(this).closest('.nav-link').siblings().find('.main-nav-link').removeClass("active").next(".sub-nav-link").removeClass("active").slideUp();
    // Update icons to "fa-plus" for all main-nav-links in sibling nav-links
    $(this).closest('.nav-link').siblings().find('.main-nav-link i').removeClass("fa-minus").addClass("fa-plus");
  
    // Toggle "active" class for the clicked main-nav-link
    $(this).toggleClass("active");
    // Toggle slide for the corresponding sub-navigation
    $(this).next(".sub-nav-link").toggleClass("active").slideToggle();
    // Toggle icon class for the clicked main-nav-link
    $(this).find("i").toggleClass("fa-minus fa-plus");
    
  });
  
  

}); 
