async function askAI(codeId, outputId) {
    const code = document.getElementById(codeId).innerText;
    const response = await fetch("/api/explain", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ code: code })
    });
    const data = await response.json();
    document.getElementById(outputId).innerText = data.explanation;
}