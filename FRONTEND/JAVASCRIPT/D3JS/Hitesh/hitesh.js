heroes=['Hulk','Dr.Strange','Capt.America','Shaktiman']
        d3.select("h2").style("font-size","30px");
        d3.select('ul')
        .selectAll('li')
        .data(heroes)
        .enter()
        .append("li")
        .text(hero=>hero+"!");

        var numbers=[20,30,50,30,10,100]
        var barHeight=40;
        d3.select("svg")
        .selectAll("rect")
        .data(numbers)
        .enter()        
        .append("rect")
        .attr("width",d=>d)
        .attr("height",barHeight-4)
        .attr(
            'transform',(d,i)=>"translate(100,"+i*barHeight+")"
        )