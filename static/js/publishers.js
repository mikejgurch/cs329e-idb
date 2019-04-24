function hidePublishers() {
    var i = 1;
    while (true) {
        var publisher = "publisher_" + String(i);
        var x = document.getElementById(publisher);
        if (!x) {
            break;
        }

        x.style.display = "none";

        i++;
    }
}

function hidePublishersInitial() {
    var i = 15;
    while (true) {
        var publisher = "publisher_" + String(i);
        var x = document.getElementById(publisher);
        if (!x) {
            break;
        }

        x.style.display = "none";

        i++;
    }
}

function showPublishers(publisherset) {
    hidePublishers();
    toggleActivePub(publisherset);

    var i = Number(publisherset * 15 - 14);
    var j = Number(publisherset * 15);
    for (i; i <= j; i++) {
        var publisher = "publisher_" + String(i);
        var x = document.getElementById(publisher);
        if (!x) {} else {
            x.style.display = "table-cell";
        }
    }
}

function showPublishersInitial() {
    hidePublishersInitial();
    showPublishers("1");
}

function toggleActivePub(current_publisherpage) {
    var i = 1;
    while (true) {
        var publisherpage = "publisherpage_" + String(i);
        var element = document.getElementById(publisherpage);
        if (!element) {
            break;
        }
        if (i == current_publisherpage) {
            element.classList.add("active");
        } else {
            element.classList.remove("active");
        }

        i++;
    }
}
publisher