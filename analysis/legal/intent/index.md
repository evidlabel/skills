
# how to analyze intent

```mermaid
stateDiagram-v2
  state "The formal and informal weight placed on intent" as Weight
  state "A route by which to establish intent" as Route

  [*] --> Weight
  Weight --> Route
  Route --> Route: the route, and what it shows
  Route --> [*]: the weight is stated, and the routes are mapped
```

- figure out formal and informal weight placed on intent
- map out all routes by which to establish intent, including but not limited to
  - presence of actions that align with intent
  - previously held similar intent
  - written/witnessed/recorded expressions of intent
  - surrounding facts align with intent
  - etc 
