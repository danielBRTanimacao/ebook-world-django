const nameBook = "tecnologia";
const key = "AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w";
const apiGetEndpoint = `https://www.googleapis.com/books/v1/volumes?q=${nameBook}&key=${key}`;

fetch(apiGetEndpoint)
    .then((response) => response.json())
    .then((data) => {
        let lanc = document.querySelector("div#lanc");
        array = data.items.length;
        for (let index = 0; index < array; index++) {
            try {
                lanc.innerHTML += `<img class="img-fluid mx-1" src="${data.items[index].volumeInfo.imageLinks.thumbnail}" alt="book">`;
            } catch (error) {
                lanc.innerHTML += `<img class="img-fluid mx-1" src="https://source.unsplash.com/128x171/?book" alt="book">`;
            }
        }
    });
