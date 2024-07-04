from anyio import run


def run_with_anyio(func, *args):
    return run(func, *args)
