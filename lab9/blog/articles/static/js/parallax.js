$(document).ready(() => {
	let scrolled = 0;
	let ticking = false;
	const $parallaxElements = $(".icons-for-parallax img");
	const $logo = $(".header-logo");

	const initialTops = $parallaxElements.map((i, el) => el.offsetTop).get();

	const maxScroll = $(".header").outerHeight();

	const updateParallax = () => {
		const clamped = Math.min(scrolled, maxScroll);
		for (let i = 0; i < $parallaxElements.length; i++) {
			const yPosition = initialTops[i] + clamped * 0.15 * (i + 1);
			$parallaxElements.eq(i).css({ top: yPosition });
		}
		$logo.css({ transform: `translateY(${clamped * 0.25}px)` });
		ticking = false;
	};

	$(window).on("scroll", () => {
		scrolled = $(window).scrollTop();
		if (!ticking) {
			requestAnimationFrame(updateParallax);
			ticking = true;
		}
	});
});
