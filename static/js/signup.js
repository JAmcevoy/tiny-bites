document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('id_password1');
    const passwordHelp = document.getElementById('password-help');
    const passwordStrength = document.getElementById('password-strength');
    const signupButton = document.getElementById('signup-button');
    const signupForm = document.getElementById('signup-form');

    passwordInput.addEventListener('input', function() {
        const password = passwordInput.value;
        const strength = calculatePasswordStrength(password);
        updatePasswordStrengthIndicator(strength);
    });

    signupForm.addEventListener('submit', function(event) {
        const password = passwordInput.value;
        const strength = calculatePasswordStrength(password);

   
        if (strength < 2) { 
            event.preventDefault(); 
            passwordInput.focus(); 
            alert('Please choose a stronger password.');
        }
    });

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
