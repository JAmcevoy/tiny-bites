document.addEventListener("DOMContentLoaded", function() {
    
    var createRadio = document.getElementById("createRadio");
    var reviewRadio = document.getElementById("reviewRadio");
    var postForm = document.getElementById("postForm");
    var reviewForm = document.getElementById("reviewForm");

    
    createRadio.addEventListener("change", function() {
        if (createRadio.checked) {
            postForm.style.display = "block";
            reviewForm.style.display = "none";
        }
    });

    reviewRadio.addEventListener("change", function() {
        if (reviewRadio.checked) {
            reviewForm.style.display = "block";
            postForm.style.display = "none";
        }
    });
});
