document.addEventListener('DOMContentLoaded', function () {
  // Get the Sign Up link, modal, and close button elements
  var signupLink = document.getElementById('signupLink');
  var signupModal = document.getElementById('signupModal');
  var closeModal = document.getElementById('closeModal');

  // Function to open the modal
  function openModal(event) {
    event.preventDefault();
    signupModal.classList.add('show');
  }

  // Function to close the modal
  function hideModal() {
    signupModal.classList.remove('show');
  }

  // When the Sign Up link is clicked, open the modal
  signupLink.addEventListener('click', openModal);

  // When the close button (×) is clicked, close the modal
  closeModal.addEventListener('click', hideModal);

  // Also close the modal if the user clicks outside of the modal content
  signupModal.addEventListener('click', function (event) {
    if (event.target === signupModal) {
      hideModal();
    }
  });
});
