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

$(document).ready(function(){
    var dict = {
        "I": "E",
        "E": "I",
        "S": "N",
        "N": "S",
        "T": "F",
        "F": "T",
        "J": "P",
        "P": "J"
    }
    $('input[name=toggle]').change(
        function() { 
            var state = $(this).attr("state");
            var newState = dict[state];
            $(this).attr("state", newState);
            var place = $(this).attr("place");
            console.log(newState);
            $('#' + place).html(newState);
        }
    );
});