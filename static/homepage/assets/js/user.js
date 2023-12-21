$(document).ready(function() {

    $(".dashboard-icon").click(function() {
        const close_popup = $(".d-none");
        if (close_popup.length) {
            $("#use-section").removeClass("d-none")
        } else {
            $("#use-section").addClass("d-none")
        }
    });

});
