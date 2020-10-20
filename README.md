# LC
- An interpreter for the lambda calculus.
- Each expression is transformed into an equivalent Python one.
- It's small, but it can compute anything!
- I included a few functions to get started with if you want to try it out: `id`, `true`, `false`, `if`, `and`, `or`, and `not`.
- Here's an example of what it can do:
```
λ
> middle = \x. \y. \z. y
> middle 1 2 3
2
> running = true
> if running 10 20
10
>
```
