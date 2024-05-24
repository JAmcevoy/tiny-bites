/**
 * @jest-environment jsdom
 */

function validatePasswordsMatch() {
    const password1 = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;
    const passwordHelp = document.getElementById('password-help');
    const submitButton = document.getElementById('submit-button');
    const passwordMismatchMessage = 'New password and confirmation do not match.';
  

    if (password1 === password2) {
      passwordHelp.textContent = '';
      submitButton.style.display = 'block';
    } else {
      passwordHelp.textContent = passwordMismatchMessage;
    }
  }
  
  function calculatePasswordStrength(password) {
    let strength = 0;
  

    if (password.length >= 6) {
      strength++;
    }
  

    if (/[A-Z]/.test(password)) {
      strength++;
    }
  

    if (/[a-z]/.test(password)) {
      strength++;
    }
  

    if (/\d/.test(password)) {
      strength++;
    }
  

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
  

  describe('Password Validation Functions', () => {

    beforeEach(() => {
      document.body.innerHTML = `
        <form id="passwordForm">
          <input id="id_password1" type="password">
          <input id="id_password2" type="password">
          <div id="password-help"></div>
          <button id="submit-button" style="display: none;"></button>
        </form>
        <div id="password-strength"></div>
      `;
    });
  

    test('validatePasswordsMatch function should update help text and button visibility', () => {

      document.getElementById('id_password1').value = 'password123';
      document.getElementById('id_password2').value = 'password123';
  

      validatePasswordsMatch();
  

      expect(document.getElementById('password-help').textContent).toBe('');
      expect(document.getElementById('submit-button').style.display).toBe('block');
    });
  

    test('calculatePasswordStrength function should return the correct strength', () => {

      expect(calculatePasswordStrength('')).toBe(0); 
      expect(calculatePasswordStrength('password')).toBe(2);
      expect(calculatePasswordStrength('Pa$$w0rd')).toBe(5);
    });

    test('updatePasswordStrengthIndicator function should update strength indicator', () => {
      updatePasswordStrengthIndicator(0);
      expect(document.getElementById('password-strength').textContent).toBe('Weak');
      expect(document.getElementById('password-strength').classList.contains('weak')).toBe(true);
  
      updatePasswordStrengthIndicator(2);
      expect(document.getElementById('password-strength').textContent).toBe('Moderate');
      expect(document.getElementById('password-strength').classList.contains('moderate')).toBe(true);
  
      updatePasswordStrengthIndicator(4);
      expect(document.getElementById('password-strength').textContent).toBe('Strong');
      expect(document.getElementById('password-strength').classList.contains('strong')).toBe(true);
    });
  });
  