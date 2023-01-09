const lightbox = document.createElement("div")
lightbox.id = "lightbox"
document.body.appendChild(lightbox)

const images = document.querySelectorAll("img")
images.forEach(image => {
    image.addEventListener("click", (e) => {
        lightbox.classList.add("active")
        const img = document.createElement("img")
        img.src = image.src
        while (lightbox.firstChild) {
            lightbox.removeChild(lightbox.firstChild)
        }
        lightbox.appendChild(img)
    })
})

lightbox.addEventListener("click", (e) => {
    if (e.target !== e.currentTarget) return
    lightbox.classList.remove("active")
})

const artModal = new bootstrap.Modal(document.getElementById("artModal"));

htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id == "modal-dialog") {
        artModal.show();
    }
});

htmx.on("htmx:beforeSwap", (e) => {
    if (e.detail.target.id == "modal-dialog" && !e.detail.xhr.response) {
        artModal.hide();
        e.detail.shouldSwap = false;
    }
});

htmx.on("hidden.bs.modal", () => {
    document.getElementById("modal-dialog").innerHTML = "";
    location.reload();
});