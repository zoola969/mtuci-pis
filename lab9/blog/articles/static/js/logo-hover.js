$(document).ready(() => {
	$(".header img").hover(
		(event) => {
			$(event.currentTarget).animate(
				{
					width: "+=20px",
				},
				300,
			);
		},
		(event) => {
			$(event.currentTarget).animate(
				{
					width: "-=20px",
				},
				300,
			);
		},
	);
});
