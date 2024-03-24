const nameBook = document.querySelector("span#bookValue").outerText;
const apiGetEndpoint =
    "https://www.googleapis.com/books/v1/volumes?q=" +
    nameBook +
    "&key=AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w";

fetch(apiGetEndpoint)
    .then((response) => {
        console.log(response);
        console.log(response.json());
        response.json();
    })
    .then((data) => {
        console.log(data);
        const show = document.querySelector("div#showBooksFetch");
        show.innerHTML = data;
    });
