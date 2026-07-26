## GitLab Handbook & Direction AI Assistant

A single-page chat app that talks directly to your FastAPI backend from the browser. Base URL is configurable (default `http://127.0.0.1:8000`), stored in the browser so you can point it anywhere. No conversation persistence — refresh or "Clear Chat" starts fresh.

### Screen layout (all at `/`)

```text
┌──────────────────────────────────────────────────────────┐
│ [logo] GitLab Handbook & Direction AI Assistant  ● Online│
│        Powered by Pinecone DB & Gemini AI        [⚙ URL] │
├──────────────────────────────────────────────────────────┤
│  ┌ empty state: logo + 3 suggestion chips ┐              │
│  User bubble ...........................  [avatar]       │
│  [bot] Assistant markdown answer                         │
│        ▸ Sources (8)   ← collapsed accordion             │
│            source · section · snippet                    │
├──────────────────────────────────────────────────────────┤
│ [chips: core values | remote work | FY25 strategy]       │
│ [ Ask anything about GitLab's Handbook... ]  [↺] [send]  │
└──────────────────────────────────────────────────────────┘
```

### Behaviour

- **Header status badge** — polls `GET {base}/health` on load and every 30s. Green "Online" when `status: "healthy"` (shows index name in a tooltip), red "Offline" on error. A small settings popover lets you edit the API base URL; it's saved to localStorage and re-checks health immediately.
- **Send** — `POST {base}/chat` with `{ question }`. Optimistic user bubble appears instantly, then an animated "Thinking…" shimmer until the answer arrives.
- **Assistant messages** — rendered as markdown (bold, bullets, inline/blocks of code) via `react-markdown`, no bubble background; user messages get a filled high-contrast bubble.
- **Sources** — collapsed-by-default accordion under each answer, one card per source showing Source, Section Title, and the content snippet in a readable monospace-ish block.
- **Suggestion chips** — three sample questions above the input, visible in the empty state and as a compact row above the composer; clicking one sends it.
- **Clear Chat** — resets the transcript, refocuses the input.
- **Errors** — network failure / CORS / non-200 shows an inline error message in the transcript plus a toast, with the user's text preserved so they can retry.
- Input stays focused on load, after sending, and after clearing.

### Design direction

Not the generic purple-gradient look: warm GitLab-adjacent palette (deep charcoal ink, tangerine/amber accent) on an off-white surface, dark mode included. Distinctive display typeface for the header, clean sans for body. Semantic tokens only, defined in `src/styles.css`.

### Technical notes

- Rewrite `src/routes/index.tsx` as the chat page with its own SEO head() (title, description, og/twitter).
- Chat UI built from AI Elements primitives (`conversation`, `message`, `prompt-input`, `shimmer`) installed into the project; sources accordion uses shadcn `collapsible`.
- Client-side `fetch` straight to the configured base URL — nothing server-side, so your FastAPI app needs CORS enabled for the preview origin (`allow_origins=["*"]` while developing). I'll note this in the UI's offline hint.
- Small modules: `src/lib/chat-api.ts` (types + fetch calls + base-URL storage), `src/components/chat/*` for message, sources, composer, status badge.
- Generated bot/brand mark image instead of a generic sparkle icon.
