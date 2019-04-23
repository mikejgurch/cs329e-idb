function hideAuthors() {
    var i = 1;
    while (true) {
        var author = "author_" + String(i);
        var x = document.getElementById(author);
        if (!x) {
            break;
        }

        x.style.display = "none";

        i++;
    }
}

function hideAuthorsInitial() {
    var i = 8;
    while (true) {
        var author = "author_" + String(i);
        var x = document.getElementById(author);
        if (!x) {
            break;
        }

        x.style.display = "none";

        i++;
    }
}

function showAuthors(authorset) {
    hideAuthors();
    toggleActive(authorset);

    var author = "authorset_" + String(authorset);
    var x = document.getElementsByClassName(author);

    var i;
    for (i = 0; x.length; i++) {
        x[i].style.display = "block";
    }
}

function showAuthorsInitial() {
    hideAuthorsInitial();
    showAuthors("1");
}

function toggleActive(current_authorpage) {
    var i = 1;
    while (true) {
        var authorpage = "authorpage_" + String(i);
        var element = document.getElementById(authorpage);
        if (!element) {
            break;
        }
        if (i == current_authorpage) {
            element.classList.add("active");
        } else {
            element.classList.remove("active");
        }

        i++;
    }
}