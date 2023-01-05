console.log('test')
var roomAddress = document.querySelector('#name')
var addresses = document.querySelector('#names')


function showAddresses(){
    addresses.innerHTML = ''
    if (addressData.length > 0) {
        addressData.forEach(element => {
            addresses.innerHTML +=  "<div class='results' onclick= 'selectAddress("
                              + address.lat + "," + address.lon + "," + '"'+ address.display_name +'"' +")'>" 
                              + address.display_name +"</div>"
        
        });
    }
}

// function selectAddress(){

// }

function findAddresses(){
    var url = "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + address.value 
    fetch(url)
            .then(response => response.json())
            .then(data => addressArr = data)
            .then(show => showAddress())
            .catch(err => console.log(err))
}

// map
// var mymap = L.map('mapid').setView([-6.0358707641514915, 106.16313770172039], 12)