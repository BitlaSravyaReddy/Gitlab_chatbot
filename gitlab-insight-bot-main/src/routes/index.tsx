import { useCallback, useEffect, useRef, useState } from "react";
import { createFileRoute } from "@tanstack/react-router";
import { AlertTriangle, RotateCcw, User } from "lucide-react";
import { toast, Toaster } from "sonner";

import assistantMark from "@/assets/assistant-mark.png";
import {
  Conversation,
  ConversationContent,
  ConversationScrollButton,
} from "@/components/ai-elements/conversation";
import {
  Message,
  MessageContent,
  MessageResponse,
} from "@/components/ai-elements/message";
import {
  PromptInput,
  PromptInputFooter,
  PromptInputSubmit,
  PromptInputTextarea,
  PromptInputTools,
} from "@/components/ai-elements/prompt-input";
import { Shimmer } from "@/components/ai-elements/shimmer";
import { SourcesPanel } from "@/components/chat/sources-panel";
import { Button } from "@/components/ui/button";
import {
  askQuestion,
  type ChatSource,
} from "@/lib/chat-api";

const TITLE = "GitLab Handbook & Direction AI Assistant";
const DESCRIPTION =
  "Ask questions about GitLab's Handbook, culture, and product direction. Answers are grounded in retrieved handbook sources via Pinecone DB and Gemini AI.";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "GitLab Handbook & Direction AI Assistant" },
      { name: "description", content: DESCRIPTION },
      { property: "og:title", content: TITLE },
      { property: "og:description", content: DESCRIPTION },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: ChatPage,
});

const SUGGESTIONS = [
  "What are GitLab's core values?",
  "Explain GitLab's remote work principles",
  "What is GitLab's strategy for FY25?",
];

type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  text: string;
  sources?: ChatSource[];
  error?: boolean;
};

function ChatPage() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    textareaRef.current?.focus();
  }, []);

  const send = useCallback(
    async (question: string) => {
      const trimmed = question.trim();
      if (!trimmed || loading) return;

      const userMessage: ChatMessage = {
        id: `u-${Date.now()}`,
        role: "user",
        text: trimmed,
      };
      setMessages((prev) => [...prev, userMessage]);
      setInput("");
      setLoading(true);

      try {
        const result = await askQuestion(trimmed);
        setMessages((prev) => [
          ...prev,
          {
            id: `a-${Date.now()}`,
            role: "assistant",
            text: result.answer || "_No answer was returned._",
            sources: result.sources,
          },
        ]);
      } catch (error) {
        const detail =
          error instanceof Error ? error.message : "Unknown error";
        setMessages((prev) => [
          ...prev,
          {
            id: `e-${Date.now()}`,
            role: "assistant",
            text: `Something went wrong. Please try again.\n\n${detail}`,
            error: true,
          },
        ]);
        setInput(trimmed);
        toast.error("Request failed", { description: detail });
      } finally {
        setLoading(false);
        requestAnimationFrame(() => textareaRef.current?.focus());
      }
    },
    [loading],
  );

  const clearChat = useCallback(() => {
    setMessages([]);
    setInput("");
    textareaRef.current?.focus();
  }, []);

  return (
    <div className="flex h-screen flex-col bg-background text-foreground">
      <Toaster position="top-center" richColors />

      {/* ── Header ── */}
      <header className="flex items-center justify-between gap-3 border-b border-border/60 bg-card/80 px-5 py-3.5 backdrop-blur-xl sm:px-8">
        <div className="flex items-center gap-3.5">
          <div className="flex size-9 shrink-0 items-center justify-center rounded-xl bg-primary shadow-sm shadow-primary/30">
            <img
              src={assistantMark}
              alt=""
              width={512}
              height={512}
              className="size-6 brightness-0 invert"
            />
          </div>
          <div>
            <h1 className="text-[15px] font-semibold leading-tight tracking-tight text-foreground">
              GitLab AI Assistant
            </h1>
            <p className="text-[11px] font-medium tracking-wide text-muted-foreground/80">
              Handbook · Direction · Culture
            </p>
          </div>
        </div>
        {messages.length > 0 && (
          <Button
            type="button"
            size="sm"
            variant="ghost"
            onClick={clearChat}
            disabled={loading}
            className="gap-1.5 text-xs text-muted-foreground hover:text-foreground"
          >
            <RotateCcw className="size-3.5" />
            Clear
          </Button>
        )}
      </header>

      {/* ── Conversation ── */}
      <Conversation className="flex-1">
        <ConversationContent className="mx-auto w-full max-w-2xl gap-6 py-8 px-4">
          {messages.length === 0 ? (
            <div className="flex flex-1 flex-col items-center justify-center gap-6 py-20 text-center">
              {/* Hero icon */}
              <div className="flex size-20 items-center justify-center rounded-3xl bg-primary/10 ring-1 ring-primary/20 shadow-xl shadow-primary/10">
                <img
                  src={assistantMark}
                  alt=""
                  width={512}
                  height={512}
                  loading="lazy"
                  className="size-10 opacity-90"
                />
              </div>

              <div className="space-y-2">
                <h2 className="text-2xl font-semibold tracking-tight text-foreground">
                  Ask the handbook anything
                </h2>
                <p className="mx-auto max-w-sm text-sm leading-relaxed text-muted-foreground">
                  Grounded answers from GitLab&apos;s Handbook and Direction
                  pages, with exact source sections attached.
                </p>
              </div>

              {/* Suggestion chips */}
              <div className="flex flex-wrap justify-center gap-2 pt-1">
                {SUGGESTIONS.map((suggestion) => (
                  <button
                    key={suggestion}
                    type="button"
                    onClick={() => void send(suggestion)}
                    className="rounded-full border border-border/80 bg-card px-4 py-2 text-sm text-foreground/80 transition-all duration-200 hover:border-primary/40 hover:bg-primary/5 hover:text-foreground hover:shadow-sm active:scale-95"
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            </div>
          ) : null}

          {messages.map((message) => (
            <Message key={message.id} from={message.role}>
              <div className="flex items-start gap-3">
                {message.role === "assistant" ? (
                  <div className="mt-0.5 flex size-7 shrink-0 items-center justify-center rounded-lg bg-primary/10 ring-1 ring-primary/20">
                    <img
                      src={assistantMark}
                      alt="Assistant"
                      width={512}
                      height={512}
                      loading="lazy"
                      className="size-4 opacity-90"
                    />
                  </div>
                ) : null}
                <div className="min-w-0 flex-1">
                  <MessageContent
                    className={
                      message.error
                        ? "rounded-xl border border-destructive/30 bg-destructive/8 px-4 py-3 text-destructive"
                        : undefined
                    }
                  >
                    {message.role === "assistant" ? (
                      <div className="flex items-start gap-2">
                        {message.error ? (
                          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
                        ) : null}
                        <MessageResponse className="leading-relaxed [&_h1]:font-display [&_h2]:font-display [&_h3]:font-display [&_li]:my-1 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ul_ul]:list-[circle]">
                          {message.text}
                        </MessageResponse>
                      </div>
                    ) : (
                      <p className="whitespace-pre-wrap text-sm leading-relaxed">
                        {message.text}
                      </p>
                    )}
                  </MessageContent>
                  {message.role === "assistant" && message.sources ? (
                    <SourcesPanel sources={message.sources} />
                  ) : null}
                </div>
                {message.role === "user" ? (
                  <span className="mt-0.5 flex size-7 shrink-0 items-center justify-center rounded-lg bg-secondary ring-1 ring-border/50">
                    <User className="size-3.5 text-muted-foreground" />
                  </span>
                ) : null}
              </div>
            </Message>
          ))}

          {loading ? (
            <Message from="assistant">
              <div className="flex items-center gap-3">
                <div className="mt-0.5 flex size-7 shrink-0 items-center justify-center rounded-lg bg-primary/10 ring-1 ring-primary/20">
                  <img
                    src={assistantMark}
                    alt=""
                    width={512}
                    height={512}
                    loading="lazy"
                    className="size-4 animate-pulse opacity-80"
                  />
                </div>
                <Shimmer className="text-sm text-muted-foreground">
                  Searching the handbook...
                </Shimmer>
              </div>
            </Message>
          ) : null}
        </ConversationContent>
        <ConversationScrollButton />
      </Conversation>

      {/* ── Input ── */}
      <div className="border-t border-border/60 bg-card/80 px-4 py-4 backdrop-blur-xl sm:px-8">
        <div className="mx-auto w-full max-w-2xl space-y-2.5">
          {messages.length > 0 ? (
            <div className="flex flex-wrap gap-1.5">
              {SUGGESTIONS.map((suggestion) => (
                <button
                  key={suggestion}
                  type="button"
                  disabled={loading}
                  onClick={() => void send(suggestion)}
                  className="rounded-full border border-border/70 bg-background px-3 py-1.5 text-xs text-muted-foreground transition-all duration-200 hover:border-primary/40 hover:text-foreground disabled:opacity-40 active:scale-95"
                >
                  {suggestion}
                </button>
              ))}
            </div>
          ) : null}

          <PromptInput
            onSubmit={(_message, event) => {
              event.preventDefault();
              void send(input);
            }}
          >
            <PromptInputTextarea
              ref={textareaRef}
              value={input}
              onChange={(event) => setInput(event.target.value)}
              placeholder="Ask anything about GitLab's Handbook, culture, or product direction..."
            />
            <PromptInputFooter>
              <PromptInputTools>
                <span className="text-[11px] text-muted-foreground/60 select-none">
                  Powered by Pinecone · Gemini AI
                </span>
              </PromptInputTools>
              <PromptInputSubmit
                status={loading ? "submitted" : undefined}
                disabled={loading || !input.trim()}
              />
            </PromptInputFooter>
          </PromptInput>
        </div>
      </div>
    </div>
  );
}
