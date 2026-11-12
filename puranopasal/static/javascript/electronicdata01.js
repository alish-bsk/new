function sendEelct() {
    fetch("{% url 'elect' %}", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ laptop: "1" })
    })
    .then(res => res.json())
    .then(data => console.log(data));
}