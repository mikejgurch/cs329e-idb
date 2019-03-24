function totalTable() {
    var commitsTotal = 0;
    commitsTotal += Number(document.getElementById("r1c1").innerHTML);
    commitsTotal += Number(document.getElementById("r2c1").innerHTML);
    commitsTotal += Number(document.getElementById("r3c1").innerHTML);
    commitsTotal += Number(document.getElementById("r4c1").innerHTML);
    commitsTotal += Number(document.getElementById("r5c1").innerHTML);

    document.getElementById("commitsTotal").innerHTML = commitsTotal;

    var issuesTotal = 0;
    issuesTotal += Number(document.getElementById("r1c2").innerHTML);
    issuesTotal += Number(document.getElementById("r2c2").innerHTML);
    issuesTotal += Number(document.getElementById("r3c2").innerHTML);
    issuesTotal += Number(document.getElementById("r4c2").innerHTML);
    issuesTotal += Number(document.getElementById("r5c2").innerHTML);

    document.getElementById("issuesTotal").innerHTML = issuesTotal;

    var unitTests = 0;
    unitTests += Number(document.getElementById("r1c3").innerHTML);
    unitTests += Number(document.getElementById("r2c3").innerHTML);
    unitTests += Number(document.getElementById("r3c3").innerHTML);
    unitTests += Number(document.getElementById("r4c3").innerHTML);
    unitTests += Number(document.getElementById("r5c3").innerHTML);

    document.getElementById("unitTests").innerHTML = unitTests;
}