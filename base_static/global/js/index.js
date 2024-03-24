function onSubmitBook() {
    require("dotenv").config();
    const nameBook = document.querySelector("input#bookSearch").value;
    const apiKey = process.env.API_BOOK_KEY;
    const apiGetResponse =
        "https://www.googleapis.com/books/v1/volumes?q=" +
        nameBook +
        "&key=" +
        apiKey;
    fetch(apiGetResponse).then((response) => {
        console.log(response);
    });
}
