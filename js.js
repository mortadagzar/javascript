function theLocation(){
    var city="san Fransico";
    return{
        get: function(){console.log(city);}
        set: function(newCity){city=newCity;}
    }
}