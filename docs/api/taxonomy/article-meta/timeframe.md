# Timeframe

Timeframe metadata (`meta_type=temporal_orientation`) describes how the story relates to time: future, present, past, ongoing trends, recurring cycles, or timeless relevance.

## Filter

```text
?meta=temporal_orientation:ongoing
```

Discover values in your project with `GET …/articles/metadata/types/temporal_orientation/values`.

## Categories

| API value | Meaning |
| --- | --- |
| `future` | Oriented toward events, decisions, or conditions that have not yet happened |
| `present` | Centered on something happening now or that just happened in a non-breaking way |
| `past` | Looks backward at events that already happened, including consequences, analysis, or reflection |
| `ongoing` | Covers a durational phenomenon without a single defining event |
| `cyclical` | Concerns recurring or seasonal patterns on a predictable cadence |
| `evergreen` | Not tied to a particular timeframe; remains relevant whenever it is read |
| `other` | No clear temporal orientation, or mixed timeframes obscure the dominant one |

## Related

- [Article Meta overview](index.md)
- [Scope](scope.md)
- [User need](user-need.md)
