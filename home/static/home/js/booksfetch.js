function fetchBook(nameBook, nameRender) {
    const key = "AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w";
    const apiGetEndpoint = `https://www.googleapis.com/books/v1/volumes?q=${nameBook}&key=${key}`;

    fetch(apiGetEndpoint)
        .then((response) => response.json())
        .then((data) => {
            let render = document.querySelector(`div#${nameRender}`);
            array = data.items.length;
            for (let index = 0; index < array; index++) {
                try {
                    render.innerHTML += `<img class="img-fluid mx-1 col-sm-1" src="${data.items[index].volumeInfo.imageLinks.thumbnail}" alt="book">`;
                } catch (error) {
                    render.innerHTML += `<img class="img-fluid mx-1 col-sm-1" src="https://source.unsplash.com/128x171/?book" alt="book">`;
                }
            }
        });
}

renderObjLanc = document.querySelector("div#lanc");
renderObjSearcher = document.querySelector("div#searcher");
renderObjRecomends = document.querySelector("div#recomends");

renderObjLanc.addEventListener("load", fetchBook("tecnologia", "lanc"));
renderObjLanc.addEventListener("load", fetchBook("sobre", "searcher"));
renderObjLanc.addEventListener("load", fetchBook("recomendado", "recomends"));
