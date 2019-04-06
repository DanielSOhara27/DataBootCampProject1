// Global variables
var url = "http://127.0.0.1:5000/amz200k-table"

//Getting the data from the flask app
d3.json(url).then( response => {
    //do something
    console.log("json response from flask server");
    console.log(response);

    var myTable = d3.select("data-table")
});