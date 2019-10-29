# import classes
from firstpackage.src.documentmedia import DocumentMedia as doc_med
from firstpackage.src.socialmedia import SocialMedia as soc_med

# import package methods
from firstpackage.src.utils import we_need_to_talk
from firstpackage.src.utils import sum_counters
from firstpackage.src.utils import plot_counter

# import external iterables (lists, tuples, dicts)
from repository_lists import word_counts


# utils.py - methods
# -------------------------------------------------------------------
# # Decide to start seeing other people
break_up = True

we_need_to_talk(break_up)

# ===================================================================


# documentmedia.py 
# -------------------------------------------------------------------
# doc = doc_med('test doc')
doc = doc_med('a e i o u')

print("DocumentMedia \'attribute\': ", doc.attribute)

print("DocumentMedia property \'text\': ", doc.text)
print("DocumentMedia property: \'tokens\': ", list(doc.tokens))
print("DocumentMedia property: \'count_words\': ", doc.word_counts)
# INPUT: 'test doc'
# OUTPUT: 
# Document prop: count_words: 
# Counter({ 
#   Tok(kind=11001, txt=None, val=(0, None)): 1, 
#   Tok(kind=6, txt='test', val=None): 1, 
#   Tok(kind=6, txt='doc', val=None): 1, 
#   Tok(kind=11002, txt=None, val=None): 1})

# INPUT: 'a e i o u'
# DocumentMedia property: 'count_words':  
# Counter({
#   Tok(kind=11001, txt=None, val=(0, None)): 1, 
#   Tok(kind=6, txt='a', val=None): 1, 
#   Tok(kind=6, txt='e', val=None): 1, 
#   Tok(kind=6, txt='i', val=None): 1, 
#   Tok(kind=6, txt='o', val=None): 1, 
#   Tok(kind=6, txt='u', val=None): 1, 
#   Tok(kind=11002, txt=None, val=None): 1})

doc_tokens = iter(doc.tokens)
print(next(doc_tokens))

# ===================================================================


# utils.py
# -------------------------------------------------------------------
# Sum word_counts using sum_counters from text_analyzer
word_count_totals = sum_counters(word_counts)
# print("word_count_totals: ", word_count_totals)


# -------------------------------------------------------------------
plot_counter(word_count_totals, 10)

# ===================================================================


# documentmedia.py 
# -------------------------------------------------------------------
doc = doc_med('test doc')
print("Document: ", doc.tokens, doc.attribute)

# ===================================================================


# socialmedia.py 
# -------------------------------------------------------------------
# Create a SocialMedia instance with datacamp_tweets
# dc_tweets = soc_med(text=datacamp_tweets)

# ===================================================================

