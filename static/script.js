
const ctx = document.getElementById('growthChart');

new Chart(ctx,{

type:'line',

data:{

labels:["Jan","Feb","Mar","Apr","May","Jun"],

datasets:[{

label:"Growth",

data:[12,25,18,35,42,55],

borderWidth:3,

fill:false

}]

},

options:{

responsive:true

}

});
