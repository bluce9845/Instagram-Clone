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

function closeCreatePost() {
  const containers = document.querySelector(".containers");
  const contents = document.querySelector(".contents");
  const sidebar2 = document.querySelector(".sidebar2");
  const createNewPostElement = document.querySelector(".slide");

  // Debug
  console.log("Close this create post...");

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
  const posts = document.querySelectorAll(".description-content");

  posts.forEach((post) => {
    const fullText = post.querySelector(".full-text").innerText;
    const wordCount = fullText.trim().split(/\s+/).length;
    const seeMoreBtn = post.querySelector(".see-more-btn");
    const seeLessBtn = post.querySelector(".see-less-btn");
    const tagPost = post.querySelector(".tags-post");

    // Debug
    console.log("Full Text Element:", fullText);
    console.log("See More Button:", seeMoreBtn);
    console.log("Word count:", wordCount);

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

  console.log("Mouse over........");

  likeIcon.style.display = "block";
  commentIcon.style.display = "block";
}

function hideIcon(imageElement) {
  const postItem = imageElement.closest("li");

  const likeIcon = postItem.querySelector(".like-icon-post-profile");
  const commentIcon = postItem.querySelector(".comment-icon-post-profile");

  console.log("Mouse out........");

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

// ========= like condition =========== //

function likeClick() {
  const likeIconNotLike = document.querySelector(".like-icon-not-like");
  const likeIconLike = document.querySelector(".like-icon-like");

  likeIconNotLike.style.display = "none";
  likeIconLike.style.display = "inline-block";
}

function disLike() {
  const likeIconNotLike = document.querySelector(".like-icon-not-like");
  const likeIconLike = document.querySelector(".like-icon-like");

  likeIconNotLike.style.display = "inline-block";
  likeIconLike.style.display = "none";
}
