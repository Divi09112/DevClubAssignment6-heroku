var k = 0;

var dark = true;

function enter(elem,e){
  if (e.keyCode==13){
    var li = document.createElement("li");
    li.innerHTML=document.getElementById("entry").value;
    li.setAttribute("Id", "task"+k);
    document.getElementById("list").appendChild(li);
    document.getElementById("entry").value='';
    
    if (dark){
      li.className="dark";
      dark = false;
    }
    else{
      li.className="light";
      dark = true;
    };
    
    li.setAttribute('onClick',`strike(${k})`);
    k++;
  };
}


function strike(n){
  var el = document.getElementById("task"+n);

  if (el.className !== "clicked"){
    el.className="clicked";
  }
  else{
    const val = el.id.slice(4,el.id.length);
    if (val%2===0) {
      el.className = "dark";
    }
    else{
      el.className = "light";
    };
  };
}

console.log(document.getElementById('entry').value)
