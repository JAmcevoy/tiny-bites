var currentUrl = window.location.href;
var hideSupportBubble = currentUrl.includes("support/submit_error");

if (hideSupportBubble) {
    document.getElementById("support-bubble").style.display = "none";
}

document.getElementById("support-bubble").onclick = function() {
    var supportUrl = window.location.origin + "/support/submit_error/";
    window.location.href = supportUrl;
}

document.getElementById("admin-bubble").onclick = function() {
    var supportUrl = window.location.origin + "/admin/";
    window.location.href = supportUrl;
}