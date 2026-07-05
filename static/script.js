// ===== Count Animation =====

function animateValue(element, start, end, duration) {

    let startTime = null;

    function animation(currentTime) {

        if (!startTime) startTime = currentTime;

        const progress = Math.min((currentTime - startTime) / duration, 1);

        element.innerHTML = Math.floor(progress * (end - start) + start);

        if (progress < 1) {
            requestAnimationFrame(animation);
        }

    }

    requestAnimationFrame(animation);

}


// ===== Animate Cards =====

window.onload = () => {

    document.querySelectorAll(".card").forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(30px)";

        setTimeout(() => {

            card.style.transition = ".5s";

            card.style.opacity = "1";

            card.style.transform = "translateY(0)";

        }, index * 150);

    });

};


// ===== Chart =====

const chart = document.getElementById("growthChart");

if(chart){

new Chart(chart,{

type:"line",

data:{

labels:["Jan","Feb","Mar","Apr","May","Jun"],

datasets:[{

label:"Growth",

data:[1200,1800,2500,3100,4500,6000],

borderColor:"#38bdf8",

backgroundColor:"rgba(56,189,248,.2)",

fill:true,

tension:.4

}]

},

options:{

responsive:true,

plugins:{

legend:{

labels:{

color:"white"

}

}

},

scales:{

x:{

ticks:{

color:"white"

}

},

y:{

ticks:{

color:"white"

}

}

}

}

});

}
window.addEventListener("load",()=>{

setTimeout(()=>{

const loader=document.getElementById("loader");

if(loader){

loader.style.display="none";

}

},1200);

});
