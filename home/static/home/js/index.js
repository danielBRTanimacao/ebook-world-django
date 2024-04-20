let slideIndex = 0;

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    setTimeout(showSlides, 3000);
}

showSlides();

function onScreenMinus() {
    const text = document.querySelector("div#visible-img");
    const col_interact = document.querySelector("#colum");

    var screen_height = window.innerWidth;
    if (screen_height <= 1199.98) {
        text.innerHTML = " ";
        col_interact.classList.remove("col-lg-6");
        text.classList.remove("col-lg-6");
    } else {
        col_interact.classList.add("col-lg-6");
        text.classList.add("col-lg-6");
        text.innerHTML = `
            <img 
            class="img-fluid rounded"
            src="https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=1798&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" 
            alt="img-teste"
            >
        `;
    }
}

onScreenMinus();
window.addEventListener("resize", onScreenMinus);

function animateImgs(classItem) {
    const watching = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add(classItem);
            } else {
                entry.target.classList.remove(classItem);
            }
        });
    });

    const hiddenClass = document.querySelectorAll(".hidden");
    const hiddenImgClass = document.querySelectorAll(".hidden-img");

    hiddenClass.forEach((e) => watching.observe(e));
    hiddenImgClass.forEach((e) => watching.observe(e));
}

animateImgs("showing");
animateImgs("upimg");
