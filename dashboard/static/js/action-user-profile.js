const tableCells = document.querySelectorAll(".header-profile table td");

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("posts").classList.add("active-profile");
  document.getElementById("posts").classList.add("text-dark");
});

tableCells.forEach((cell) => {
  cell.addEventListener("click", function () {
    // Hapus class 'active' dari semua <td>
    tableCells.forEach((td) => td.classList.remove("active-profile"));
    tableCells.forEach((td) => td.classList.remove("text-dark"));

    // Tambahkan class 'active' ke <td> yang diklik
    this.classList.add("active-profile");
    this.classList.add("text-dark");
  });
});
