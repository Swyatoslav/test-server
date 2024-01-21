async function CheckCardNumber() {

    // получаем введеный в поле номер банковской карты
    const card_number = document.getElementById("card_number").value;

    const info_fields = ['bin', 'brand', 'type', 'category', 'issuer', 'alpha_2', 'alpha_3', 'country', 'latitude', 'longitude', 'bank_phone', 'bank_url']
    info_fields.forEach((field) => {
        document.getElementById(field).style.color = 'black';
        document.getElementById(field).textContent = "WAIT FOR RESPONSE";
    })

    // отправляем запрос
    const response = await fetch("/get-info", {
        method: "POST",
        headers: {"Accept": "application/json", "Content-Type": "application/json"},
        body: JSON.stringify({
            card_number: card_number,
        })
    });

    if (response.ok) {
        const data = await response.json();
        const card_info = JSON.parse(data.data)
        for (const key in card_info) {
            if (card_info[key]) {
                document.getElementById(key).textContent = card_info[key];
            } else {
                document.getElementById(key).textContent = `NOT FOUND`;
                document.getElementById(key).style.color = `red`;
            }
        }
        // document.getElementById("type").textContent = data.data.type ? data.data.type : "-"
        // document.getElementById("category").textContent = data.data.category ? data.data.category : "-"
        // document.getElementById("issuer").textContent = data.data.issuer ? data.data.issuer : "-"
        // document.getElementById("alpha_2").textContent = data.data.alpha_2 ? data.data.alpha_2 : "-"
        // document.getElementById("alpha_3").textContent = data.data.alpha_3 ? data.data.alpha_3 : "-"
        // document.getElementById("country").textContent = data.data.country ? data.data.country : "-"
        // document.getElementById("latitude").textContent = data.data.latitude ? data.data.latitude : "-"
        // document.getElementById("longitude").textContent = data.data.longitude ? data.data.longitude : "-"
        // document.getElementById("bank_phone").textContent = data.data.bank_phone ? data.data.bank_phone : "-"
        // document.getElementById("bank_url").textContent = data.data.bank_url ? data.data.bank_url : "-"
    } else
        info_fields.forEach((field) => {
            document.getElementById(field).style.color = 'red';
            document.getElementById(field).textContent = "ERROR";
        })
    console.log(response);
}