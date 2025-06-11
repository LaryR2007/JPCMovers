document.addEventListener("DOMContentLoaded", function () {
    const serviceSelect = document.getElementById("id_service");
    const workersSelect = document.getElementById("id_workers");
    const hoursSelect = document.getElementById("id_hours");
    const totalDisplay = document.getElementById("total-cost");

    const servicePrices = JSON.parse(document.getElementById("service-prices").textContent);

    function updateTotal() {
        const serviceId = serviceSelect.value;
        const workers = parseInt(workersSelect.value) || 0;
        const hours = parseInt(hoursSelect.value) || 0;

        if (serviceId && workers && hours) {
            const basePrice = parseFloat(servicePrices[serviceId]) || 0;
            const total = (basePrice * workers * hours).toFixed(2);
            totalDisplay.innerText = `$${total}`;
        } else {
            totalDisplay.innerText = "$0.00";
        }
    }

    serviceSelect.addEventListener("change", updateTotal);
    workersSelect.addEventListener("change", updateTotal);
    hoursSelect.addEventListener("change", updateTotal);

    updateTotal(); // initialize on load
});
