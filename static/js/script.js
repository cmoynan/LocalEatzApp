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

// Add event listeners to set up time slots once the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the select element for time slots
    const select = document.getElementById('time');
    const startTime = new Date();
    const endTime = new Date();

    // Set start and end times for the booking options
    startTime.setHours(12, 0, 0);  // Set start time to 12:00 PM
    endTime.setHours(21, 0, 0);   // Set end time to 9:00 PM

    // Loop to create time slots from start to end time, incrementing by 1 hour
    while (startTime <= endTime) {
        // Create a new option element for the time slot
        const option = document.createElement('option');
        // Format the time to "HH:MM" and set as value and text content
        const timeString = startTime.toTimeString().substring(0, 5);
        option.value = timeString;
        option.textContent = timeString;
        // Append the option to the select element
        select.appendChild(option);
        
        // Add 1 hour to the start time for the next iteration
        startTime.setHours(startTime.getHours() + 1);
    }
});
