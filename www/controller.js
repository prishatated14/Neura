$(document).ready(function () {
    // Display speak message
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message); // Update the first <li> element with the message
        $('.siri-message').textillate('start'); // Restart the textillate animation
    }

    // Display Hood
    eel.expose(ShowHood);
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true); // Ensure the ID matches exactly (case-sensitive)
    }
});