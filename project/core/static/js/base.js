    $(document).ready(
        function () {
                $('.commentsdiv').each(function() {
                    $(this).load($(this).attr('data-url'));
                })
        }
    )