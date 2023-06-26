
# [Voikko](https://github.com/voikko/corevoikko)

- Voikko is a package providing linguistic data and grammar checking for the Finnish language.
- [Libvoikko](https://github.com/voikko/corevoikko) is its open source functional core. 
- compatible with some generic spellcheckers
	- enchant, sonnet (Qt5)
- instructions
	-  https://voikko.puimula.org/python.html
- [Various dictionaries](https://www.puimula.org/htp/testing/voikko-snapshot-v5/) - need 1 for it to function
- Use voikko [tests](https://github.com/voikko/corevoikko/tree/master/tests) for inspecting new words for accuracy, works with compound words
- Finite State Transducer (FST) codes
	```
	! Voikko-fi, description of Finnish language morphology.
	!
	! Copyright © 2006 - 2016 Hannu Väisänen (Firstname.Lastname@joensuu.fi)
	!                 2006 - 2015 Harri Pitkänen (hatapitk@iki.fi)
	!
	! This program is free software; you can redistribute it and/or modify
	! it under the terms of the GNU General Public License as published by
	! the Free Software Foundation; either version 2, or (at your option)
	! any later version.
	!
	! This program is distributed in the hope that it will be useful, but
	! WITHOUT ANY WARRANTY; without even the implied warranty of
	! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
	! General Public License for more details.
	!
	! You should have received a copy of the GNU General Public License
	! along with this program; see the file COPYING.  If not, write to the
	! Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
	! 02110-1301, USA.
	
	Multichar_Symbols
	
	! Parts of speech
	[Ln]  ! noun
	[Lee] ! proper noun - first name
	[Les] ! proper noun - last name
	[Lep] ! proper noun - place name
	[Lem] ! proper noun - other proper noun
	[Ll]  ! adjective
	[Lnl] ! nominal adjective
	[Lt]  ! verb
	[Lh]  ! interjection
	[Lp]  ! prefix
	[La]  ! abbreviation
	[Ls]  ! adverb
	[Lc]  ! conjunction
	[Lu]  ! numeral
	[Lur] ! numeral (roman)
	[Lr]  ! postposition
	[Ld]  ! preposition
	[Lk]  ! negation
	
	! Vowel harmony
	[Va]
	[Vä]
	[Vaä]
	
	! String parameters
	[Xp]  ! base form
	[Xj]  ! stem base form
	[Xr]  ! structure
	[Xs]  ! sourceid
	[X]   ! end character of parameter
	
	! Cases
	[Sn]   ! nominative
	[Sg]   ! genitive
	[Sp]   ! partitive
	[Ses]  ! essive
	[Str]  ! translative
	[Sine] ! inessive
	[Sela] ! elative
	[Sill] ! illative
	[Sade] ! adessive
	[Sabl] ! ablative
	[Sall] ! allative
	[Sab]  ! abessive
	[Sko]  ! comitative
	[Sin]  ! instructive
	[Ssti] ! narrative_sti
	[Sak]  ! accusative
	
	! Numbers
	[Ny]  ! singular
	[Nm]  ! plural
	
	! Possessive suffixes
	[O1y] ! singular 1st person
	[O2y] ! singular 2nd person
	[O1m] ! plural 1st person
	[O2m] ! plural 2nd person
	[O3]  ! singular/plural 3rd person
	
	! Comparative forms
	[Cc] ! comparative
	[Cs] ! superlative
	
	! Enclitics
	[Fkin]  ! -kin
	[Fkaan] ! -kaan
	[Fko]   ! question particle ko/kö
	
	! Moods
	[Tn1] ! 1st infinitive
	[Tn2] ! 2nd infinitive
	[Tn3] ! 3rd infinitive
	[Tn4] ! 4th infinitive
	[Tn5] ! 5th infinitive
	[Tk1] ! 1st imperative
	[Tk2] ! 2nd imperative
	[Tp]  ! participle
	[Te]  ! e-infinitive
	[Tma] ! mA-infinitive
	[Tpe] ! passive present participle
	[Tpa] ! active past participle
	[Tna] ! active present participle
	
	! Other flags
	[Z]  ! unknown word
	[Zy] ! compound word
	[Q]  ! quality
	[P]  ! potential
	[R]  ! reflexive
	```


