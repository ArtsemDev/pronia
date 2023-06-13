$('form#contact-form').on('submit', function (e) {
    e.preventDefault()
    $.ajax({
        url: '/api/contact',
        contentType: 'application/json',
        dataType: 'json',
        method: 'post',
        data: JSON.stringify({
            name: this.name.value,
            email: this.email.value,
            message: this.message.value
        })
    }).done(function (data) {
        document.querySelector('form#contact-form').querySelector('input#name').value = ''
        document.querySelector('form#contact-form').querySelector('input#email').value = ''
        document.querySelector('form#contact-form').querySelector('textarea#message').value = ''
    })
})