
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("user-ads");
    const productList = document.getElementById("product_list");

    if (!form || !productList) {
        console.error("Form or product_list element not found.");
        return;
    }

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        console.log("Form intercepted by JavaScript");

        const formData = new FormData(form);

        // Send the clicked button's value
        if (e.submitter?.name) {
            formData.set(e.submitter.name, e.submitter.value);
        }

        try {
            const response = await fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": form.querySelector(
                        '[name="csrfmiddlewaretoken"]'
                    ).value
                },
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }

            const data = await response.json();
            console.log("Django response:", data);

            if (data.success) {
                const products = data.prdsl || [];

                productList.innerHTML = products.map(product => {
                    const productUrl =
                        `/product-info/?id=${encodeURIComponent(product.product_id)}`;

                    return `
                        <div class="card p-2" style="width: 200px;">
                            <a href="${productUrl}">
                                <img
                                    src="/media/${escapeHtml(product.image)}"
                                    class="card-img-top"
                                    alt="${escapeHtml(product.model_name)}">
                            </a>

                            <div class="card-body">
                                <h5>${escapeHtml(product.model_name)}</h5>
                                <p>Rs. ${escapeHtml(product.price)}</p>
                                <p>Product ID: ${escapeHtml(product.product_id)}</p>
                            </div>
                        </div>
                    `;
                }).join("") || "<p>No products found.</p>";
            } else {
                console.error("Request failed:", data.message || data.errors);
            }
        } catch (error) {
            console.error("Error loading products:", error);
        }
    });
});

function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, char => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[char]);
}
