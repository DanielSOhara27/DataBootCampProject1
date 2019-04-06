var trace1 = {
  labels: ["1 Star", "2 Star", "3 Star", "4 Star",
      "5 Star"],
  values: [330, 257, 300, 600, 900],
  type: 'pie'
};

var data = [trace1];

var layout = {
  title: "MOCK: Num per Ratings",
};

Plotly.newPlot("pie-plot", data, layout);
