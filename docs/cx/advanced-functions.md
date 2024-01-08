# Advanced Functions
## Callbacks
### Subscribe/Unsubscribe
`callback [action] +/-= ctx -> [function](ctx)`
- `callback`: Callback keyword. Tells the language that this is a callback. (KEYWORD)
- `[action]`: The action object (for instance, keypress, CALLBACK.ACTION)
- `+/-=`: Assigns/unassigns the event context/callback (ASSIGNMENT.OPERATOR)
- `ctx`: Event context (for instance, for keyboard.key_pressed, the context might be what time and which key. VARIABLE)
- `->`: Callback sign. (CALLBACK.SIGN)
- `[function](ctx)`: The function to be performed on the event. (CTX is an arg. CALLBACK.FUNCTION)
### Trigger
`trigger [action]`
- `trigger`: Trigger keyword. (KEYWORD)
- `[action]`: Action to trigger which activates all callbacks.
