from d import run_with_anyio


def run_with_d(func, *args):
    return run_with_anyio(func, *args)
