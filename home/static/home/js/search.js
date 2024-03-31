const nameBook = document.querySelector("span#bookValue").outerText;
const key = response.API_BOOK_KEY;
const apiGetEndpoint = `https://www.googleapis.com/books/v1/volumes?q=${nameBook}&key=${key}`;
const erroImg =
    "https://i.pinimg.com/564x/a2/9f/64/a29f6458abfb132920fb8a99d8b60f85.jpg";

fetch(apiGetEndpoint)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        const show = document.querySelector("div#showBooksFetch");
        show.innerHTML = "";
        let array = data.items.length;
        for (let index = 0; index < array; index++) {
            try {
                let book_name = data.items[index].volumeInfo.title;
                let book_img =
                    data.items[index].volumeInfo.imageLinks.thumbnail;
                let author = data.items[index].volumeInfo.authors;
                let description = data.items[index].volumeInfo.description;
                let categories = data.items[index].volumeInfo.categories;
                show.innerHTML += `
                    <button 
                        class="col-sm-3 text-center bg-light pt-3 my-2 mx-3 rounded btn"
                        data-bs-toggle="modal" 
                        data-bs-target="#exampleModal"
                        onclick="setBook('${book_img}', '${book_name}', '${categories}', '${author}', '${description}')"
                    >
                        <img class="img-fluid" src="${book_img}" alt="img">
                        <p class="lead">
                            ${book_name}
                        </p>
                    </button>`;
            } catch (error) {
                let book_name = data.items[index].volumeInfo.title;
                let author = data.items[index].volumeInfo.authors;
                let description = data.items[index].volumeInfo.description;
                let categories = data.items[index].volumeInfo.categories;
                show.innerHTML += `
                    <button
                        class="col-sm-3 text-center bg-light pt-3 my-2 mx-3 rounded btn"
                        data-bs-toggle="modal" 
                        data-bs-target="#exampleModal"
                        onclick="setBook('${erroImg}', '${book_name}', '${categories}', '${author}', '${description}')"
                    >
                        <img class="img-fluid" width="180" src="${erroImg}" alt="img-book">
                        <p class="lead">
                            ${book_name}
                        </p>
                    </button>`;
            }
        }
    });

function setBook(
    img_path,
    name_book,
    categorie,
    author = "autor não informado",
    description = "descrição não informada"
) {
    const text_set = document.querySelector("div#modal-body-text");
    text_set.innerHTML = `
        <div class="col-md-4" >
            <img class="img-fluid" width="200" src="${img_path}">
        </div>
        <div class="col-md-8" >
            <h3>
                ${name_book}
            </h3>
            <div>
                <p>
                    ${author}
                </p>
                <p>
                    ${categorie}
                </p>
                <p>
                    ${description}
                </p>
            </div>
        </div>
    `;
}
