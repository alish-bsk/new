
document.getElementById("profileedit").addEventListener("submit", async function (e) {
    e.preventDefault();

    document.querySelectorAll(".errorprf").forEach(el => {
        el.innerHTML = "";
    });

    const formData = new FormData(this);

    try {
        const response = await fetch(this.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": document.querySelector(
                    "[name=csrfmiddlewaretoken]"
                ).value
            },
            body: formData
        });

        const data = await response.json();

        if (data.errors) {
            for (const [field, msg] of Object.entries(data.errors)) {
                const errorDiv = document.getElementById(
                    field + "_errorprf"
                );
                console.log(errorDiv);

                if (errorDiv) {
                    errorDiv.innerHTML =
                        '<i class="fas fa-exclamation-triangle"></i> ' + msg;
                } else {
                    console.warn("Missing error element:", field + "_errorprf");
                }
            }

            return; // Do not reset the form
        }

        if (!response.ok) {
            alert(data.message || "Request failed.");
            return;
        }

        if (data.success && data.redirect) {
            window.location.href = data.redirect;
            return;
        }

    } catch (error) {
        console.error("Submission failed:", error);
        alert("An error occurred while submitting the form.");
    }
});
