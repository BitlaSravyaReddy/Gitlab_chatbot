import { useEffect, useState } from "react";
import { Settings2, Wifi, WifiOff } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { cn } from "@/lib/utils";
import {
  DEFAULT_API_BASE_URL,
  fetchHealth,
  normalizeBaseUrl,
  type HealthResponse,
} from "@/lib/chat-api";

type Props = {
  baseUrl: string;
  onBaseUrlChange: (url: string) => void;
};

export function SystemStatus({ baseUrl, onBaseUrlChange }: Props) {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [online, setOnline] = useState<boolean | null>(null);
  const [draft, setDraft] = useState(baseUrl);

  useEffect(() => {
    setDraft(baseUrl);
  }, [baseUrl]);

  useEffect(() => {
    let cancelled = false;
    const controller = new AbortController();

    const check = async () => {
      try {
        const result = await fetchHealth(baseUrl, controller.signal);
        if (cancelled) return;
        setHealth(result);
        setOnline(result.status === "healthy");
      } catch {
        if (cancelled) return;
        setHealth(null);
        setOnline(false);
      }
    };

    void check();
    const timer = window.setInterval(() => void check(), 30_000);

    return () => {
      cancelled = true;
      controller.abort();
      window.clearInterval(timer);
    };
  }, [baseUrl]);

  const label = online === null ? "Checking" : online ? "Online" : "Offline";

  return (
    <div className="flex items-center gap-2">
      <span
        className={cn(
          "inline-flex items-center gap-2 rounded-full border px-3 py-1.5 text-xs font-medium tracking-wide",
          online === null &&
            "border-border bg-muted text-muted-foreground",
          online === true &&
            "border-success/30 bg-success/10 text-success",
          online === false &&
            "border-destructive/30 bg-destructive/10 text-destructive",
        )}
        title={
          health?.pinecone_index
            ? `${health.vector_db ?? "Vector DB"} · index: ${health.pinecone_index}`
            : `No response from ${baseUrl}`
        }
      >
        <span
          className={cn(
            "size-2 rounded-full",
            online === null && "bg-muted-foreground",
            online === true && "animate-pulse bg-success",
            online === false && "bg-destructive",
          )}
        />
        {online ? <Wifi className="size-3.5" /> : <WifiOff className="size-3.5" />}
        {label}
      </span>

      <Popover>
        <PopoverTrigger asChild>
          <Button size="icon-sm" variant="outline" aria-label="API settings">
            <Settings2 className="size-4" />
          </Button>
        </PopoverTrigger>
        <PopoverContent align="end" className="w-80">
          <form
            className="space-y-3"
            onSubmit={(event) => {
              event.preventDefault();
              onBaseUrlChange(normalizeBaseUrl(draft) || DEFAULT_API_BASE_URL);
            }}
          >
            <div className="space-y-1.5">
              <Label htmlFor="api-base-url">API base URL</Label>
              <Input
                id="api-base-url"
                value={draft}
                spellCheck={false}
                onChange={(event) => setDraft(event.target.value)}
                placeholder={DEFAULT_API_BASE_URL}
              />
              <p className="text-xs text-muted-foreground">
                Requests go straight from your browser, so the backend must
                allow CORS from this origin.
              </p>
            </div>
            {health?.pinecone_index ? (
              <p className="text-xs text-muted-foreground">
                {health.vector_db ?? "Vector DB"} · {health.pinecone_index}
              </p>
            ) : null}
            <div className="flex justify-end gap-2">
              <Button
                type="button"
                size="sm"
                variant="ghost"
                onClick={() => setDraft(DEFAULT_API_BASE_URL)}
              >
                Reset
              </Button>
              <Button type="submit" size="sm">
                Save
              </Button>
            </div>
          </form>
        </PopoverContent>
      </Popover>
    </div>
  );
}
