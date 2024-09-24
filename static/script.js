// Initialize the Chart.js bar chart with empty labels and data
let ctx = document.getElementById("probabilityChart").getContext("2d");
let probabilityChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: [],  // Empty labels initially
    datasets: [{
      label: "Probability",
      data: [],  // Empty data initially
      backgroundColor: [],
    }],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        max: 1,
      },
    },
  },
});

// Define a generic color palette
const colorPalette = [
  "#ff6384", "#36a2eb", "#4caf50", "#ff9f40", "#9966ff", "#ffcd56", "#c9cbcf"
];

// Handle button click to send input text to server
$("#text-button").click(function () {
  let message = {
    input_text: $("#text-input").val(),
  };
  console.log("Message to send:", message);

  $.post("http://localhost:5000/predict", JSON.stringify(message), function (response) {
    console.log("Response:", response);
    
    // Extract labels and data from the server response
    let labels = Object.keys(response);  // Dynamic labels (e.g., 'negative', 'neutral', 'positive')
    let data = Object.values(response).map(Number);  // Convert string probabilities to numbers
    
    // Update chart with new labels and data
    probabilityChart.data.labels = labels;
    probabilityChart.data.datasets[0].data = data;

    // Dynamically assign colors from the palette in sequence
    let backgroundColors = labels.map((_, index) => colorPalette[index % colorPalette.length]);
    probabilityChart.data.datasets[0].backgroundColor = backgroundColors;

    // Refresh the chart with new data
    probabilityChart.update();
  });
});
