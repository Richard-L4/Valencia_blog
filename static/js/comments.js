document.addEventListener('DOMContentLoaded', () => {
  

  /**
   * ===============================
   * 1. COMMENT EDIT FUNCTIONALITY
   * ===============================
   * Attaches event listeners to all edit buttons.
   * When clicked:
   *  - Retrieves the comment content by ID.
   *  - Populates the form with the comment's current text.
   *  - Updates the form's action to point to the correct edit URL.
   *  - Changes the submit button text to "Update".
   */
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      const commentId = e.target.getAttribute("data-comment_id");
      const commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }

  /**
   * ================================
   * 2. DELETE MODAL FUNCTIONALITY
   * ================================
   * Attaches event listeners to all delete buttons.
   * When clicked:
   *  - Updates the delete confirmation link with the appropriate comment ID.
   *  - Triggers the Bootstrap modal for confirmation.
   */
  const deleteModalEl = document.getElementById("deleteModal");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  if (deleteModalEl && deleteConfirm) {
    const deleteModal = new bootstrap.Modal(deleteModalEl);

    for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
      });
    }
  }

  /**
   * =================================
   * 3. LIKE / DISLIKE FUNCTIONALITY
   * =================================
   * For each comment's reaction buttons:
   *  - Sends a POST request to register a like or dislike.
   *  - Updates the counts shown without reloading the page.
   */
  document.querySelectorAll('.reaction-buttons').forEach(container => {
    const commentId = container.getAttribute('data-id');
    const likeBtn = container.querySelector('.like-btn');
    const dislikeBtn = container.querySelector('.dislike-btn');

    likeBtn.addEventListener('click', () => {
      sendReaction(commentId, 'like', container);
    });

    dislikeBtn.addEventListener('click', () => {
      sendReaction(commentId, 'dislike', container);
    });
  });

  /**
   * Sends a reaction to the server (like/dislike) for a given comment.
   * @param {string} commentId - ID of the comment being reacted to
   * @param {string} action - 'like' or 'dislike'
   * @param {HTMLElement} container - The container with the like/dislike UI
   */
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
        container.querySelector('.like-count').textContent = data.likes;
        container.querySelector('.dislike-count').textContent = data.dislikes;
      }
    });
  }

  /**
   * Retrieves the CSRF token from the page.
   * @returns {string} CSRF token value
   */
  function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
  }

  /**
   * ================================
   * 4. LANGUAGE SWITCH FUNCTIONALITY
   * ================================
   * Switches text content based on selected language.
   * Currently handles the guide heading.
   */
  document.querySelectorAll('.lang-btn').forEach(button => {
    button.addEventListener('click', () => {
      const lang = button.getAttribute('data-lang');
      changeLanguage(lang);
    });
  });

  /**
   * Changes text content of translatable elements based on selected language.
   * @param {string} lang - Language code ('en', 'es', etc.)
   */
  function changeLanguage(lang) {
    const guideElement = document.querySelector('[data-translate="guide"]');
    if (guideElement) {
      if (lang === 'en') {
        guideElement.textContent = "A guide to the Valencian Community";
      } else if (lang === 'es') {
        guideElement.textContent = "Una guía de Comunidad Valenciana";
      }
    } else {
      console.error('Guide element not found!');
    }
  }
});
