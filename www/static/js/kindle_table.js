// Global variables
var url = "http://127.0.0.1:5000/kindle-table"

//Getting the data from the flask app
d3.json(url).then( response => {

    var myTable = d3.select(".data-table")

    var tBody = myTable.select("#main")




    for(var i = 1; i < 6; i++){
        var tR = tBody.append("tr");
        tR.append("td").text(response[i]["kindle_id"]);
        tR.append("td").text(response[i]["Reviewer ID"]);
        tR.append("td").text(response[i]["ASIN"]);
        tR.append("td").text(response[i]["Review Time"]);
        tR.append("td").text(response[i]["Overall"]);
        tR.append("td").text(response[i]["Summary"]);
    }



});
