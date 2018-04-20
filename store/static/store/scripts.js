$('.add-to-cart-form').on('submit', function (event) {
  event.preventDefault()
  $.ajax({
    url: $(this).attr('add-to-cart-url'),
    data: $(this).serialize(),
    dataType: 'json',
    success: function (data) {
      $('#sum').text(data.sum)
    }
  })
})

$(document).ready(function() {
  $('a[href="' + location.pathname + '"]').addClass('active')
});