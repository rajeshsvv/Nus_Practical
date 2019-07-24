// 7    Axes

// Axes are integral part of any chart or graph

d3.axisTop(),d3.axisRight(),d3.axisLeft(),d3.axisBottom()


// var data=[80,100,56,120,180,30,40,120,160]
var data=[1,2,3,4,5,6]

var svgHeight=500,svgWidth=300;

var svg=d3.select("svg")
    .attr("width",svgWidth)
    .attr("height",svgHeight)

var xScale=d3.scaleLinear()
    .domain([0,d3.max(data)])
    .range([0,svgWidth]);

var yScale=d3.scaleLinear()
    .domain([0,d3.max(data)])
    .range([svgHeight,0]);

var x_axis=d3.axisBottom().scale(xScale);
var y_axis=d3.axisLeft().scale(yScale);

svg.append("g")
    .attr("transform","translate(50,10)")
    .call(y_axis);

var xAxisTranslate=svgHeight-30;

svg.append("g")
    .attr("transform","translate(50, "+xAxisTranslate+")")
    .call(x_axis);