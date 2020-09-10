function initMap() {
    //The location of Oconnell Street in Sligo
            var oconnellstr ={lat: 54.271374, lng:-8.475250};
    //The map centered at Oconnell Street
            var map = new google.maps.Map(
                document.getElementById('google-location'), {zoom:15, center: oconnellstr});
            var marker = new google.maps.Marker({position: oconnellstr, map: map}); 
        }