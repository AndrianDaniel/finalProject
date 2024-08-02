function buyButtonClicked(productId, productName, productDescription, productPrice, productPicture) {

    // Setăm valoarea câmpului ascuns din modalul buyModal
    const hiddenInput = document.querySelector('#buyModal #buyProductId');
    if (hiddenInput) {
        hiddenInput.value = productId;
    }

    const textProductName = document.querySelector('#buyModal #buyProductName');
    if (textProductName) {
        textProductName.innerText = productName
    }

    const textProductDescription = document.querySelector('#buyModal #buyProductDescription');
    if (textProductDescription) {
        textProductDescription.innerText = productDescription
    }

    const textProductPrice = document.querySelector('#buyModal #buyProductPrice');
    if (textProductPrice) {
        textProductPrice.innerText = productPrice
    }

    const imgProductPicture = document.querySelector('#buyModal #buyProductPicture');
    if (imgProductPicture) {
        if (productPicture) {
            imgProductPicture.src = window.location.origin + "/media/" + productPicture;
        } else {
            imgProductPicture.src = window.location.origin + "/static/images/img.png"
        }
    }
}

function exchangeButtonClicked(productId) {
    const hiddenInput = document.querySelector('#exchangeModal #exchangeProductId');
    if (hiddenInput) {
        hiddenInput.value = productId;
    }
}

