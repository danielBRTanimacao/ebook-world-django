const nameBook = document.querySelector("span#bookValue").outerText;
const key = "AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w";
const apiGetEndpoint = `https://www.googleapis.com/books/v1/volumes?q=${nameBook}&key=${key}`;

fetch(apiGetEndpoint)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        const show = document.querySelector("div#showBooksFetch");
        show.innerHTML = "";
        let array = data.items.length;
        for (let index = 0; index < array; index++) {
            try {
                show.innerHTML += `
                    <a href="#" class="col-sm-3 text-center bg-light pt-3 my-2 mx-3 rounded text-dark text-decoration-none">
                        <img class="img-fluid" src="${data.items[index].volumeInfo.imageLinks.thumbnail}" alt="img">
                        <p class="lead">
                            ${data.items[index].volumeInfo.title}
                        </p>
                    </a>`;
            } catch (error) {
                show.innerHTML += `
                    <a href="#" class="col-sm-3 text-center bg-light pt-3 my-2 mx-3 rounded text-dark text-decoration-none">
                        <img class="img-fluid" width="180" src="https://i.pinimg.com/564x/a2/9f/64/a29f6458abfb132920fb8a99d8b60f85.jpg" alt="img-book">
                        <p class="lead">
                            ${data.items[index].volumeInfo.title}
                        </p>
                    </a>`;
            }
        }
    });
