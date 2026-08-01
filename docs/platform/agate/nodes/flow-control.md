# Flow control nodes

**Flow control nodes** shape how data moves through a [flow](../flows.md). They can be useful when a flow branches into several paths that you later need to bring back together.

| Node | What it does |
| --- | --- |
| **Gather** | Combines the results of several upstream steps into a single, organized bundle |

## Why Gather exists

Branches let independent work happen from the same article. A flow might
extract people, organizations, and places on three branches. If a later output
needs all three result sets together, Gather provides one point where those
branches rejoin.

Gather does not interpret, deduplicate, or editorially approve the values. It
preserves the named upstream results in a combined structure so a downstream
step can consume them.

## When to use it

Use Gather when the guided builder indicates that a later node needs several
branches as one input. Do not add it merely to make the diagram look linear:
branches that can feed the output independently may not need a gather step.

Like other deterministic nodes, Gather does not require an AI model. Its output
can be inspected in a completed run when the node panel exposes an Output tab.
