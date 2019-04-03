function hideBooks() {
    var i = 1;
    while (true) {
        var book = "book_" + String(i);
        var x = document.getElementById(book);
        if (!x) {
            break;
        }

        x.style.display = "none";

        i++;
    }
}

function showBooks(bookset) {
    hideBooks();

    var book = "bookset_" + String(bookset);
    var x = document.getElementsByClassName(book);

    var i;
    for (i = 0; x.length; i++) {
        x[i].style.display = "block";
    }
}