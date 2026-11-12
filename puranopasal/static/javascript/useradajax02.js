const form = document.getElementById("user-ads");

form.addEventListener("submit", async function (e) {
    e.preventDefault();

    console.log("Form intercepted by JavaScript");

    const formData = new FormData(this);

    if (e.submitter?.name) {
        formData.set(e.submitter.name, e.submitter.value);
    }

    const response = await fetch(this.action, {
        method: "POST",
        headers: {
            "X-CSRFToken": form.querySelector(
                '[name="csrfmiddlewaretoken"]'
            ).value
        },
        body: formData
    });

    const data = await response.json();

    console.log(data);

    if (data.success) {
        document.getElementById("product_list").innerHTML =
            data.prdsl.map(product => `
                <div class="card p-2" style="width: 200px;">
                    <img src="/media/${escapeHtml(product.image)}"
                         class="card-img-top"
                         alt="${escapeHtml(product.model_name)}">

                    <div class="card-body">
                        <h5>${escapeHtml(product.model_name)}</h5>
                        <p>Rs. ${escapeHtml(product.price)}</p>
                        <p>Product ID: ${escapeHtml(product.product_id)}</p>
                    </div>
                </div>
            `).join("");
    }
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





