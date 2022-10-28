   
function toggle(btn, id){
    fetch(`/add_remove_favorite/${id}`, {
        method: "GET"
    })
    .then(response => response.text())
    .then(result => {
        if(btn.classList.contains("fa-solid"))
        {
            btn.classList.remove("fa-solid");
            btn.classList.add("fa-regular");
        }
        else
        {
            btn.classList.add("fa-solid");
            btn.classList.remove("fa-regular");
        }
    })    
}

function toggle1(btn, id) {
    fetch(`/add_remove_to_cart/${id}`,{
        method: "GET"
    })
    .then(response => response.text())
    .then(result => 
    {

    if(btn.classList.contains("fa-solid"))
    {
        btn.classList.remove("fa-solid");
        btn.classList.add("fa-light");
    }
    else
    {
        btn.classList.add("fa-solid");
        btn.classList.remove("fa-light");
    }

})

}


function incrementValue(id)
{
    fetch(`/cart/${id}`, {
        method: "GET"
    })
    .then(response => response.text())
    .then(result => {
    
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value<10){
        value++;
            document.getElementById('number').value = value;
    }
})
}

function decrementValue(id)
{
    fetch(`/cart/${id}`, {
        method: "GET"
    })
    .then(response => response.text())
    .then(result => {

    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
            document.getElementById('number').value = value;
    }
})
}
