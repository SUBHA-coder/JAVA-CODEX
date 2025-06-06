async function askAI(codeId, outputId) {
    const code = document.getElementById(codeId).innerText;
    document.getElementById(outputId).innerText = "Explaining...";
    try {
        const response = await fetch("/api/explain", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code })
        });
        const data = await response.json();
        document.getElementById(outputId).innerText = data.explanation;
    } catch (err) {
        document.getElementById(outputId).innerText = "Something went wrong: " + err;
    }
}