document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.cancel-btn').forEach(button => {
        button.addEventListener('click', () => {
            const bookingId = button.getAttribute('data-booking-id');
            confirmCancel(bookingId);
        });
    });
});

function confirmCancel(bookingId) {
    const confirmation = confirm("Are you sure you want to cancel this booking?");
    
    if (confirmation) {
        window.location.href = `/cancel-booking/${bookingId}/`;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const select = document.getElementById('time');
    const startTime = new Date();
    const endTime = new Date();

    // Set start and end times
    startTime.setHours(12, 0, 0);  // 12:00 PM
    endTime.setHours(21, 0, 0);   // 9:00 PM

    while (startTime <= endTime) {
        const option = document.createElement('option');
        const timeString = startTime.toTimeString().substring(0, 5);
        option.value = timeString;
        option.textContent = timeString;
        select.appendChild(option);
        
        // Add 1 hour
        startTime.setHours(startTime.getHours() + 1);
    }
});
