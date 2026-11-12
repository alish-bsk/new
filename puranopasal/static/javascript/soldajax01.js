document.getElementById("solderror").addEventListener("submit", async function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll(".errorprd").forEach(el => el.innerText = "");

    const formData = new FormData(this);
        // Include the clicked submit button
        if (event.submitter?.name) {
            formData.set(
                event.submitter.name,
                event.submitter.value
            );
        }

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
        const errorDiv = document.getElementById(field + "_errorprd");
        if (field==="successname"){
            errorDiv.innerHTML =   msg;
        }
        if (field==="deletename"){
            errorDiv.innerHTML =   msg;
        }

        else{
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



