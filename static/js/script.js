async function randomizeKey() {
    const response = await fetch('/random-key');
    const data = await response.json();
    document.getElementById('keyOutput').innerText = `Random Key: ${data.key} major`;
}

async function randomizeTimeSignature() {
    const response = await fetch('/random-time');
    const data = await response.json();
    document.getElementById('timeOutput').innerText = `Random Time Signature: ${data.time_signature}`;
}

async function generateMusic() {
    const num_measures = document.getElementById('num_measures').value;
    const keyOutput = document.getElementById('keyOutput').innerText.split(': ')[1];
    const timeOutput = document.getElementById('timeOutput').innerText.split(': ')[1];

    // Send data to the backend
    const response = await fetch('/generate-music', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            num_measures: num_measures || 16,
            key_signature: keyOutput,
            time_signature: timeOutput
        })
    });

    // Display the sheet music
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const sheetMusicImage = document.getElementById('sheetMusicImage');
    sheetMusicImage.src = url;
    sheetMusicImage.style.display = 'block';
}
