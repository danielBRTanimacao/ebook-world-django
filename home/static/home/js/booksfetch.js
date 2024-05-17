const nameBook = "tecnologia";
const key = "AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w";
const apiGetEndpoint = `https://www.googleapis.com/books/v1/volumes?q=${nameBook}&key=${key}`;

fetch(apiGetEndpoint)
    .then((response) => response.json())
    .then((data) => {
        const lanc = document.querySelector("div#lanc");
        array = data.items.length;
        for (let index = 0; index < array.length; index++) {
            let book_img = data.items[index].volumeInfo.imageLinks.thumbnail;
            lanc.innerHTML += `
                <img src="${book_img}" alt="${book_img}">
            `;
        }
        console.log(data);
    });
