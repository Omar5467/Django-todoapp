$(document).ready(function() {
    $('.edit_b').hide();

    // alert('checked');
    $('.titlein').hide();

    // When the checkbox state changes
    $('.check').change(function() {
        // alert('checked');
        // If the checkbox is checked
        var checkboxId = $(this).attr('id');
        if ($(this).is(':checked')) {
            
            $(this).parent().find('label[for="' + checkboxId + '"]').css('text-decoration', 'line-through');

        } else {
            
            $(this).parent().find('label[for="' + checkboxId + '"]').css('text-decoration', 'none');
            // $(this).parent().find('label[for="check"]').css('text-decoration', 'none');
        }
    });

    $(".edit_a").click(function(){
        $(this).parent().find('.edit_b').show();
        $(this).parent().find('.titlein').show();
        $(this).parent().find('.edit_a').hide();
    })

    
});
