$('.add-to-cart-form').on('submit', function (event) {
  event.preventDefault()
  $.ajax({
    url: $(this).attr('add-to-cart-url'),
    data: $(this).serialize(),
    dataType: 'json',
    success: function (data) {
      $('#sum').text(data.sum)
      $("#add-success").text(`Added ${data.item} (${data.count}) to cart.`)
      $("#add-success").fadeTo(4000, 500).slideUp(500)
    }
  })
})

$('delete-from-cart-btn').on('click', function () {
  $('#remove-success').text('')
})

$(document).ready(function () {
  $('#add-success').hide()
  $('a[href="' + location.pathname + '"]').addClass('active')
  setTimeout(() => {
    $('#remove-success').slideUp(500)
  }, 4000);
});