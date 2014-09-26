from contextlib import contextmanager
import pygame as pg


@contextmanager
def pginit():
    try:
        pg.init()
        yield
    except:
        raise
    finally:
        pg.quit()
