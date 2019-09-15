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
doc = doc_med('test doc')
print("Document attribute: ", doc.attribute)
print("Document prop: text: ", doc.text)
print("Document prop: tokens: ", doc.tokens)
# print("Document prop: count_words", doc.count_words)

doc_tokens = iter(doc.tokens)
print(doc_tokens)

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

