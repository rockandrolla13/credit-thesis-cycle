// One scroll pass over an X search page. State stays in window.__xc between calls.
// The result is a short status word and a count. Post text never goes back to the model.
const sleep = ms => new Promise(r => setTimeout(r, ms));
await sleep(window.__xc ? 300 : 3500);
const S = window.__xc = window.__xc || { seen: new Map(), calls: 0 };
S.calls++;
const tidy = s => s.replace(/\s+/g, ' ').trim();
const grab = () => document.querySelectorAll('article[data-testid="tweet"]').forEach(a => {
  const t = a.querySelector('time'); if (!t) return;
  const id = (t.closest('a')?.getAttribute('href') || '').split('/').pop();
  if (!id || !/^\d+$/.test(id) || S.seen.has(id)) return;
  const texts = [...a.querySelectorAll('[data-testid="tweetText"]')].map(e => tidy(e.innerText));
  if (!texts.length || texts[0].length < 5) return;
  const who = a.querySelector('[data-testid="User-Name"]')?.innerText.split('\n').find(s => s.startsWith('@')) || '';
  S.seen.set(id, t.getAttribute('datetime').slice(0, 10) + ' | ' + who + ' | id ' + id + ' | post' +
    '\nTEXT: ' + texts[0].slice(0, 4000) + (texts[1] ? '\nQUOTED: ' + texts[1].slice(0, 1500) : ''));
});
let stale = 0; const t0 = Date.now();
while (stale < 6 && Date.now() - t0 < 21000) {
  const before = S.seen.size; grab();
  stale = S.seen.size === before ? stale + 1 : 0;
  window.scrollBy(0, 2600); await sleep(1300);
}
const col = document.querySelector('[data-testid="primaryColumn"]');
const retry = col ? [...col.querySelectorAll('button, [role="button"]')].some(b => /^(retry|try again)$/i.test(b.innerText.trim())) : false;
const noResults = col ? /No results for/i.test(col.innerText) : false;
let out;
if (/\/(login|i\/flow)/.test(location.pathname)) out = 'LOGIN';
else if (retry) out = 'RATELIMIT ' + S.seen.size;
else if (stale < 6) out = 'MORE ' + S.seen.size;
else if (S.seen.size === 0 && !noResults) out = 'UNSURE 0';
else out = 'DONE ' + S.seen.size;
S.last = out;
out
