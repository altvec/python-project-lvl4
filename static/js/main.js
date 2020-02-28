$(document).ready(function () {
  $(".card").hover(
    function () {
      $(this).addClass('shadow-sm').css('cursor', 'pointer');
    },
    function() {
      $(this).removeClass('shadow-sm');
    }
  )
});

// Add active attribute to highlight currently active page
$(function() {
  const current = location.pathname;
  $('.nav-link').each(function() {
    const $this = $(this);
    if ($this.attr('href') == current) {
      $this.addClass('active');
    }
  });
});
