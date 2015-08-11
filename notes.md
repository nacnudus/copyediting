# Clarifications
All PI~ journals use the PIF style.
Vancouver references use journal abbreviations from Index Medicus, which is defunct.  Use CASSI instead.

# TODO

[ ] Queries give context (e.g. name and year of references)
[ ] Name spellings consistent between the text and the references
[ ] Spellcheck (US)
[ ] LanguageTool
[ ] Abstract (single paragraph)
[ ] Consistent definitions using italics or quotes
[ ] Keywords
[ ] References (Harvard) \usepackage[sort]{natbib} \bibpunct[: ]{(}{)}{;}{a}{,}{,}
[ ] Don't query issue numbers
[ ] Appendices before references in IJR
[ ] Remove \nocites
[ ] Multimedia extension standard wording
[ ] Roman $n$th, not $n^th$
[ ] et~al
[ ] et~al.\ and other full-points in running text
[ ] acronyms
[ ] Title and headings (numbered except references etc., sentence case)
[ ] punctuation preceeded by spaces
[ ] STM addresses (authors have numbers corresponding to addresses, not vice-versa)
[ ] Full names on front page
[ ] Full name in corresponding author
[ ] i.e. e.g. not followed by spaces
[ ] Funding
[ ] Lemma, Section, equation not Lemm. Sec. Eqn.
[ ] citep/citet
[ ] Move tables to the end
[ ] \theendnotes before the funding statement.
[ ] Table
[ ] Figure 
[ ] Equations end with punctuation (IJR and MMS, otherwise comment out) (})
[ ] Contractions (wasn't -> was not) TODO: regex
[ ] Primes $p_1^{''}$ should be $p_1^{\prime\prime}$
[ ] Check all tables cited
[ ] Check all figures cited
[ ] Figures
[ ] Tables
[ ] Upright T for transpose
[ ] Upright H for Hermitian
[ ] Upright F for Fourier
[ ] \quad to separate equations
[ ] Notes (if present) > COI > Acknowledgments (if present) > Funding (mandatory)
[ ] Equation numbering runs on in the appendices
[ ] 6 and 12
[ ] cdots -> ldots
[ ] \noindent after display equations
[ ] the graph -> a graph
[ ] Lowercase after display equations continuing the sentence
[ ] 1,~2,~3 in text
[ ] Conflict of interest (MMS, JIM and WMR)
[ ] Check italics of Tr for trace of matrix
[ ] Captions end with full points
[ ] Lognotes
[ ] No coloured text
[ ] Smart quotes
[ ] Manual section letters in the appendices (and \ref), cite as Appendix \ref
[ ] Don't begin sentences with mathematics (Use 'Here, ...')
[ ] Spaces between numbers and units

# hyphens

# acronyms

# Bibliography
# The style should do all this, but 1 in 3 papers have to be fixed
# See page 17 of the Sage pdf
Order by the combination of the first letter of each surname, so
Peter Avery, Sebastien Bettel, Cedric Conroy 2010 comes before Peter Averyi, Sebastian Bettel, Alouicious Zebedee 2010
Peter Avery 2010 comes before either of those
Peter Avery 2009 comes before any of those
Another Peter Avery 2009 becomes Peter Avery 2009a and 2009b, going by which one was cited first
