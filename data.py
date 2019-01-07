nouns_dictionary = {
    'bear': 
        {'english': 
            {'singular': 'bear', 'plural': 'bears'},
        'latin': 
            {'stem': "urs", "gender": "masc"}
        },
    "wolf":
        {'english':
            {"singular": "wolf", "plural": "wolves"},
        "latin":
            {"stem": "lup", "gender": "masc"}
        },
    "horse":
        {'english':
            {"singular": "horse", "plural": "horses"},
        "latin":
            {"stem": "equ", "gender": "masc"}
        },
    "frog":
        {'english':
            {"singular": "frog", "plural": "frogs"},
        "latin":
            {"stem": "ran", "gender": "fem"}
        }
}

verbs_dictionary = {
    "love": 
        { "english": 
            {"singular": 
                {"present": "loves", "past": "loved", "future": "will love"},
            "plural":
                {"present": "love", "past": "loved", "future": "will love"}
            },
         "latin": 
            {"singular": 
                {"present": "am-a-t", "past": "am-aba-t", "future": "am-abi-t"},
            "plural":
                {"present": "am-a-nt", "past": "am-aba-nt", "future": "am-abi-nt"}
            }
        },
    "carry": 
        { "english": 
            {"singular": 
                {"present": "carries", "past": "carried", "future": "will carry"},
            "plural":
                {"present": "carry", "past": "carried", "future": "will carry"}
            },
         "latin": 
            {"singular": 
                {"present": "port-a-t", "past": "port-aba-t", "future": "port-abi-t"},
            "plural":
                {"present": "port-a-nt", "past": "port-aba-nt", "future": "port-abi-nt"}
            }
        },
    "eat": 
        { "english": 
            {"singular": 
                {"present": "eats", "past": "ate", "future": "will eat"},
            "plural":
                {"present": "eat", "past": "ate", "future": "will eat"}
            },
         "latin": 
            {"singular": 
                {"present": "vor-a-t", "past": "vor-aba-t", "future": "vor-abi-t"},
            "plural":
                {"present": "vor-a-nt", "past": "vor-aba-nt", "future": "vor-abi-nt"}
            }
        }
}

latin_noun_endings = {
    'masc': 
        {'subject': 
            {'singular': '-us', 'plural': '-i'},
        'object': 
            {'singular': "-um", "plural": "-os"}
        },
    "fem":
        {'subject': 
            {'singular': '-us', 'plural': '-i'},
        'object': 
            {'singular': "-um", "plural": "-os"}
        }
}