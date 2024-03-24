const nameBook = document.querySelector("span#bookValue").outerText;
const apiGetEndpoint = `https://www.googleapis.com/books/v1/volumes?q=${nameBook}&key=AIzaSyCsk64sineil4IZ_Mj80b0cMxPOm0T-r7w`;

fetch(apiGetEndpoint)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        const show = document.querySelector("div#showBooksFetch");
        let array = 1000;
        for (let index = 0; index < array; index++) {
            show.innerHTML += `
            <div class="col-sm-3 text-center bg-light pt-3 my-2 mx-3 rounded">
                <img width="90" class="img-fluid" src="${data.items[index].volumeInfo.imageLinks.thumbnail}" alt="img">
                <p class="lead">
                    ${data.items[index].volumeInfo.title}
                </p>
            </div>`;
        }
        // show.innerHTML = `
        //     <div class="col-md-2 text-center bg-light pt-3 rounded">
        //         <img class="img-fluid" src="${data.items[0].volumeInfo.imageLinks.thumbnail}" alt="img">
        //         <p class="fs-5">
        //             ${data.items[0].volumeInfo.title}
        //         </p>
        //     </div>`;
    });
