$(document).ready(() => {
	$(".one-post").hover(
		(event) => {
			$(event.currentTarget).find(".one-post-shadow").animate(
				{
					opacity: "0.1",
				},
				300,
			);
		},
		(event) => {
			$(event.currentTarget)
				.find(".one-post-shadow")
				.animate({ opacity: "0" }, 300);
		},
	);
});
