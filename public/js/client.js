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
});
