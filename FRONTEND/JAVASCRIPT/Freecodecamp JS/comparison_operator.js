// strict equality operator does not do the type conversion



function testEqual(val)
{
    if(val===10)
    {
        return "Equal";
    }
    return "Not Equal";
}

console.log(testEqual(10))



/*
Equality operator(do type conversion)
3==3    //true
3=='3'  //true

strictly equality operator(does not do type conversion)

3===3       //true
3==='3'     //false
*/

/*
function compareEqual(a,b)
{
    if(a===b)
    {
        return "Equal";
    }
    else
    {
        return "Not Eqaul"
    }
}
console.log(compareEqual(10,'10'))
*/


/*
function testNoEqual(val)
{
    if(val!=10)
    {
        return "Not Equal";
    }
    return "Equal";
}
console.log(testNoEqual(100))
*/


/*
function testNoEqual(val)
{
    if(val!==10)
    {
        return "Not Equal";
    }
    return "Equal";
}
console.log(testNoEqual('10'))
*/

/*
function greaterThan(val)
{
    if(val>100)
    {
        return "Over 100";

    }
    else if(val>10)
    {
        return "Over 10"
    }
    return "10 or under";
}
console.log(greaterThan(9))
/*


/*
function testOrEqual(val)
{
    if(val<=10)
    {
        return "smaller than or eqaul to 10";
    }
    if(val<=50)
    {
        return "smaller than or equal to 50";
    }
    return "More than 50";

}

console.log(testOrEqual(-90))
*/

/*
function testLogic(val)
{
    if (val <=50 && val>=25)
    {
        return "YES";
    }
    return "NO";
}
console.log(testLogic(5))
*/


/*
function logicOr(val)
{
    if(val<10 || val>20)
    {
        return "Outside";

    }
    return "Inside";
}
console.log(logicOr(90))
*/


function check(a,b)
{
    
    if(a==b)
    {
        console.log("both are equal")
    }
    else
    {
        console.log("a is not equal to b")
    }

}

console.log("checking");
log.write(check(3,'3'))
