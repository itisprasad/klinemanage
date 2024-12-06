async function loadData() {
    const symbol = document.getElementById("symbol").value;
    const interval = document.getElementById("interval").value;

    const response = await fetch(`/kline?symbol=${symbol}&interval=${interval}`);
    const data = await response.json();

    const labels = data.map(item => item.time);
    const prices = data.map(item => ({
        o: item.open,
        h: item.high,
        l: item.low,
        c: item.close
    }));

    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
        type: 'candlestick',
        data: {
            labels: labels,
            datasets: [{
                label: `${symbol} - ${interval}`,
                data: prices
            }]
        }
    });
}

