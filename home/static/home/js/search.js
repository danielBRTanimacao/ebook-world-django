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
            show.innerHTML += `
            <a href="/${data.items[index].id}/${data.items[index].volumeInfo.title}/book/" class="col-sm-3 text-center bg-light pt-3 my-2 mx-3 rounded text-dark text-decoration-none">
                <img class="img-fluid" src="${data.items[index].volumeInfo.imageLinks.thumbnail}" alt="img">
                <p class="lead">
                    ${data.items[index].volumeInfo.title}
                </p>
            </a>`;
        }
    });
