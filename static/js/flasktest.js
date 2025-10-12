const checkbox1 = document.getElementById('checkbox1');
const textbox1 = document.getElementById('textbox1');

checkbox1.addEventListener('change', function() {
    if (checkbox1.checked) {
        textbox1.disabled = false;
    } else {
        textbox1.disabled = true;
    }
});