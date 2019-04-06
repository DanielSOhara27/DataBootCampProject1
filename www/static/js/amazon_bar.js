var trace1 = {
   x: ["Clothing", "Clothing>women", "Clothing>men", "Clothing>women>children", "Clothing>men>children"],
   y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
   type: "bar"
 };

var data = [trace1];

var layout = {
   title: "MOCK: ",
   xaxis: { title: "Categories"},
   yaxis: { title: "% of Reviews per Category"}
};

Plotly.newPlot("bar-plot", data, layout);
