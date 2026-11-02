(() => {
    // Keep local previews out of the research interaction reports.
    const liveHosts = ['martamorando.com', 'www.martamorando.com', 'marta-morando.github.io'];
    if (!liveHosts.includes(window.location.hostname)) return;

    function trackInteraction(event) {
        if (event.defaultPrevented || !(event.target instanceof Element)) return;
        const control = event.target.closest('[data-analytics-event]');
        if (!control || control.disabled || typeof window.gtag !== 'function') return;

        // Include normal/keyboard activation and middle-clicked links, never right-clicks.
        if (event.type === 'click' && event.button !== 0) return;
        if (event.type === 'auxclick' && (event.button !== 1 || control.tagName !== 'A')) return;

        // Inline toggleAbstract runs before this bubbling listener; count opens only.
        if (control.classList.contains('abstract-button') &&
            control.getAttribute('aria-expanded') !== 'true') return;

        const parameters = {};
        if (control.tagName === 'A') {
            const url = new URL(control.href);
            // Send the public document path without query strings or fragments.
            parameters.link_url = url.origin + url.pathname;
            parameters.file_name = url.pathname;
            parameters.file_extension = 'pdf';
        }

        // Distinct event names make each paper visible without custom dimensions.
        // GA's optional automatic file_download event remains a separate measure.
        window.gtag('event', control.dataset.analyticsEvent, parameters);
    }

    document.addEventListener('click', trackInteraction);
    document.addEventListener('auxclick', trackInteraction);
})();
