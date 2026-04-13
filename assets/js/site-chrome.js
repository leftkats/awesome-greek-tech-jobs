/* Theme toggle shared across all static pages. */
document.getElementById("themeToggleBtn")?.addEventListener("click", () => {
    document.documentElement.classList.toggle("dark");
});
