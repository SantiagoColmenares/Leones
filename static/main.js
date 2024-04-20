const menuToggle = document.querySelector('.menu-toggle');

const navLinks = document.querySelector('.nav-links');


menuToggle.addEventListener('click', () => {

  navLinks.classList.toggle('active');

});


// Función para permitir solo letras en los campos de texto
function allowOnlyLetters(event) {
  const key = event.key;
  const regex = /^[a-zA-Z\s]*$/; // Expresión regular para permitir solo letras y espacios
  if (!regex.test(key)) {
      event.preventDefault(); // Evita que se teclee un carácter no permitido
  }
}

// Función para permitir solo números en los campos de número
function allowOnlyNumbers(event) {
  const key = event.key;
  const regex = /^[0-9]*$/; // Expresión regular para permitir solo números

  // Permitir teclas especiales como Backspace, Delete, ArrowLeft, ArrowRight
  const specialKeys = [
      'Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab', 'Enter'
  ];

  if (!regex.test(key) && !specialKeys.includes(key)) {
      event.preventDefault(); // Evita que se teclee un carácter no permitido
  }
}

function calculateAge(event) {
  const birthdateInput = event.target;
  const birthdate = new Date(birthdateInput.value);
  const today = new Date();

  // Si la fecha de nacimiento es válida
  if (!isNaN(birthdate)) {
      let age = today.getFullYear() - birthdate.getFullYear();
      
      // Ajustar la edad si el cumpleaños no ha pasado aún este año
      const currentMonth = today.getMonth();
      const birthMonth = birthdate.getMonth();
      const currentDay = today.getDate();
      const birthDay = birthdate.getDate();

      if (currentMonth < birthMonth || (currentMonth === birthMonth && currentDay < birthDay)) {
          age--;
      }

      // Completar el campo de edad con la edad calculada
      const ageInput = document.querySelector('input[name="edad"]');
      ageInput.value = age;
  }
}


// Asignar los eventos de teclado a los campos correspondientes
document.getElementById('id_nombre').addEventListener('keydown', allowOnlyLetters);
document.getElementById('id_apellido').addEventListener('keydown', allowOnlyLetters);
document.getElementById('id_documento_identidad').addEventListener('keydown', allowOnlyNumbers);
document.getElementById('id_edad').addEventListener('keydown', allowOnlyNumbers);
document.getElementById('id_telefono_contacto').addEventListener('keydown', allowOnlyNumbers);
const birthdateInput = document.querySelector('input[name="fecha_nacimiento"]');
birthdateInput.addEventListener('input', calculateAge);



