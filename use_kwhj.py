# import classes
from first_package.src.documentmedia import DocumentMedia as doc_med
from first_package.src.socialmedia import SocialMedia as soc_med

# import package methods
from first_package.src.utils import we_need_to_talk
from first_package.src.utils import sum_counters
from first_package.src.utils import plot_counter

# import external iterables (lists, tuples, dicts)
from repository_lists import word_counts


# utils.py - methods
# -------------------------------------------------------------------
# # Decide to start seeing other people
we_need_to_talk(break_up=False)


# -------------------------------------------------------------------
# Sum word_counts using sum_counters from text_analyzer
word_count_totals = sum_counters(word_counts)
print("word_count_totals: ", word_count_totals)


# -------------------------------------------------------------------
plot_counter(word_count_totals, 10)

# ===================================================================


# documentmedia.py 
# -------------------------------------------------------------------
doc = doc_med('test doc')
print(doc.tokens)

# ===================================================================


# socialmedia.py 
# -------------------------------------------------------------------
# Create a SocialMedia instance with datacamp_tweets
# dc_tweets = soc_med(text=datacamp_tweets)

# ===================================================================

