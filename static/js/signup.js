document.addEventListener('DOMContentLoaded', function() {
    const passwordInput1 = document.getElementById('id_password1');
    const passwordInput2 = document.getElementById('id_password2');
    const passwordHelp = document.getElementById('password-help');
    const passwordMismatchMessage = 'New password and confirmation do not match.';
    const passwordForm = document.forms['passwordForm'];
    const submitButton = document.getElementById('submit-button');

    passwordInput1.addEventListener('input', function() {
        const password = passwordInput1.value;
        const strength = calculatePasswordStrength(password);
        updatePasswordStrengthIndicator(strength);
        validatePasswordsMatch();
    });

    passwordInput2.addEventListener('input', function() {
        validatePasswordsMatch();
    });

    function validatePasswordsMatch() {
        const password1 = passwordInput1.value;
        const password2 = passwordInput2.value;

        // Check if passwords match
        if (password1 === password2) {
            passwordHelp.textContent = '';
            submitButton.style.display = 'block';
        } else {
            passwordHelp.textContent = passwordMismatchMessage;
        }
    }

    function calculatePasswordStrength(password) {
        let strength = 0;

        // Minimum length check
        if (password.length >= 6) {
            strength++;
        }

        // Check for presence of uppercase letters
        if (/[A-Z]/.test(password)) {
            strength++;
        }

        // Check for presence of lowercase letters
        if (/[a-z]/.test(password)) {
            strength++;
        }

        // Check for presence of numbers
        if (/\d/.test(password)) {
            strength++;
        }

        // Check for presence of special characters
        if (/[^A-Za-z0-9]/.test(password)) {
            strength++;
        }

        return strength;
    }

    function updatePasswordStrengthIndicator(strength) {
        const strengthIndicator = document.getElementById('password-strength');

        strengthIndicator.classList.remove('weak', 'moderate', 'strong');

        if (strength === 0 || strength === 1) {
            strengthIndicator.textContent = 'Weak';
            strengthIndicator.classList.add('weak');
        } else if (strength === 2 || strength === 3) {
            strengthIndicator.textContent = 'Moderate';
            strengthIndicator.classList.add('moderate');
        } else if (strength >= 4) {
            strengthIndicator.textContent = 'Strong';
            strengthIndicator.classList.add('strong');
        }
    }
});
