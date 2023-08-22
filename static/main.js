document.addEventListener("DOMContentLoaded", function () {
    // Fetch the JSON file
    fetch("static/route.json")
        .then(response => response.json())
        .then(data => {
            console.log(data)
            main_container = document.getElementById("main_container")
            for (item of data) {
                
                extended_class = item["extended"] ? "extended" : ""

                if (item["type"] == "city"){

                    city_name = item["name"]
                    image_path = "static/city_maps/" + city_name + ".png"

                    city_template = `<div class="row ${extended_class}">
                    <div class="col-lg-4 offset-lg-4">
                        <div class="map-item">
                            <img src="${image_path}">
                            <div>
                                ${city_name}
                            </div>
                        </div>
                    </div>
                    </div>`

                    const temp_div = document.createElement("div");
                    temp_div.innerHTML = city_template;

                    main_container.appendChild(temp_div.firstChild)
                }

                if (item["type"] == "pic"){

                    image_path = item["path"]

                    image_template = `<div class="row ${extended_class}">
                    <div class="col-lg-4 offset-lg-4">
                        <div class="img-item">
                            <img src="${image_path}">
                        </div>
                    </div>
                    </div>`

                    const temp_div = document.createElement("div");
                    temp_div.innerHTML = image_template;

                    main_container.appendChild(temp_div.firstChild)
                }
                
            }
        })
        .catch(error => {
            console.error("Error fetching JSON:", error);
        });
});



