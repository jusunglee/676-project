$("#theForm").ajaxForm(
    {
        url: '/predict/', 
        type: 'post', 
        resetForm: true,
        success: function(res) {
            $("#results").fadeOut("slow", function() {
                var predictionLabel = document.getElementById("prediction-label");
                var predictionConfidence = document.getElementById("prediction-confidence");
                predictionLabel.innerText = res["prediction"];
                predictionConfidence.innerText = res["confidence"].toString().slice(2,4) + "% confidence";
                $("#results").fadeIn("slow");
            });


        }
    }
)

