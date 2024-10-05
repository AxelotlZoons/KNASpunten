document.addEventListener('DOMContentLoaded', function() {

    // Access the form and prevent its default submission behavior
    const calcForm = document.getElementById('calcForm');
    const percentageOdometer = document.getElementById('percentageOdometer');
    const pointsOdometer = document.getElementById('pointsOdometer');
    
    let isSpinning = false;  // Flag to track if the odometer is spinning

    // Function to simulate continuous spinning
    function startOdometerSpinning() {
        isSpinning = true;

        const spinnerInterval = setInterval(() => {
            // If the spinning is stopped, exit the interval
            if (!isSpinning) {
                clearInterval(spinnerInterval);
                return;
            }

            // Continuously update the odometer values with random numbers
            percentageOdometer.innerHTML = Math.floor(Math.random() * 100);  // Random values for demo
            pointsOdometer.innerHTML = Math.floor(Math.random() * 1000);     // Random values for demo
        }, 100);  // Update every 100ms for smooth spinning effect
    }

    calcForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission to stop page reload

        // Start odometer spinning
        startOdometerSpinning();

        // Create a FormData object to hold the form values
        const formData = new FormData(calcForm);
        
        // Send a POST request to '/calculate'
        fetch('/calculate', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Data received:', data);  // Debug to check if the data is correct

            // Stop spinning and set final values
            isSpinning = false;

            // Animate to the correct values
            percentageOdometer.innerHTML = data.percentage;
            pointsOdometer.innerHTML = data.points;
        })
    });
});
