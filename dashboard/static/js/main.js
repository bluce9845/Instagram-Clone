console.log("main.js loaded");

// ============ display Post function =========== //
function createNewPost() {
  const contents = document.querySelector(".contents");
  const sidebar2 = document.querySelector(".sidebar2");
  const createNewPostElement = document.querySelector(".slide");
  document.body.classList.add("no-scroll");

  createNewPostElement.style.display = "block";
  contents.style.zIndex = "-1";
  sidebar2.style.zIndex = "-1";
}

function closeCreatePost() {
  const contents = document.querySelector(".contents");
  const sidebar2 = document.querySelector(".sidebar2");
  const createNewPostElement = document.querySelector(".slide");
  document.body.classList.remove("no-scroll");

  // Debug
  // console.log("Close this create post...");

  createNewPostElement.style.display = "none";
  contents.style.removeProperty("z-index");
  sidebar2.style.removeProperty("z-index");
}

const displayFormPost = () => {
  const uploadContent = document.querySelector(".upload-content-1");
  const uploadForm = document.querySelector(".upload-content-form");

  uploadContent.style.display = "none";
  uploadForm.style.display = "block";
};

// ============ display Post function profile user login =========== //
function createNewPostProfileUserLogin() {
  const createNewPostElement = document.querySelector(".slide");
  const highlights = document.querySelector(".highlights");
  document.body.classList.add("no-scroll");

  // Debug
  console.log("Button create click...");

  createNewPostElement.style.display = "block";
  createNewPostElement.style.zIndex = "300";
  highlights.style.display = "none";
}

function closeCreatePostProfileUserLogin() {
  const createNewPostElement = document.querySelector(".slide");
  const highlights = document.querySelector(".highlights");
  document.body.classList.remove("no-scroll");

  // Debug
  console.log("Close this create post...");

  createNewPostElement.style.display = "none";
  createNewPostElement.style.removeProperty("z-index");
  highlights.style.display = "flex";
}

// ============ display Post function profile other user =========== //

// ========== display see more Btn if word more than 7 and move see more Btn if word less than or equal 7 =========//

document.addEventListener("DOMContentLoaded", function () {
  const posts = document.querySelectorAll(".description-content");

  posts.forEach((post) => {
    const fullText = post.querySelector(".full-text").innerText;
    const wordCount = fullText.trim().split(/\s+/).length;
    const seeMoreBtn = post.querySelector(".see-more-btn");
    const seeLessBtn = post.querySelector(".see-less-btn");
    const tagPost = post.querySelector(".tags-post");

    // Debug
    // console.log("Full Text Element:", fullText);
    // console.log("See More Button:", seeMoreBtn);
    // console.log("Word count:", wordCount);

    if (wordCount > 7) {
      seeMoreBtn.style.display = "block";
      tagPost.style.display = "none";
    } else {
      seeMoreBtn.style.display = "none";
    }

    // Event listener untuk "See More" button
    seeMoreBtn.addEventListener("click", function () {
      console.log("See More button clicked");
      post.querySelector(".short-text").style.display = "none";
      post.querySelector(".full-text").style.display = "block";
      seeMoreBtn.style.display = "none";
      seeLessBtn.style.display = "block";
    });

    // Event listener untuk "See Less" button
    seeLessBtn.addEventListener("click", function () {
      console.log("See Less button clicked");
      post.querySelector(".short-text").style.display = "block";
      post.querySelector(".full-text").style.display = "none";
      seeMoreBtn.style.display = "block";
      seeLessBtn.style.display = "none";
    });
  });
});

// ========= display icons in post profile if mouse over in img and hide icons if mouse out from img ===========//
function displayIcon(imageElement) {
  const postItem = imageElement.closest("li");

  const likeIcon = postItem.querySelector(".like-icon-post-profile");
  const commentIcon = postItem.querySelector(".comment-icon-post-profile");

  likeIcon.style.display = "block";
  commentIcon.style.display = "block";
}

function hideIcon(imageElement) {
  const postItem = imageElement.closest("li");

  const likeIcon = postItem.querySelector(".like-icon-post-profile");
  const commentIcon = postItem.querySelector(".comment-icon-post-profile");

  likeIcon.style.display = "none";
  commentIcon.style.display = "none";
}

// ============ post on click display detail post =============//

function postClick() {
  const containerProfile = document.querySelector(".container-profile");
  const detailPost = document.querySelector(".detail-posts");
  const higlights = document.querySelector(".highlights");

  detailPost.style.display = "block";
  containerProfile.style.position = "fixed";
  higlights.style.display = "none";
}

function closeDetailPost() {
  const containerProfile = document.querySelector(".container-profile");
  const detailPost = document.querySelector(".detail-posts");
  const higlights = document.querySelector(".highlights");

  detailPost.style.display = "none";
  containerProfile.style.position = "";
  higlights.style.display = "";
}
