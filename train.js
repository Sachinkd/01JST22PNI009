document.addEventListener("DOMContentLoaded", function() {
    // Sample train schedule data (hardcoded for simplicity)
    const trainSchedule = [
        { trainNumber: "123", trainName: "Express Train", departureTime: "08:00 AM", arrivalTime: "12:00 PM" },
        { trainNumber: "456", trainName: "Local Train", departureTime: "10:30 AM", arrivalTime: "02:30 PM" },
        { trainNumber: "789", trainName: "Superfast Train", departureTime: "02:00 PM", arrivalTime: "06:00 PM" },
    ];

    // Function to create and append a new table row for each train in the schedule
    function renderSchedule() {
        const scheduleBody = document.getElementById("schedule-body");
        trainSchedule.forEach(train => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${train.trainNumber}</td>
                <td>${train.trainName}</td>
                <td>${train.departureTime}</td>
                <td>${train.arrivalTime}</td>
            `;
            scheduleBody.appendChild(row);
        });
    }

    renderSchedule();
});
