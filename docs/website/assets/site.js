// SPDX-License-Identifier: MIT
(() => {
  'use strict';
  const input = document.getElementById('search');
  const results = document.getElementById('search-results');
  if (!input || !results) return;
  const root = new URL(document.body.dataset.root || './', location.href);
  let pagesPromise;

  const loadPages = () => {
    if (!pagesPromise) {
      pagesPromise = fetch(document.body.dataset.searchIndex)
        .then((response) => {
          if (!response.ok) throw new Error('Search index unavailable');
          return response.json();
        })
        .catch(() => []);
    }
    return pagesPromise;
  };

  const close = () => {
    results.hidden = true;
    input.setAttribute('aria-expanded', 'false');
  };

  const render = async () => {
    const term = input.value.trim().toLowerCase();
    if (!term) { close(); return; }
    const pages = await loadPages();
    if (input.value.trim().toLowerCase() !== term) return;
    const words = term.split(/\s+/).filter(Boolean);
    const ranked = pages.map((page) => {
      const title = page.title.toLowerCase();
      const corpus = `${page.scope} ${page.title} ${page.description} ${page.terms}`.toLowerCase();
      if (!words.every((word) => corpus.includes(word))) return { page, score: -1 };
      return { page, score: words.reduce((score, word) => score + (title.includes(word) ? 5 : 1), 0) };
    }).filter((entry) => entry.score >= 0).sort((a, b) => b.score - a.score).slice(0, 12);
    results.replaceChildren();
    if (!ranked.length) {
      const empty = document.createElement('p');
      empty.className = 'search-empty';
      empty.textContent = 'No matching checklists. Try a broader term.';
      results.append(empty);
    }
    for (const { page } of ranked) {
      const link = document.createElement('a');
      link.className = 'search-result';
      link.href = new URL(page.url, root).href;
      const scope = document.createElement('small');
      scope.textContent = page.scope;
      const title = document.createElement('strong');
      title.textContent = page.title;
      link.append(scope, title);
      results.append(link);
    }
    results.hidden = false;
    input.setAttribute('aria-expanded', 'true');
  };

  input.addEventListener('input', render);
  input.addEventListener('focus', () => { if (input.value.trim()) render(); });
  input.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') { close(); input.blur(); }
    if (event.key === 'Enter' && !results.hidden) {
      const first = results.querySelector('a');
      if (first) { event.preventDefault(); first.click(); }
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
      event.preventDefault(); input.focus();
    }
    if (event.key === 'Escape') close();
  });
  document.addEventListener('click', (event) => {
    if (!event.target.closest('.search-wrap')) close();
  });
})();
