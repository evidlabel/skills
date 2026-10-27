
# how to analyze intent

```mermaid
stateDiagram-v2
  state "The formal and informal weight placed on intent" as Weight
  state "One route by which to establish intent, and what the record shows on it" as Route

  [*] --> Weight
  Weight --> Route
  Route --> Route: a route is left
  Route --> [*]: every route is mapped
```

- figure out formal and informal weight placed on intent
- map out all routes by which to establish intent, including but not limited to
  - presence of actions that align with intent
  - previously held similar intent
  - written/witnessed/recorded expressions of intent
  - surrounding facts align with intent
  - etc 
