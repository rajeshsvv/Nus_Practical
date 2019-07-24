function Circle(radius)
{
    // console.log('this',this);
    // let colour='red';
    this.radius=radius; 
    let defaultLocation={x:0,y:0};

    this.getDefaultLocation=function()
    {
        return defaultLocation;
    };

    // let computeOptimumLocation=function(factor)
    // {
    //     //some logic done here
    // }

    this.draw=function()
    {
        // let x,y;
        // this.computeOptimumLocation(11);
        //defaultLocation
        //if u want to use members of the new circle
        //this.radius

        console.log('draw');
    };
        Object.defineProperty(this,'defaultLocation',{
            get: function()
            {
                return defaultLocation;
            },
            set: function(value){
                if(!value.x||!value.y)
                {
                    throw new error('Invalid location');
                    
                }
                defaultLocation=value;
            }
        });
        
    }


const circle=new Circle(10);

// circle.getDefaultLocation();
// circle.defaultLocation=0;
// circle.computeOptimumLocation(); //only reading purpose 
circle.defaultLocation=1;
circle.draw();