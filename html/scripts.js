async function CheckCardNumber() {

    // получаем введеный в поле номер банковской карты
    const card_number = document.getElementById("card_number").value;

    const info_fields = ['bin', 'brand', 'type', 'category', 'issuer', 'alpha_2', 'alpha_3', 'country', 'latitude', 'longitude', 'bank_phone', 'bank_url']
    info_fields.forEach((field) => {
        document.getElementById(field).style.color = 'black';
        document.getElementById(field).textContent = "WAIT FOR RESPONSE";
    })
    document.getElementById("error").style.visibility = "hidden";
    document.getElementById("error").textContent = "";

    // отправляем запрос
    const response = await fetch("/get-info", {
        method: "POST",
        headers: {"Accept": "application/json", "Content-Type": "application/json"},
        body: JSON.stringify({
            card_number: card_number,
        })
    });

    if (response.ok) {
        const raw_data = await response.json();
        const card_info = raw_data.data;
        for (const key in card_info) {
            if (card_info[key]) {
                document.getElementById(key).textContent = card_info[key];
            } else {
                document.getElementById(key).textContent = `NOT FOUND`;
                document.getElementById(key).style.color = `red`;
            }
        }
    } else
        info_fields.forEach((field) => {
            document.getElementById(field).style.color = 'red';
            document.getElementById(field).textContent = "ERROR";
        })
        const error_data = await response.json()
        document.getElementById("error").style.color = 'red';
        document.getElementById("error").style.visibility = "visible";
        document.getElementById("error").textContent = error_data.detail;
        console.log(response);
}