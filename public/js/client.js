const socket = io.connect();

$(() => {
    //*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    //*                                                        WEBPAGE CONTROL
    // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    $('#header').on('click', 'a', (e) => {
        if (e.target.id == 'link-register') {
            $('#div-register').show();
        }
    });

    $('#div-register').on('click', 'input', (e) => {
        if (e.target.id == 'btn-register') {
            socket.emit('registration', {
                username: $('#register-username').val(),
                password: $('#register-password').val()
            })
        }
    });


    //*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    //*                                                              SOCKET.IO
    // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    socket.on('username_taken', () => {
        alert('Username is taken.');
    });

    socket.on('registered', () => {
        $('#div-register').hide();
    });
});
