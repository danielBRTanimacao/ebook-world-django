const nameBook = document.querySelector("span#bookValue").outerText;
const apiKey = "AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w";
const apiGetEndpoint =
    "https://www.googleapis.com/books/v1/volumes?q=" +
    nameBook +
    "&key=" +
    apiKey;
fetch(apiGetEndpoint)
    .then((response) => {
        response.json();
    })
    .then((data) => {
        console.log(data);
        const show = document.querySelector("div#showBooksFetch");
        show.innerHTML = data;
    });

console.log(apiGetEndpoint);
