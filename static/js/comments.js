const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

// static/js/comments.js

// Wait for the DOM to be ready before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {

  // Loop through all the comment containers
  document.querySelectorAll('.reaction-buttons').forEach(container => {
    const commentId = container.getAttribute('data-id');  // get the comment ID
    const likeBtn = container.querySelector('.like-btn');
    const dislikeBtn = container.querySelector('.dislike-btn');

    // When the like button is clicked
    likeBtn.addEventListener('click', () => {
      sendReaction(commentId, 'like', container);
    });

    // When the dislike button is clicked
    dislikeBtn.addEventListener('click', () => {
      sendReaction(commentId, 'dislike', container);
    });
  });

  // Function to send AJAX POST request with the action
  function sendReaction(commentId, action, container) {
    fetch('/comment/react/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': getCSRFToken()
      },
      body: `comment_id=${commentId}&action=${action}`
    })
    .then(response => response.json())
    .then(data => {
      if (!data.error) {
        // Update the counts in the HTML
        container.querySelector('.like-count').textContent = data.likes;
        container.querySelector('.dislike-count').textContent = data.dislikes;
      }
    });
  }

  // Function to retrieve CSRF token from hidden input
  function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
  }
});