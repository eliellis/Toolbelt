class Toolbelt(object):

    # def __init__(self):
        # not much to initialize at this point

    def reduce(self, fn):
        def iterate(*args):
            i = iter(args)
            try:
                start = next(i)
            except Exception, e:
                raise e
            val = start
            for item in i:
                val = fn(val, item)
            return val

        return iterate

    def map(self, fn):
        def iterate(*args, **kwargs):
            return [fn(val) for val in args] + [fn(val, key) for key, val in kwargs.iteritems()]
        return iterate
