#!/usr/local/bin/fontforge

import fontforge
import psMat

outfont=fontforge.font()
outfont.encoding="unicode"
outfont.em=2048

outfont.fontname='TengwarFormalUnicode-Regular'
outfont.familyname='Tengwar Formal Unicode'
outfont.fullname='Tengwar Formal Unicode'
outfont.copyright='Copyright (c) September 2009, Michal Nowakowski (http://tengwarformal.limes.com.pl),\n\
with Reserved Font Names "Tengwar Formal" and "Tengwar Formal A".\n\
\n\
Tengwar Formal Unicode copyright (c) 2010, Johan Winge and J. "Mach" Wust (http://freetengwar.sourceforge.net/)\n\
\n\
This Font Software is licensed under the SIL Open Font License, Version 1.1.\n\
This license is provided in a separate file, LICENSE, supplied with the fonts,\n\
and is also available with a FAQ at: http://scripts.sil.org/OFL'
outfont.version='1.0'
outfont.sfnt_names=(('English (US)', 'UniqueID', 'FontTengwarFormalUnicode10'),
                    ('English (US)', 'Designer', 'Micha\xc5\x82 Nowakowski'),
                    ('English (US)', 'Designer URL', 'http://tengwarformal.limes.com.pl'),
                    ('English (US)', 'License URL', 'http://scripts.sil.org/OFL')
                   )

dansmithenc ={fontforge.open("TengwarFormal12c.sfd"): {
               'one': 'tinco',
               'q': 'parma',
               'a': 'calma',
               'z': 'quesse',
               'two': 'ando',
               'w': 'umbar',
               's': 'anga',
               'x': 'ungwe',
               'three': 'suule',
               'e': 'formen',
               'd': 'aha',
               'c': 'hwesta',
               'four': 'anto',
               'r': 'ampa',
               'f': 'anca',
               'v': 'unque',
               'five': 'nuumen',
               't': 'malta',
               'g': 'noldo',
               'b': 'nwalme',
               'six': 'oore',
               'y': 'vala',
               'h': 'anna',
               'n': 'vilya',
               'exclam': 'tincoX',
               'Q': 'parmaX',
               'A': 'calmaX',
               'Z': 'quesseX',
               'at': 'andoX',
               'W': 'umbarX',
               'S': 'angaX',
               'X': 'ungweX',
               'seven': 'roomen',
               'u': 'arda',
               'j': 'lambe',
               'm': 'alda',
               'eight': 'silme',
               'i': 'silmeN',
               'k': 'esse',
               'comma': 'esseN',
               'asterisk': 'silme.alt',
               'I': 'silmeN.alt',
               'K': 'esse.alt',
               'less': 'esseN.alt', # Or hwestaC
               'nine': 'hyarmen',
               'o': 'hwestaS',
               'l': 'yanta',
               'period': 'uure',
               'asciitilde': 'longCarrier',
               'onehalf': 'halla',
               'grave': 'shortCarrier',
               'threequarters': 'lambeN',
               'threesuperior': 'lambeN.alt',
               'bracketright': 'osse',
               'daggerdbl': 'osse.alt',
               'onequarter': 'carrierX',
               'Adieresis': 'quesseC',
               'questiondown': 'roomenN',
               'scaron': 'maltaX',
               'bullet': 'hallaRoomen',
               'numbersign': 'tehtaA.shift4',
               'E': 'tehtaA.shift3',
               'D': 'tehtaA.shift2',
               'C': 'tehtaA.shift1',
               'Udieresis': 'tehtaA.altshift4',
               'Yacute': 'tehtaA.altshift3',
               'Thorn': 'tehtaA.altshift2',
               'germandbls': 'tehtaA.altshift1',
               'Eth': 'tehtaAB.shift4',
               'Ntilde': 'tehtaAB.shift3',
               'Ograve': 'tehtaAB.shift2',
               'Oacute': 'tehtaAB.shift1',
               #'greater': 'tehtaAB.shift1alt', # Might be duplicate
               'Ocircumflex': 'tehtaY.shift4',
               'Otilde': 'tehtaY.shift3',
               'Odieresis': 'tehtaY.shift2',
               'multiply': 'tehtaY.shift1',
               'Igrave': 'tehtaYB.shift4',
               'Iacute': 'tehtaYB.shift3',
               'Icircumflex': 'tehtaYB.shift2',
               'Idieresis': 'tehtaYB.shift1',
               'acute': 'tehtaYB.lambe',
               'percent': 'tehtaI.shift4',
               'T': 'tehtaI.shift3',
               'G': 'tehtaI.shift2',
               'B': 'tehtaI.shift1',
               'parenleft': 'tehtaIB.shift4',
               #'Egrave': 'tehtaIB.shift4alt', # Might be duplicate
               'Eacute': 'tehtaIB.shift35',   # Might be duplicate
               'O': 'tehtaIB.shift3',
               'Ecircumflex': 'tehtaIB.shift2',
               'Edieresis': 'tehtaIB.shift1',
               'L': 'tehtaIB.lambe',
               'dollar': 'tehtaE.shift4',
               'R': 'tehtaE.shift3',
               'F': 'tehtaE.shift2',
               'V': 'tehtaE.shift1',
               'perthousand': 'tehtaEB.shift4',
               'Scaron': 'tehtaEB.shift3',
               'guilsinglleft': 'tehtaEB.shift2',
               'Ydieresis': 'tehtaEB.shift1',
               'florin': 'tehtaEEB.shift4',
               'quotedblbase': 'tehtaEEB.shift3',
               'ellipsis': 'tehtaEEB.shift2',
               'dagger': 'tehtaEEB.shift1',
               'quotesinglbase': 'tehtaEEB.lambe',
               'asciicircum': 'tehtaO.shift4',
               'Y': 'tehtaO.shift3',
               'H': 'tehtaO.shift2',
               'N': 'tehtaO.shift1',
               'adieresis': 'tehtaOB.shift4',
               'aring': 'tehtaOB.shift3',
               'ae': 'tehtaOB.shift2',
               'ccedilla': 'tehtaOB.shift1',
               'ampersand': 'tehtaU.shift4',
               'U': 'tehtaU.shift3',
               'J': 'tehtaU.shift2',
               'M': 'tehtaU.shift1',
               'agrave': 'tehtaU.altshift4',
               'aacute': 'tehtaU.altshift3',
               'acircumflex': 'tehtaU.altshift2',
               'atilde': 'tehtaU.altshift1',
               'quoteleft': 'tehtaUB.shift4',
               'quoteright': 'tehtaUB.shift3',
               'quotedblleft': 'tehtaUB.shift2',
               'quotedblright': 'tehtaUB.shift1',
               'bracketleft': 'tehtaN.narrow',
               'braceleft': 'tehtaN.wide',
               'icircumflex': 'tehtaN.highnarrow',
               'igrave': 'tehtaN.highwide',
               'p': 'tehtaN.altnarrow',
               'P': 'tehtaN.altwide',
               'zero': 'tehtaN.althighnarrow',
               'parenright': 'tehtaN.althighwide',
               'quotesingle': 'tehtaB.narrow',
               'quotedbl': 'tehtaB.wide',
               'cedilla': 'tehtaB.lambe',
               'idieresis': 'tehtaB.lownarrow',
               'iacute': 'tehtaB.lowwide',
               'semicolon': 'tehtaB.altnarrow',
               'colon': 'tehtaB.altwide',
               'slash': 'tehtaB.altlownarrow',
               'degree': 'tehtaB.altlambe',
               'question': 'tehtaB.altlowwide',
               'egrave': 'tehtaW.shift4',
               'eacute': 'tehtaW.shift3',
               'ecircumflex': 'tehtaW.shift2',
               'edieresis': 'tehtaW.shift1',
               'ordfeminine': 'tehtaAE.shift4',
               'minus': 'tehtaAE.shift3',
               #'Euro': 'tehtaAE.shift3alt', # Might be duplicate
               'macron': 'tehtaAE.shift2',
               'mu1': 'tehtaAE.shift1',
               'Oslash': 'tehtaBreve.altshift4', # It ought to be an alternative AE,
               'Ugrave': 'tehtaBreve.altshift3', # but people use them as the breve. Bah.
               'Uacute': 'tehtaBreve.altshift2',
               'Ucircumflex': 'tehtaBreve.altshift1',
               'udieresis': 'tehtaThinnas.shift4',
               'yacute': 'tehtaThinnas.shift3',
               'thorn': 'tehtaThinnas.shift2',
               'ydieresis': 'tehtaThinnas.shift1',
               'plus': 'tehtaS',
               'underscore': 'tehtaS.down',
               'sterling': 'tehtaS.swash',
               'yen': 'tehtaS.swashlambe',
               'Aring': 'tehtaS.upward',
               'cent': 'tehtaS.raised',
               'AE': 'tehtaS.raisedupward',
               'exclamdown': 'tehtaS.lifted',
               'bar': 'tehtaX.shift4',
               'braceright': 'tehtaX.shift3',
               'equal': 'tengwarPusta',
               'hyphen': 'tengwarDoublepusta',
               'circumflex': 'tengwarTriplepusta',
               'Aacute': 'tengwarExclamation',
               'Agrave': 'tengwarQuestion',
               'guilsinglright': 'tengwarParenthesis',
               'backslash': 'tengwarSection',
               'Acircumflex': 'tengwarSection.wide',
               'logicalnot': 'tengwarDoublesection',
               'guillemotleft': 'tengwarQuoteleft',
               'guillemotright': 'tengwarQuoteright',
               'eth': 'tengwardigit0',
               'ntilde': 'tengwardigit1',
               'ograve': 'tengwardigit2',
               'oacute': 'tengwardigit3',
               'ocircumflex': 'tengwardigit4',
               'otilde': 'tengwardigit5',
               'odieresis': 'tengwardigit6',
               'divide': 'tengwardigit7',
               'oslash': 'tengwardigit8',
               'ugrave': 'tengwardigit9',
               'uacute': 'tengwarduodecimal10',
               'ucircumflex': 'tengwarduodecimal11',
               'tilde': 'tengwardigitMark.shift4',
               'trademark': 'tengwardigitMark.shift3',
               'dieresis': 'tengwardigitMark.shift2',
               'copyright': 'tengwardigitMark.shift1',
               'section': 'aha_tinco',
               'brokenbar': 'hwesta_tinco',
               'endash': 'silme_aha',
               'emdash': 'uni204A',
               'plusminus': 'quoteleft',
               'twosuperior': 'quoteright',
               'registered': 'question',
               'Ccedilla': 'exclam',
               'ordmasculine': 'period',
               'Atilde': 'semicolon',
               'onesuperior': 'comma',
               'OE': 'parenleft',
               'oe': 'parenright',
               'space': 'space',
               'paragraph': 'paragraph',
               'middot': 'middot',
               'currency': 'currency',
              },

              fontforge.open("TengwarFormalA12c.sfd"): {
               'seven': 'roomen.alt',
               'u': 'arda.alt',
               'less': 'hwestaC',
               'y': 'valaX',
               'questiondown': 'roomenN.alt',
               'percent': 'tehtaYanta.shift4',
               'T': 'tehtaYanta.shift3',
               'G': 'tehtaYanta.shift2',
               'B': 'tehtaYanta.shift1',
               'numbersign': 'tehtaUure.shift4', # Not encoded in the unicode font
               'E': 'tehtaUure.shift3',
               'D': 'tehtaUure.shift2',
               'C': 'tehtaUure.shift1',
               'asciicircum': 'tehtaBreve.shift4',
               'Y': 'tehtaBreve.shift3',
               'H': 'tehtaBreve.shift2',
               'N': 'tehtaBreve.shift1',
               'dollar': 'tehtaW.narrowshift4',
               'R': 'tehtaW.narrowshift3',
               'F': 'tehtaW.narrowshift2',
               'V': 'tehtaW.narrowshift1',
               'braceright': 'tehtaS.swashhyarmen',
              }}

references =  {'tehtaA.shift2': 'tehtaA',
               'tehtaAB.shift2': 'tehtaAB',
               'tehtaY.shift2': 'tehtaY',
               'tehtaYB.shift2': 'tehtaYB',
               'tehtaI.shift2': 'tehtaI',
               'tehtaIB.shift2': 'tehtaIB',
               'tehtaE.shift2': 'tehtaE',
               'tehtaEB.shift2': 'tehtaEB',
               'tehtaEEB.shift2': 'tehtaEEB',
               'tehtaO.shift2': 'tehtaO',
               'tehtaOB.shift2': 'tehtaOB',
               'tehtaU.shift2': 'tehtaU',
               'tehtaUB.shift2': 'tehtaUB',
               'tehtaN.narrow': 'tehtaN',
               'tehtaB.narrow': 'tehtaB',
               'tehtaW.shift2': 'tehtaW',
               'tehtaBreve.shift2': 'tehtaBreve',
               'tehtaYanta.shift2': 'tehtaYanta',
               'tehtaAE.shift2': 'tehtaAE',
               'tehtaThinnas.shift2': 'tehtaThinnas',
               'tehtaX.shift3': 'tehtaX',
               'tengwarPusta': 'uni2E31',
               'tengwarDoublepusta': 'colon',
               'tengwarTriplepusta': 'uni205D',
               'tengwarQuadruplepusta': 'uni2058',
               'tengwarQuintuplepusta': 'uni2E2D',
               'tengwardigit0': 'osseN',
              }

freetengenc = {'tinco': 0xE000,
               'parma': 0xE001,
               'calma': 0xE002,
               'quesse': 0xE003,
               'ando': 0xE004,
               'umbar': 0xE005,
               'anga': 0xE006,
               'ungwe': 0xE007,
               'suule': 0xE008,
               'formen': 0xE009,
               'aha': 0xE00A,
               'hwesta': 0xE00B,
               'anto': 0xE00C,
               'ampa': 0xE00D,
               'anca': 0xE00E,
               'unque': 0xE00F,
               'nuumen': 0xE010,
               'malta': 0xE011,
               'noldo': 0xE012,
               'nwalme': 0xE013,
               'oore': 0xE014,
               'vala': 0xE015,
               'anna': 0xE016,
               'vilya': 0xE017,
               'tincoX': 0xE018,
               'parmaX': 0xE019,
               'calmaX': 0xE01A,
               'quesseX': 0xE01B,
               'andoX': 0xE01C,
               'umbarX': 0xE01D,
               'angaX': 0xE01E,
               'ungweX': 0xE01F,
               'roomen': 0xE020,
               'arda': 0xE021,
               'lambe': 0xE022,
               'alda': 0xE023,
               'silme': 0xE024,
               'silmeN': 0xE025,
               'esse': 0xE026,
               'esseN': 0xE027,
               'hyarmen': 0xE028,
               'hwestaS': 0xE029,
               'yanta': 0xE02A,
               'uure': 0xE02B,
               'longCarrier': 0xE02C,
               'halla': 0xE02D,
               'shortCarrier': 0xE02E,
               'osseN': 0xE030,
               'lambeN': 0xE031,
               'osse': 0xE032,
               'carrierX': 0xE034,
               'annaS': 0xE035,
               'annaX': 0xE036,
               'quesseC': 0xE037,
               'hwestaC': 0xE038,
               'roomenN': 0xE039,
               'maltaX': 0xE03A,
               'valaX': 0xE03B,
               'hallaRoomen': 0xE03C,
               'vaiya': 0xE03D,
               'tehtaA': 0xE040,
               'tehtaAB': 0xE041,
               'tehtaY': 0xE042,
               'tehtaYB': 0xE043,
               'tehtaI': 0xE044,
               'tehtaIB': 0xE045,
               'tehtaE': 0xE046,
               'tehtaEB': 0xE047,
               'tehtaEE': 0xE048,
               'tehtaEEB': 0xE049,
               'tehtaO': 0xE04A,
               'tehtaOB': 0xE04B,
               'tehtaU': 0xE04C,
               'tehtaUB': 0xE04D,
               'tehtaOO': 0xE04E,
               'tehtaUU': 0xE04F,
               'tehtaN': 0xE050,
               'tehtaB': 0xE051,
               'tehtaW': 0xE052,
               'tehtaBreve': 0xE053,
               'tehtaGrave': 0xE054,
               'tehtaYanta': 0xE055,
               'tehtaAE': 0xE056,
               'tehtaThinnas': 0xE057,
               'tehtaS': 0xE058,
               'tehtaX': 0xE059,
               'tehtaDotInside': 0xE05A,
               'tengwarPusta': 0xE060,
               'tengwarDoublepusta': 0xE061,
               'tengwarTriplepusta': 0xE062,
               'tengwarQuadruplepusta': 0xE063,
               'tengwarQuintuplepusta': 0xE064,
               'tengwarExclamation': 0xE065,
               'tengwarQuestion': 0xE066,
               'tengwarParenthesis': 0xE067,
               'tengwarSection': 0xE068,
               'tengwarDoublesection': 0xE069,
               'tengwarQuoteleft': 0xE06A,
               'tengwarQuoteright': 0xE06B,
               'tengwarEclamationB': 0xE06C,
               'tengwardigit0': 0xE070,
               'tengwardigit1': 0xE071,
               'tengwardigit2': 0xE072,
               'tengwardigit3': 0xE073,
               'tengwardigit4': 0xE074,
               'tengwardigit5': 0xE075,
               'tengwardigit6': 0xE076,
               'tengwardigit7': 0xE077,
               'tengwardigit8': 0xE078,
               'tengwardigit9': 0xE079,
               'tengwarduodecimal10': 0xE07A,
               'tengwarduodecimal11': 0xE07B,
               'tengwarduodeciaml12': 0xE07C,
               'tengwardigitMark': 0xE07D,
              }

def ucname(alias):
   if '.' in alias:
     (base,var)=alias.split('.',1)
     var='.'+var
   else:
     (base,var)=(alias,'')
   name=''
   for comp in base.split('_'):
     if len(name)>0:
       name=name+'_'
     if comp in freetengenc:
       name=name+ 'uni' + hex(freetengenc[comp])[2:].upper() + var
     else:
       name=name+ comp+var
   return name

gdh=open('TengwarFormalUC.gdh','w')
gdh.write('table(glyph)\n')


for thefont, encoding in dansmithenc.iteritems():
   for char, alias in sorted(encoding.iteritems(), lambda x, y: cmp(ucname(x[1]),ucname(y[1]))):
      ucchar=alias
      thefont.selection.select(char)
      thefont[char].unlinkRef()
      thefont.copy()
      thefont.clear()
      outfont.createChar(-1,ucchar)
      outfont.selection.select(ucchar)
      outfont.paste()
      if alias in freetengenc:
        outfont[ucchar].unicode=freetengenc[alias]
      gdh.write('  ' + alias.replace('.', '_') + ' = ps("' + ucchar + '");\n')

outfont.createChar(0x200B,"zwsp").width=0
outfont.createChar(0x200C,"zwnj").width=0
outfont.createChar(0x200D,"zwj").width=0
gdh.write('  ZWJ = ps("zwj");\n')

ucchar='tengwarQuadruplepusta'
outfont.createChar(-1,ucchar).width=0;
outfont.selection.select('tengwarPusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.paste()
outfont.transform(psMat.translate(130*outfont.em/1000,0))
outfont.selection.select('tengwarDoublepusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.pasteInto()
outfont.transform(psMat.translate(130*outfont.em/1000,0))
outfont.selection.select('tengwarPusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.pasteInto()
outfont[ucchar].unicode=freetengenc[ucchar]

ucchar='uni10FB'
outfont.createChar(-1,ucchar).width=0;
outfont.selection.select('tengwarPusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.paste()
outfont.transform(psMat.translate(150*outfont.em/1000,0))
outfont.selection.select('tengwarDoublepusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.pasteInto()

ucchar='uni2E2C'
outfont.createChar(-1,ucchar).width=0;
outfont.selection.select('tengwarDoublepusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.paste()
outfont.transform(psMat.translate(206*outfont.em/1000,0))
outfont.selection.select('tengwarDoublepusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.pasteInto()

ucchar='tengwarQuintuplepusta'
outfont.createChar(-1,ucchar).width=0;
outfont.selection.select('tengwarPusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.paste()
outfont.transform(psMat.translate(160*outfont.em/1000,0))
outfont.selection.select('tengwarTriplepusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.pasteInto()
outfont.transform(psMat.translate(90*outfont.em/1000,0))
outfont.selection.select('tengwarPusta')
outfont.copyReference()
outfont.selection.select(ucchar)
outfont.pasteInto()
outfont[ucchar].unicode=freetengenc[ucchar]

for ref, target in references.iteritems():
   outfont.createChar(-1,target)
   outfont.selection.select(ref)
   outfont.copyReference()
   outfont.selection.select(target)
   outfont.paste()
   if target in freetengenc:
     outfont[target].unicode=freetengenc[target]
   gdh.write('  ' + target.replace('.', '_') + ' = ps("'+ target + '");\n')

gdh.write('endtable;\n\n')
gdh.close()

outfont.selection.all()
outfont.save("TengwarFormalUC.sfd")
outfont=fontforge.open("TengwarFormalUC.sfd")
outfont.generate("TengwarFormalUC_dumb.ttf")

