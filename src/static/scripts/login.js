document.addEventListener("DOMContentLoaded", function() {
    var messages = document.querySelectorAll('.mess');
    
    messages.forEach(function(message) {
        setTimeout(function() {
            message.classList.add('fade-out');
            setTimeout(function() {
                message.style.display = 'none';
            }, 1000);
        }, 3000);
    });
});