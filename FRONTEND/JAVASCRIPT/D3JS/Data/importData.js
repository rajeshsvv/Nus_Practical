window.onload = function importData()
{
    alert("error");
    // d3.json("\D3JS\Data\test_data_load_test.json",function(data)
    d3.json("/D3JS/Data/importData.js",function(data)
    {
        // console.log(data);
        var canvas=d3.select(".importData").append("svg")        
                    .attr("width",100)
                    .attr("height",500)
        canvas.selectAll("rect")
                .data(data)
                .enter()
                .append("rect")
                .attr("width",function(d)
                {
                    return d.locationid;
                })
                .attr("height",50)
                .attr("y",function(d,i)
                {
                    return i*80
                })
                .attr("fill","red");
        canvas.selectAll("text")
                .data(data)
                .enter()
                .append("text")
                .attr("fill","pink")
                .attr("y",function(d,i){
                    return i*80-25;
                })
                .data("x",5)
                .text(function(d)
                {
                    return d.firstname+"closeddate:"+d.lastname;
                })
    })

    // d3.json("\D3JS\Data\importData.js".then(function(data)
    //     {
    //         var canvas=d3.select("body").append("svg")
    //         .attr("width",1000)
    //         .attr("height",1000)

    //         canvas.selectAll("rect")
    //         .data(data)
    //         .enter()
    //         .append("rect")
    //         .attr("width",function(d){
    //             return d.firstname*100;
    //         })
    //         .attr("height",400)
    //         .attr("y",function(d,i){return i.subjectid*50
    //         })
    //         .attr("fill","blue")

    //         canvas.selectAll("text")
    //         .data(data)
    //         .enter()
    //             .append("text")
    //             .attr("fill","orange")
    //             .attr("y",function(d,i)
    //             {
    //                 return i*240+560;
    //             })
    //             .text(function(d)
    //             {
    //                 return d.firstname;
    //             })
    //     }))


        
}