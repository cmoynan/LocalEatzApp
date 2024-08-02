// Add event listeners to all cancel buttons once the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Select all elements with the class 'cancel-btn' and add a click event listener to each
    document.querySelectorAll('.cancel-btn').forEach(button => {
        button.addEventListener('click', () => {
            // Get the booking ID from the data attribute of the button
            const bookingId = button.getAttribute('data-booking-id');
            // Call the confirmCancel function to handle the cancellation
            confirmCancel(bookingId);
        });
    });
});

// Function to handle booking cancellation
function confirmCancel(bookingId) {
    // Show a confirmation dialog to the user
    const confirmation = confirm("Are you sure you want to cancel this booking?");
    
    // If the user confirms the cancellation
    if (confirmation) {
        // Redirect to the cancel booking URL with the booking ID
        window.location.href = `/cancel-booking/${bookingId}/`;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const select = document.getElementById('time');
    if (!select) {
        console.error('Select element with ID "time" not found.');
        return;
    }

    const startTime = new Date();
    const endTime = new Date();

    startTime.setHours(12, 0, 0);
    endTime.setHours(21, 0, 0);

    select.innerHTML = '';  // Clear existing options

    while (startTime <= endTime) {
        const option = document.createElement('option');
        const timeString = startTime.toTimeString().substring(0, 5);
        option.value = timeString;
        option.textContent = timeString;
        select.appendChild(option);

        startTime.setHours(startTime.getHours() + 1);
    }
});
