require("dotenv").config();

const apiGetResponse =
    "https://www.googleapis.com/books/v1/volumes?q=flowers&filter=free-ebooks&key=yourAPIKey";

console.log(process.env.KEY);
