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

function hideBooksInitial() {
    var i = 15;
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
    toggleActive(bookset);

    var i = Number(bookset * 15 - 14);
    var j = Number(bookset * 15);
    for (i; i <= j; i++) {
        var book = "book_" + String(i);
        var x = document.getElementById(book);
        if (!x) {} else {
            x.style.display = "table-cell";
        }
    }
}

function showBooksInitial() {
    hideBooksInitial();
    showBooks("1");
}

function toggleActive(current_bookpage) {
    var i = 1;
    while (true) {
        var bookpage = "bookpage_" + String(i);
        var element = document.getElementById(bookpage);
        if (!element) {
            break;
        }
        if (i == current_bookpage) {
            element.classList.add("active");
        } else {
            element.classList.remove("active");
        }

        i++;
    }
}