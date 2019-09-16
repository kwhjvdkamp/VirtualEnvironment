from collections import Counter

from firstpackage.src.documentmedia import DocumentMedia as doc_med

# # Tests on Document object
# # -------------------------------------------------------------------
# # blank document
# def test_document_empty():
#     doc = doc_med('')
#     assert doc.tokens != []  # Test Pass
#       assert doc.tokens == []  # Test Fails, because
#       # checking an empty document delivers a generator object (doc.tokens) 
#       # which itself apparently is an empty 'box' (if I may say so) 
#       # which is not equal to an empyt list
#       # Whats the purpose of this test?
#     assert doc.word_counts == Counter({}) # Test Pass, 
#       # seems obvious, no word counted compared to the Counter-object which is empty


# ------------------------------------------------------------------- 
# attribute
def test_document_tokens():
    doc = doc_med('a e i o u')
    assert doc.tokens == ['a', 'e', 'i', 'o', 'u']   # I expect this assert as True >> pytest -v says False ???

  
# # ------------------------------------------------------------------- 
# # attribute
# def test_document_word_counts():
#     doc = doc_med('a e i o u')
#     assert doc.word_counts == ['a', 'e', 'i', 'o', 'u']

#     # doc = Document('This is a test, this is a test')
#     # assert doc.word_counts == Counter({'is': 2, 'a': 2, 'test': 2, 'This': 1, 'this': 1})

# # ===================================================================