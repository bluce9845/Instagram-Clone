console.log("main.js loaded");

// ============ display Post function =========== //
function createNewPost() {
  const containers = document.querySelector(".containers");
  const contents = document.querySelector(".contents");
  const sidebar2 = document.querySelector(".sidebar2");
  const createNewPostElement = document.querySelector(".slide");

  createNewPostElement.style.display = "block";
  containers.style.position = "fixed";
  contents.style.zIndex = "-1";
  sidebar2.style.zIndex = "-1";
}

function closePost() {
  const containers = document.querySelector(".containers");
  const contents = document.querySelector(".contents");
  const sidebar2 = document.querySelector(".sidebar2");
  const createNewPostElement = document.querySelector(".slide");

  createNewPostElement.style.display = "none";
  contents.style.removeProperty("z-index");
  sidebar2.style.removeProperty("z-index");
  containers.style.removeProperty("position");
}

const displayFormPost = () => {
  const uploadContent = document.querySelector(".upload-content-1");
  const uploadForm = document.querySelector(".upload-content-form");

  uploadContent.style.display = "none";
  uploadForm.style.display = "block";
};

// ========== display see more Btn if word more than 7 and move see more Btn if word less than or equal 7 =========//

document.addEventListener("DOMContentLoaded", function () {
  const fullText = document.getElementById("full-text").innerText;
  const wordCount = fullText.trim().split(/\s+/).length;
  const seeMoreBtn = document.getElementById("see-more-btn");

  // Debug
  console.log("Full Text Element:", fullText);
  console.log("See More Button:", seeMoreBtn);
  console.log("Word count :", wordCount);

  if (wordCount > 7) {
    seeMoreBtn.style.display = "block";
  } else {
    seeMoreBtn.style.display = "none";
  }
});

// document.getElementById("see-more-btn").addEventListener("click", function () {});

const btnSeeMoreClick = () => {
  const seeMoreBtn = document.getElementById("see-more-btn");
  const seeLessBtn = document.getElementById("see-less-btn");

  // Debug
  console.log("See More button clicked");

  document.getElementById("short-text").style.display = "none";
  document.getElementById("full-text").style.display = "block";
  seeMoreBtn.style.display = "none";
  seeLessBtn.style.display = "block";
};

const btnSeeLessClick = () => {
  const seeMoreBtn = document.getElementById("see-more-btn");
  const seeLessBtn = document.getElementById("see-less-btn");

  // Debug
  console.log("See Less button clicked");

  document.getElementById("short-text").style.display = "block";
  document.getElementById("full-text").style.display = "none";
  seeMoreBtn.style.display = "block";
  seeLessBtn.style.display = "none";
};
