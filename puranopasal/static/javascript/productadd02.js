

document.getElementById("prdtcost").addEventListener("submit", async function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll(".errorprd").forEach(el => el.innerText = "");

    const formData = new FormData(this);
        // Include the clicked submit button

    const response = await fetch(this.action, {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
        },
        body: formData
    });

    const data = await response.json();

if (data.error) {
    for (const [field, msg] of Object.entries(data.error)) {
        const errorDiv = document.getElementById(field + "_errorprd");
        if (errorDiv){
            errorDiv.innerHTML = '<i class="fas fa-exclamation-triangle"></i> ' + msg;
        }
        
    }
}
     else {
        if (data.success) {
            //  THIS is where you redirect
            window.location.href = data.redirect;
        }

        this.reset();
    }
});



