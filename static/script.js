document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const sections = document.querySelectorAll(".category-section");
    const noResults = document.getElementById("no-results");

    searchInput.addEventListener("input", (e) => {
        const term = e.target.value.toLowerCase().trim();
        let totalVisibleCards = 0;

        sections.forEach(section => {
            const sectionCards = section.querySelectorAll(".tool-card");
            let sectionVisible = false;

            sectionCards.forEach(card => {
                const title = card.querySelector("h3").textContent.toLowerCase();
                const desc = card.querySelector("p").textContent.toLowerCase();
                const category = card.querySelector(".category-badge").textContent.toLowerCase();

                if (title.includes(term) || desc.includes(term) || category.includes(term)) {
                    card.style.display = "flex";
                    sectionVisible = true;
                    totalVisibleCards++;
                } else {
                    card.style.display = "none";
                }
            });

            // Smooth fade in/out for sections
            if (sectionVisible) {
                if (section.style.display === "none") {
                    section.style.display = "block";
                    section.animate([{opacity: 0}, {opacity: 1}], {duration: 300, fill: 'forwards'});
                }
            } else {
                section.style.display = "none";
            }
        });

        if (totalVisibleCards === 0) {
            if (noResults.classList.contains("hidden")) {
                noResults.classList.remove("hidden");
                noResults.animate([{opacity: 0}, {opacity: 1}], {duration: 300, fill: 'forwards'});
            }
        } else {
            noResults.classList.add("hidden");
        }
    });
});
