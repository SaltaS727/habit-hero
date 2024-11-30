document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".mark-done");

    buttons.forEach((button) => {
        button.addEventListener("click", (event) => {
            const taskItem = event.target.closest("li");

            // Prevent duplicate checkmarks
            if (!taskItem.querySelector("span")) {
                const checkmark = document.createElement("span");
                checkmark.textContent = "✔️"; // Checkmark symbol
                checkmark.style.color = "green"; // Ensure it's green
                checkmark.style.marginLeft = "10px";
                taskItem.appendChild(checkmark);
            }

            // Update button
            event.target.textContent = "Completed!";
            event.target.disabled = true;
        });
    });
});
