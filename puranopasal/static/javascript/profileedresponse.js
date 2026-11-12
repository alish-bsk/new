document.getElementById("profileedit").addEventListener("submit", async function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll(".errorprf").forEach(el => el.innerText = "");

    const formData = new FormData(this);

    const response = await fetch(this.action, {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
        },
        body: formData
    });

    const data = await response.json();

if (data.errors) {
    for (const [field, msg] of Object.entries(data.errors)) {
        const errorDiv = document.getElementById(field + "_errorprf");

        if (errorDiv)errorDiv.innerHTML = '<i class="fas fa-exclamation-triangle"></i> ' + msg;
        
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



