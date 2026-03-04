let currentBatch = 0;
const batchSize = 24; 
const allCheckboxes = Array.from(document.querySelectorAll('input.bulkCheck[name="file"]'));
const totalFiles = allCheckboxes.length;

function downloadNextBatch() {
    if (currentBatch * batchSize >= totalFiles) {
        console.log("Finished all downloads.");
        return;
    }

    // 1. Reset selection
    allCheckboxes.forEach(cb => { if(cb.checked) cb.click(); });

    const startIndex = currentBatch * batchSize;
    const endIndex = startIndex + batchSize;
    const batch = allCheckboxes.slice(startIndex, endIndex);

    console.log(`Processing Batch ${currentBatch + 1}...`);

    // 2. Click with irregular timing (100ms to 400ms)
    batch.forEach((cb, index) => {
        setTimeout(() => {
            cb.click();
        }, index * (Math.random() * 300 + 100)); 
    });

    // 3. Trigger Download
    setTimeout(() => {
        const btn = document.getElementById('downloadFiles');
        if (btn) {
            btn.click();
            currentBatch++;
            
            // 4. LONG RANDOM WAIT (30 to 60 seconds)
            // This is the key to avoiding the "Too Many Requests" block
            const waitTime = Math.floor(Math.random() * 30000) + 30000;
            console.log(`Success. Waiting ${waitTime/1000} seconds before next batch to stay under the radar...`);
            setTimeout(downloadNextBatch, waitTime); 
        }
    }, (batchSize * 400) + 3000);
}

downloadNextBatch();