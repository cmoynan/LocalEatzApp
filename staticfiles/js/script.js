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
