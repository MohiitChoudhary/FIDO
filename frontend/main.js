$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',

        },
        out: {
            effect: 'bounceOut',

        },

    });
    //Siri wave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude	: "1",
        speed: "0.30",
        autostart: true
        

    });
    //siri meessage
     $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true,

        },
        out: {
            effect: 'fadeOutUpt',
            sync: true,

        },


});

    //Mic Event

    $("#MicBtn").click(function () { 
        $("#oval").attr("hidden", true);
         $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });
    
function doc_keyUp(e) {
    // On Mac: metaKey = Command ⌘
    if (e.key.toLowerCase() === 'j' && e.metaKey) {
        eel.playAssistantSound();
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands(); // just call, no need for ()()
    }
}

document.addEventListener('keyup', doc_keyUp, false);


function PlayAssistant(message){
    
    if(message != ""){

        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands(message);
        $("#chatbox").val("");
        $("#MicBtn").attr("hidden", false);
        $("#SendBtn").attr("hidden", true);
    }
}
    function ShowHideButton(message) {
        if(message.length == 0 ){
        $("#MicBtn").attr("hidden", false);
        $("#SendBtn").attr("hidden", true);
        }
        else{
        $("#MicBtn").attr("hidden", true);
        $("#SendBtn").attr("hidden", false);
        }
    }

    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message);
    });

    $("#SendBtn").click(function () {

        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

     $("#chatbox").on("keypress", function(e) {
        if (e.key === "Enter" || e.which === 13) {
            e.preventDefault();
            let message = $("#chatbox").val().trim();
            if (message.length > 0) {
                PlayAssistant(message);
            }
        }
    });

   


});