self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
  // No cache aggressive — serve network first, fallback to cache if needed
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
