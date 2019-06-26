$('form').on('submit', function(event) {
            $('#loader').fadeIn();
            $("#a").blur();
            setTimeout(function() {
                $('form')[0].submit();
            }, 1);
            event.preventDefault();
            return false;
        });    
    
