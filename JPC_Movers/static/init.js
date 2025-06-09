document.addEventListener('DOMContentLoaded', function () {
    const serviceSelect = document.getElementById('id_service');
    const workersSelect = document.getElementById('id_workers');
    const hoursSelect = document.getElementById('id_hours');
    const totalPriceDisplay = document.getElementById('total-price');

    const servicePrices = window.servicePrices || {};

    function updateTotal() {
        console.log("updating total");
        const serviceId = serviceSelect.value;
        const workers = parseInt(workersSelect.value) || 0;
        const hours = parseInt(hoursSelect.value) || 0;
        const pricePerHourPerWorker = servicePrices[serviceId] || 0;
        const total = pricePerHourPerWorker * workers * hours;
        totalPriceDisplay.textContent = total.toFixed(2);
    }

    serviceSelect.addEventListener('change', updateTotal);
    workersSelect.addEventListener('change', updateTotal);
    hoursSelect.addEventListener('change', updateTotal);
});
