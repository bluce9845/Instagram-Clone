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
