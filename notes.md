start 18:30
pause 11:30
start 18:10
pause 19:35
start 19:50
pause 21:55
start 22:20
pause 23:30
start 08:25
ended 11:00

words   16509
tables  2
figures 18
minutes 435 + 300 for biblatex

# TODO

[x] Check activity log
[x] Naming convention ABC123456_ed
[x] Check italics of Tr for trace of matrix
[x] 6 and 12
[x] 1,~2,~3 in text
[x] minus signs in text and tables
[x] Equations end with punctuation (IJR and MMS, otherwise comment out) (})
[x] Lowercase after display equations continuing the sentence
[x] \noindent after display equations
[x] Don't begin sentences with mathematics (Use 'Here, ...')
[x] \quad to separate equations
[x] Changes to figures – instructions to typesetter (CL) not author queries
[x] Time format should be 09:00, 13:45 etc. Date format is 12 December 2010
[x] Oxford commas in US only, and then consistently if at all
[x] 1.7E-05 -> 1.7×10–5 (todo: regex \text{\sc{e}-}5)
[x] Replace grave, acute, hat, bar, and so on, with proper accents/diacritics
[x] Regex
[x] acronyms (redefine in captions and abstract)
[x] hyphenations
[x] Remove \nocites
[x] the graph -> a graph
[x] Consistent definitions using italics or quotes (called, known as, termed)
[x] Contractions (wasn't -> was not) 're 'll 've 'd 't
[x] Captions end with full points
[x] Capital B for Bessel
[x] Capital B for Boolean
[x] Capital C for Cauchy
[x] Capital C for Cartesian
[x] Capital C for Coriolis
[x] Capital C for Coulomb
[x] Capital D for Dirac
[x] Capital D for Doppler
[x] Capital E for Euclid
[x] Capital F for Fourier
[x] Capital H for Hessian
[x] Capital G for Gauss(ian)
[x] Capital J for Jacobian
[x] Capital L for Lagrangian
[x] Capital L for Laplace
[x] Capital L for Lebesgue
[x] Capital L for Lie derivative
[x] Capital N for Newton
[x] Capital P for Poisson
[x] Upright H for Hermitian
[x] X-ray unless at the start of the sentence in which case X-Ray x.\?ray
[x] Addresses (authors have numbers corresponding to addresses, not vice-versa)
[x] Corresponding author (no titles/positions)
[x] Email
[x] Full names on front page
[x] Full name in corresponding author
[x] Title and headings (numbered except references etc., sentence case) (use ]] or ,t, not <space>t or you will miss subsubsections)
[x] Main edit
[x] Abstract (single paragraph)
[x] Keywords
[x] Acknowledgments
[x] Acknowledgments (if present) > DCI (if present/mandatory) > Funding (mandatory) > Notes > References > Appendices (except IJR, when references follow the appendices, note multimedia extensions are the first appendix)
[x] Conflict of interest (JIM and WMR)
[x] Funding
[x] \theendnotes before the funding statement.
[x] Appendices -- manual section numbers in the appendices (and \ref), cite as Appendix \ref
[x] Equation numbering runs on in the appendices
[x] Biographies
[x] Multimedia extension standard wording
[x] Check all tables cited
[x] Check all figures cited
[x] Check all references referred to
[x] References (Harvard) \usepackage[sort]{natbib} \bibpunct[: ]{(}{)}{;}{a}{,}{,}
[x] -- in the references (see regex)
[x] Remove DOIs, URLs and ISBNs unless ahead of print
[x] Queries give context (e.g. name and year of references)
[x] Don't query issue numbers
[x] Name spellings consistent between the text and the references
[x] Spellcheck (UK ,Sg) set spellfile=./local.utf-8.add
[x] iz/is
[x] LanguageTool
[x] Lognotes
[x] Move tables to the end
[x] Return articles by 3pm on the due date

# hyphens
setup / set up / set-up
well known / well-known
turnout/turn out/turnouts
non-
bi-

# acronyms

# Bibliography
# The style should do all this, but 1 in 3 papers have to be fixed
# See page 17 of the Sage pdf
Order by the combination of the first letter of each surname, so
Peter Avery, Sebastien Bettel, Cedric Conroy 2010 comes before Peter Avery, Sebastian Bettel, Alouicious Zebedee 2010
Peter Avery 2010 comes before either of those
Peter Avery 2009 comes before any of those
Another Peter Avery 2009 becomes Peter Avery 2009a and 2009b, going by which one was cited first
