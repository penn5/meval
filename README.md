# meval

Evaluates python strings as async code

## Usage

```python
# inside an `async def`
from meval import meval
await meval("await thing", globals(), thing=my_function(arg=1))
```

## License

MIT
