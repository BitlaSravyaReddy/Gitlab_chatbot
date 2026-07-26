import { useState } from "react";
import { ChevronRight, FileText } from "lucide-react";

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { cn } from "@/lib/utils";
import type { ChatSource } from "@/lib/chat-api";

export function SourcesPanel({ sources }: { sources: ChatSource[] }) {
  const [open, setOpen] = useState(false);

  if (!sources.length) return null;

  return (
    <Collapsible open={open} onOpenChange={setOpen} className="mt-3">
      <CollapsibleTrigger className="inline-flex items-center gap-1.5 rounded-md border border-border bg-card px-2.5 py-1.5 text-xs font-medium text-muted-foreground transition-colors hover:bg-accent hover:text-accent-foreground">
        <ChevronRight
          className={cn("size-3.5 transition-transform", open && "rotate-90")}
        />
        <FileText className="size-3.5" />
        Sources ({sources.length})
      </CollapsibleTrigger>
      <CollapsibleContent className="mt-2 space-y-2">
        {sources.map((source, index) => (
          <article
            key={`${source.section}-${index}`}
            className="rounded-lg border border-border bg-card p-3"
          >
            <div className="flex flex-wrap items-center gap-2">
              <span className="rounded-full bg-accent px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wider text-accent-foreground">
                {source.source}
              </span>
              <span className="font-mono text-xs text-muted-foreground break-all">
                {source.section}
              </span>
            </div>
            <p className="mt-2 whitespace-pre-wrap border-l-2 border-primary/40 pl-3 text-xs leading-relaxed text-foreground/80">
              {source.snippet}
            </p>
          </article>
        ))}
      </CollapsibleContent>
    </Collapsible>
  );
}
