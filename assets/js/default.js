//Script for homepage dynamics
$(document).ready(function () {
    // Add smooth scrolling to all links in navbar + footer link
    $(".navbar a, footer a[href='#myPage']").on('click', function (event) {
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 900, function () {

                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
            });
        } // End if
    });

    $(window).scroll(function () {
        $(".slideanim").each(function () {
            var pos = $(this).offset().top;

            var winTop = $(window).scrollTop();
            if (pos < winTop + 600) {
                $(this).addClass("slide");
            }
        });
    });
})

//Ajax for contact form submission and modal
$(document).on('submit', '#contactForm', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            name: $('#name').val(),
            email: $('#email').val(),
            message: $('#comments').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {
            $('#modalSuccess').modal('show');
            $('input[type=text], textarea, input[type=email]').val('');
        },
        error: function (xhr, textStatus, errorThrown) {
            $('#modalFail').modal('show');
        },
    });
});