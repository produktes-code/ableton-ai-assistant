function renderTracks(tracks) {
  const container = document.getElementById('tracks-view');
  if (!container) return;
  container.innerHTML = '';
  
  const limited = (tracks || []).slice(0, 20);
  for (const track of limited) {
    const div = document.createElement('div');
    div.className = 'track-item';
    div.textContent = `${track.name || 'Track'}`;
    container.appendChild(div);
  }
}

function updateQueueCount(n) {
  const el = document.getElementById('queue-count');
  if (el) el.textContent = n;
}
