$(function() {
    $('#reGister').on('change', function () {
        if ($('#reGister').is(":checked")) {
            $('#submit').attr("value", "Register")
        } else {
            $('#submit').attr("value", "Logic")
        }
    });
    $('#showPwd').on('change', function () {
        if ($('#showPwd').is(":checked")) {
            $('#password').attr("type", "text")
        } else {
            $('#password').attr("type", "password")
        }
    });
    $("form").submit(function () {
        if (($("#username").val() == "") || ($("#password").val()==""))
        {
            Swal.fire({
                title: 'Warning!',
                text: 'Username or Password can not be empty!',
                type: 'warning',
                confirmButtonText: 'Ok',
            });
            event.preventDefault();
        }
    });
    if ($('span').text() !== ''){
        Swal.fire({
                // title: $('span').attr('data-status'),
                text: $('span').text(),
                type: $('span').attr('data-status'),
                confirmButtonText: 'Ok',
            });
        ;
    }
});