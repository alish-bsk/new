document.getElementById("user-ads").addEventListener("submit", async function(e) {
    e.preventDefault();

    const form = this;
    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": document.querySelector(
                    "[name=csrfmiddlewaretoken]"
                ).value
            },
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        if (data.success) {
            // Redirect if the server provides a redirect URL
            if (data.redirect) {
                window.location.href = data.redirect;
                return;
            }

            // Display products if the server returns them
            if (data.prdsl) {
                let html = "";

                for (const slpd of data.prdsl) {
                    const productUrl =
                        `/product-info/?id=${encodeURIComponent(slpd.product_id)}`;

                    html += `
                        <div class="card cardall-laptop h-extra laptop-cardgrp">

                            <a href="${productUrl}">
                                <img src="${escapeHtml(slpd.image)}"
                                     class="card-img-top img-fluid w-extra h-extra laptop-cardimg"
                                     alt="${escapeHtml(slpd.model_name)}">
                            </a>

                            <a href="${productUrl}"
                               class="h5 text-dark text-center mt-5 text-decoration-none card-name d-block">
                                ${escapeHtml(slpd.model_name)}
                            </a>

                            <p class="h5 text-center text-body-tertiary mb-3">
                                RS ${escapeHtml(slpd.price)}
                            </p>

                            <p class="h5 text-center text-body-tertiary mb-3">
                                ${escapeHtml(slpd.product_id)}
                            </p>

                        </div>
                    `;
                }

                document.getElementById("product_list").innerHTML =
                    html || "<p>No products found.</p>";
            }

            form.reset();

        } else {
            // Handle validation errors returned by Django
            console.log(data.errors || data.message || "Submission failed");
        }

    } catch (error) {
        console.error("Error:", error);
    }
});

