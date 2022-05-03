"use strict";

function modalWindow() {
  const overlay = document.querySelector(".overlay"),
    modal = document.querySelector(".modal"),
    modalContent = document.querySelector(".modal__content"),
    modalClose = document.querySelector(".modal__close");

  modalClose.addEventListener("click", () => {
    overlay.style.display = "none";
  });

  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) {
      overlay.style.display = "none";
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.code === "Escape" && overlay.style.display === "block") {
      overlay.style.display = "none";
    }
  });

  if (window.innerWidth < 700) {
    overlay.style.display = "block";
  }
}

export default modalWindow;
