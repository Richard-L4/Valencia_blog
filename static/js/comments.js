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
   */
  // Method A: Buttons inside .reaction-buttons container
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
     if (!data.error){
        container.querySelector('.like-count').textContent = data.likes;
        container.querySelector('.dislike-count').textContent = data.dislikes;
      } 
    });
  }

  // Method B: General-purpose .reaction-button handling
  const buttons = document.querySelectorAll(".reaction-button");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const commentId = button.dataset.commentId;
      const action = button.dataset.action;

      fetch("/update-reaction/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCSRFToken()
        },
        body: `comment_id=${commentId}&action=${action}`
      })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error(data.error);
        } else {
          const likeBtn = document.querySelector(`#like-${commentId}`);
          const dislikeBtn = document.querySelector(`#dislike-${commentId}`);

          if (data.liked) {
            likeBtn.classList.add("active-reaction");
            dislikeBtn.classList.remove("active-reaction");
          } else if (data.disliked) {
            dislikeBtn.classList.add("active-reaction");
            likeBtn.classList.remove("active-reaction");
          } else {
            likeBtn.classList.remove("active-reaction");
            dislikeBtn.classList.remove("active-reaction");
          }
        }
      });
    });
  });

  /**
   * Retrieves the CSRF token from cookie or form
   */
  function getCSRFToken() {
    const metaToken = document.querySelector('[name=csrfmiddlewaretoken]');
    if (metaToken) return metaToken.value;

    const name = "csrftoken=";
    const decodedCookies = decodeURIComponent(document.cookie).split(';');
    for (let cookie of decodedCookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name)) {
        return cookie.substring(name.length);
      }
    }
    return '';
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
   * @param {string} lang - Language code ('en', 'es')
   */
  function changeLanguage(lang) {
    const guideElement = document.querySelector('[data-translate="guide"]');
    if (guideElement) {
      if (lang === 'en') {
        guideElement.textContent = "A guide to the Valencian Community";
      } else if (lang === 'es') {
        guideElement.textContent = "Una guía de Comunidad Valenciana";
      }
    } 
  }
});
