// Save the collected posts of this search page as one text file in the browser download directory.
const S = window.__xc;
const q = new URLSearchParams(location.search).get('q') || '';
const m = q.match(/^from:(\w{1,15}) since:(\d{4}-\d{2}-\d{2}) until:(\d{4}-\d{2}-\d{2})$/);
let out;
if (!m) out = 'NOT SAVED not a backfill page';
else if (!S || !/^DONE/.test(S.last || '')) out = 'NOT SAVED scroll is not done';
else {
  const body = S.seen.size ? [...S.seen.values()].join('\n=====\n') : 'NO POSTS';
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([body + '\n'], { type: 'text/plain' }));
  a.download = 'xc__' + m[1] + '__' + m[2] + '__' + m[3] + '.txt';
  document.body.appendChild(a); a.click(); a.remove();
  await new Promise(r => setTimeout(r, 1500));
  out = 'SAVED ' + S.seen.size;
}
out
