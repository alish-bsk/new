document.getElementById("user-add").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = this;
    const formData = new FormData(form);
    const errorDiv = document.getElementById("product_list");

    // Include the clicked submit button
    if (e.submitter?.name) {
        formData.set(e.submitter.name, e.submitter.value);
    }

    // Get CSRF token from the form
    const csrfToken = form.querySelector(
        "[name=csrfmiddlewaretoken]"
    )?.value;

    try {
        const response = await fetch(form.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken
            },
            body: formData
        });

        // Parse the server response
        const data = await response.json();

        console.log("Server response:", data);

        // Display server-side errors
        if (data.error) {
            if (errorDiv) {
                const errors = data.error;

                if (typeof errors === "object" && errors !== null) {
                    errorDiv.textContent = Object.entries(errors)
                        .map(([field, msg]) => {
                            const message = Array.isArray(msg)
                                ? msg.join(", ")
                                : String(msg);

                            return field === "message"
                                ? message
                                : `${field}: ${message}`;
                        })
                        .join("\n");
                } else {
                    errorDiv.textContent = String(errors);
                }
            }

            return;
        }

        // Handle HTTP errors
        if (!response.ok) {
            if (errorDiv) {
                errorDiv.textContent =
                    data.message || `Request failed: ${response.status}`;
            }
            return;
        }

        // Redirect on success
        if (data.success) {
            if (data.redirect) {
                window.location.href = data.redirect;
            } else if (errorDiv) {
                errorDiv.textContent = data.message || "Success!";
            }

            return;
        }

        // Handle unexpected response
        console.log("Unexpected response:", data);

        if (errorDiv) {
            errorDiv.textContent = "An unexpected response was received.";
        }

    } catch (error) {
        console.error("Request failed:", error);

        if (errorDiv) {
            errorDiv.textContent =
                "Something went wrong. Please try again.";
        }
    }
});
