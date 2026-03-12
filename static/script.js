document.getElementById("taskForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    
        const data = {
    firstName: document.getElementById("firstName").value,
    lastName: document.getElementById("lastName").value,
    email: document.getElementById("email").value,
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    dueDate: document.getElementById("dueDate").value
};
   
    try {
        const res = await fetch("/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        document.getElementById("responseMsg").textContent = result.message;

    } catch (error) {
        document.getElementById("responseMsg").textContent = "Error submitting task.";
    }
});