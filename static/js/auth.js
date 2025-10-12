console.log("✅ main.js loaded successfully");
document.addEventListener('DOMContentLoaded', function() {
    // ===== LOGIN PAGE TOGGLE =====
    const loginToggle = document.getElementById('visibility-login');
    const loginPassword = document.getElementById('password-login');
    const loginEye = document.getElementById('v_plain_login');
    const loginEyeSlash = document.getElementById('v_slash_login');

    if (loginToggle && loginPassword && loginEye && loginEyeSlash) {
        loginToggle.addEventListener('click', function() {
            const isHidden = loginPassword.type === 'password';
            loginPassword.type = isHidden ? 'text' : 'password';
            loginEye.style.display = isHidden ? 'none' : 'block';
            loginEyeSlash.style.display = isHidden ? 'block' : 'none';
        });
    }

    // ===== REGISTER PAGE TOGGLE =====
    const registerToggle = document.getElementById('visibility-register');
    const registerPassword = document.getElementById('password-register');
    const registerEye = document.getElementById('v_plain_register');
    const registerEyeSlash = document.getElementById('v_slash_register');

    if (registerToggle && registerPassword && registerEye && registerEyeSlash) {
        registerToggle.addEventListener('click', function() {
            const isHidden = registerPassword.type === 'password';
            registerPassword.type = isHidden ? 'text' : 'password';
            registerEye.style.display = isHidden ? 'none' : 'block';
            registerEyeSlash.style.display = isHidden ? 'block' : 'none';
        });
    }
});

document.querySelector("form").addEventListener("submit", function(event) {
    const password = document.getElementById("password-register").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();

    // Remove any existing message
    const existingMessage = document.getElementById("passwordError");
    if (existingMessage) existingMessage.remove();

    if (password !== confirmPassword) {
        event.preventDefault(); // Stop form submission

        // Create an error message element
        const errorMsg = document.createElement("div");
        errorMsg.id = "passwordError";
        errorMsg.textContent = "⚠️ Passwords do not match!, please try again.";
        errorMsg.style.color = "crimson";
        errorMsg.style.textAlign = "center";
        errorMsg.style.marginBottom = "10px";

        // Insert the message just above the Register button
        const button = document.querySelector("button[type='submit']");
        button.parentNode.insertBefore(errorMsg, button);

        // Optional: auto-hide message after 4 seconds
        setTimeout(() => {
            if (errorMsg) errorMsg.remove();
        }, 4000);
    }
});
