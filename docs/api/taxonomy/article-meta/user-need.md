# User Need

User need metadata (`meta_type=user_need`) describes why a reader would seek out or value the story. It captures the dominant audience need the story serves, not the article's subject, format, timeframe, or scope.

## Filter

```text
?meta=user_need:explain_it_to_me
```

Discover values in your project with `user_need_categories` from [Article facets](../../articles/facets.md) or `GET …/articles/metadata/types/user_need/values`.

## Categories

| API value | Meaning |
| --- | --- |
| `update_me` | Provides timely information about what happened, what changed, or what was announced |
| `explain_it_to_me` | Helps the reader understand what something means, how it works, why it matters, or what context is needed |
| `help_me_act` | Gives practical information to make a decision, solve a problem, access a resource, or take action |
| `hold_power_to_account` | Investigates, scrutinizes, or challenges people, institutions, systems, or decisions with power over public life |
| `show_me_the_community` | Helps the reader understand the people, places, institutions, traditions, and shared life of a community |
| `move_me` | Creates emotional connection through human experience, narrative, surprise, grief, joy, resilience, or meaning |
| `entertain_me` | Gives enjoyment, diversion, recommendations, cultural discovery, or something interesting to talk about |
| `catch_me_up` | Orients the reader within an ongoing story, controversy, process, campaign, trial, project, or public conversation |
| `other` | The article does not clearly serve one of the standard user needs |

## Related

- [Article Meta overview](index.md)
- [Format](format.md)
- [Timeframe](timeframe.md)
