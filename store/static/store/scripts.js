$('#itemlist').on('submit', '.add-to-cart-form', function (event) {
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