
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("user-add");
    const productList = document.getElementById("product_listprdt");

    if (!form || !productList) {
        console.error("Form or product_listprdt not found.", {
            form,
            productList
        });
        return;
    }

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        // Include the clicked button value: All, Sold, or Expire
        if (e.submitter?.name) {
            formData.set(e.submitter.name, e.submitter.value);
        }

        console.log("Submitting to:", form.action);
        console.log("Selected button:", formData.get("prdtads"));


        try {
            // Get the CSRF token from the form
            let csrfInput = form.querySelector(
                '[name="csrfmiddlewaretoken"]'
            );

            // Fallback: search the entire page
            if (!csrfInput) {
                csrfInput = document.querySelector(
                    '[name="csrfmiddlewaretoken"]'
                );
            }

            if (!csrfInput) {
                throw new Error(
                    "CSRF token not found. Check {% csrf_token %} in your Django template."
                );
            }

            const csrfToken = csrfInput.value;

            const response = await fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "X-Requested-With": "XMLHttpRequest"
                },
                body: formData
            });

            console.log("HTTP status:", response.status);

            const responseText = await response.text();
            console.log("Raw Django response:", responseText);

            if (!response.ok) {
                throw new Error(
                    `HTTP ${response.status}: ${responseText.slice(0, 500)}`
                );
            }

            let data;

            try {
                data = JSON.parse(responseText);
            } catch {
                throw new Error(
                    "Django did not return valid JSON. Check the console."
                );
            }

            console.log("Parsed JSON:", data);

            if (data.success === true) {
                const products = data.products || [];

productList.innerHTML = products.map(product => {
    return `
            <div class="card cardall-laptop  h-extra  laptop-cardgrp" >

            <a href="${productInfoUrl}?id=${product.product_id}">
                    <img src="${ product.image }" class="card-img-top img-fluid  laptop-cardimg" alt="image">
                </a>

            <a href="${productInfoUrl}?id=${product.product_id}"
                   class="h5 text-dark text-center mt-5 text-decoration-none card-name d-block">
                    ${ product.model_name }
                </a>

                <p class="h5  text-center text-body-tertiary mb-3 ">
                    RS ${ product.price }
                </p>
                <p class="h5  text-center text-body-tertiary mb-3 ">
                    Id: ${ product.product_id }
                </p>


            </div>
    `;
}).join("") ;

            } else {
                productList.textContent =
                    data.message || "Django returned success: false.";
            }

        } catch (error) {
            console.error("AJAX error:", error);
            productList.textContent = error.message;
        }
    });
});

