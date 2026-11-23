await new Promise(r => setTimeout(r, 4000));
const seen = new Map(); let stale = 0; const t0 = Date.now();
while (stale < 4 && seen.size < 45 && Date.now() - t0 < 26000) {
  const before = seen.size;
  document.querySelectorAll('article[data-testid="tweet"]').forEach(a => {
    const t = a.querySelector('time'); if (!t) return;
    const id = (t.closest('a')?.getAttribute('href') || '').split('/').pop();
    if (!id || !/^\d+$/.test(id) || seen.has(id)) return;
    const clean = s => s.replace(/https?:\S+/g, '[link]').replace(/[?=&]/g, ' ').replace(/\s+/g, ' ').trim();
    const texts = [...a.querySelectorAll('[data-testid="tweetText"]')].map(e => clean(e.innerText));
    if (!texts.length || texts[0].length < 20) return;
    const who = a.querySelector('[data-testid="User-Name"]')?.innerText.split('\n').find(s => s.startsWith('@')) || '';
    const ctx = a.querySelector('[data-testid="socialContext"]')?.innerText || '';
    seen.set(id, t.getAttribute('datetime').slice(0, 10) + ' | ' + who + ' | id ' + id + ' | ' + (/repost/i.test(ctx) ? 'repost' : 'post') +
      '\nTEXT: ' + texts[0].slice(0, 1500) + (texts[1] ? '\nQUOTED: ' + texts[1].slice(0, 800) : ''));
  });
  stale = seen.size === before ? stale + 1 : 0;
  window.scrollBy(0, 2200); await new Promise(r => setTimeout(r, 1000));
}
const all = [...seen.values()].join('\n=====\n');
const art = document.createElement('article'); const pre = document.createElement('pre');
pre.textContent = all || 'NO POSTS'; art.appendChild(pre);
document.body.innerHTML = ''; document.body.appendChild(art);
seen.size + ' posts'
