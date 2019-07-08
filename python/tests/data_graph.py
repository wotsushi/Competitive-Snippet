K4 = [
    set(),
    {2, 3, 4},
    {1, 3, 4},
    {1, 2, 4},
    {1, 2, 3}
]

sparse_graph = [
    set(),
    {2, 10},
    {1, 3},
    {2, 4},
    {3, 5},
    {4, 6},
    {5, 7},
    {6, 8},
    {7, 9},
    {8, 10},
    {9, 1}
]

no_edge_graph = [
    set(),
    set(),
    set(),
    set()
]

d_K4 = [
    set(),
    {2, 3, 4},
    {1, 3, 4},
    {1, 2, 4},
    {1, 2, 3}
]

d_sparse_graph = [
    set(),
    {2},
    {3},
    {4},
    {5},
    {6},
    {7},
    {8},
    {9},
    {10},
    {1}
]

w_K4 = [
    {},
    {
        2: 1,
        3: 3,
        4: 8
    },
    {
        1: 1,
        3: 1,
        4: 5
    },
    {
        1: 3,
        2: 1,
        4: 2
    },
    {
        1: 8,
        2: 5,
        3: 2
    }
]

w_sparse_graph = [
    {},
    {
        2: 1,
        10: 10
    },
    {
        1: 1,
        3: 2
    },
    {
        2: 2,
        4: 3
    },
    {
        3: 3,
        5: 4
    },
    {
        4: 4,
        6: 5
    },
    {
        5: 5,
        7: 6
    },
    {
        6: 6,
        8: 7
    },
    {
        7: 7,
        9: 8
    },
    {
        8: 8,
        10: 9
    },
    {
        1: 10,
        9: 9
    }
]

w_no_edge_graph = [
    {},
    {},
    {},
    {}
]

wd_K4 = [
    {},
    {
        2: 1,
        3: 3,
        4: 8
    },
    {
        1: 1,
        3: 1,
        4: 5
    },
    {
        1: 3,
        2: 1,
        4: 2
    },
    {
        1: 8,
        2: 5,
        3: 2
    }
]

wd_sparse_graph = [
    {},
    {
        2: 1
    },
    {
        3: 2
    },
    {
        4: 3
    },
    {
        5: 4
    },
    {
        6: 5
    },
    {
        7: 6
    },
    {
        8: 7
    },
    {
        9: 8
    },
    {
        10: 9
    },
    {
        1: 10
    }
]

wd_negative_weight_graph = [
    {},
    {
        2: 3,
        3: 2,
    },
    {
        3: -2
    },
    {
        1: 2,
        2: 4
    }
]

wd_zero_weight_graph = [
    {},
    {
        2: 0,
        3: 1,
    },
    {
        3: 0
    },
    {}
]

dag_line = [
    set(),
    {4},
    set(),
    {1},
    {5},
    {2}
]

dag_binary_tree = [
    set(),
    {4, 8},
    {1, 7},
    set(),
    {3},
    set(),
    set(),
    set(),
    {5, 6}
]

dag_star = [
    set(),
    {2, 3, 4, 5},
    set(),
    set(),
    set(),
    set()
]


dag_grid = [
    set(),
    {2, 4},
    {3, 5},
    {6},
    {5, 7},
    {6, 8},
    {9},
    {8},
    {9},
    set()
]
