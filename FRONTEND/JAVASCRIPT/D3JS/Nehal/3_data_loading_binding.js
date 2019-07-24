
// 3    Data Loading and Binding
// using d3 we can map our data into DOM elements means we can append update or display DOM elements

var dataset=[1,2,3,4,5]

d3.select('body')
.selectAll('p')
.data(dataset)
.enter()
.append('p')
.text("D3 is in position")
// .text(function(d)
// {
//     return d;
// })

d3.selectAll('p').style('color',"green")
