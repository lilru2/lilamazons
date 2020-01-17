const socket = io.connect();

$(() => {
    //*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    //*                                                        WEBPAGE CONTROL
    // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    $('#header').on('click', 'a', (e) => {
        if (e.target.id == 'link-register') {
            $('#div-login').hide();
            $('#div-register').show();
        }
        else if (e.target.id == 'link-login') {
            $('#div-register').hide();
            $('#div-login').show();
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

    $('#div-login').on('click', 'input', (e) => {
        if (e.target.id == 'btn-login') {
            socket.emit('login', {
                username: $('#login-username').val(),
                password: $('#login-password').val()
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

    socket.on('no_such_user', () => {
        alert('No such user.');
    });
});
