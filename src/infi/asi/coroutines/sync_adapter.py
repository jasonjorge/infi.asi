import types

def sync_call(func, *init_args, **init_kwargs):
    stack = [ func(*init_args, **init_kwargs) ]
    return sync_wait(func(*init_args, **init_kwargs))

def sync_wait(generator):
    stack = [ generator ]
    args = None
    while len(stack) > 0:
        try:
            if isinstance(args, BaseException):
                result = stack[-1].throw(args)
            else:
                result = stack[-1].send(args)
            args = None
            if isinstance(result, types.GeneratorType):
                stack.append(result)
            else:
                args = result
        except StopIteration, e:
            stack.pop()
        except BaseException, e:
            stack.pop()
            args = e
    return result
