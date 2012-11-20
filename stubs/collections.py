# Stubs for collections

# Based on http://docs.python.org/3.2/library/collections.html

# TODO namedtuple (requires language changes)
# TODO UserDict
# TODO UserList
# TODO UserString
# TODO abstract base classes


class deque<t>(len_t, iterable<t>):
    # TODO int with None default
    int maxlen # TODO readonly
    void __init__(self, iterable<t> iter=None, int maxlen=None): pass
    void append(self, t x): pass
    void appendleft(self, t x): pass
    void clear(self): pass
    int count(self, t x): pass
    void extend(self, iterable<t> iter): pass
    void extendleft(self, iterable<t> iter): pass
    t pop(self): pass
    t popleft(self): pass
    void remove(self, t value): pass
    void reverse(self): pass
    void rotate(self, int n): pass
    
    int __len__(self): pass
    iterator<t> __iter__(self): pass
    str __str__(self): pass
    int __hash__(self): pass
    
    t __getitem__(self, int i): pass
    void __setitem__(self, int i, t x): pass
    bool __contains__(self, t o): pass

    # TODO __reversed__

    
class Counter<t>(dict<t, int>):
    void __init__(self): pass
    void __init__(self, mapping<t, int> mapping): pass
    void __init__(self, iterable<t> iter): pass
    # TODO keyword arguments
    iterator<t> elements(self): pass
    list<t> most_common(self): pass
    list<t> most_common(self, int n): pass
    void subtract(self, mapping<t, int> mapping): pass
    void subtract(self, iterable<t> iter): pass
    # TODO update


class OrderedDict<kt, vt>(dict<kt, vt>):
    tuple<kt, vt> popitem(self, bool last=True): pass
    void move_to_end(self, kt key, bool last=True): pass


class defaultdict<kt, vt>(dict<kt, vt>):
    func<vt> default_factory
    void __init__(self): pass
    void __init__(self, mapping<kt, vt> map): pass
    void __init__(self, iterable<tuple<kt, vt>> iter): pass
    void __init__(self, func<vt> default_factory): pass
    void __init__(self, func<vt> default_factory, mapping<kt, vt> map): pass
    void __init__(self, func<vt> default_factory,
                  iterable<tuple<kt, vt>> iter): pass
    # TODO __init__ keyword args
    vt __missing__(self, kt key): pass
    # TODO __reversed__