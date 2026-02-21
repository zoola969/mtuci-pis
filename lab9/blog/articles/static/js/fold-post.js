document.addEventListener("DOMContentLoaded", () => {
	const foldButtons = document.getElementsByClassName("fold-button");

	for (let i = 0; i < foldButtons.length; i++) {
		foldButtons[i].addEventListener("click", (e) => {
			console.log("Кнопка 'свернуть' была нажата");
			const foldedClass = "folded";
			const article = e.target.closest(".one-post");

			if (article.classList.contains(foldedClass)) {
				article.classList.remove(foldedClass);
				e.target.innerHTML = "свернуть";
			} else {
				article.classList.add(foldedClass);
				e.target.innerHTML = "развернуть";
			}
		});
	}
});
