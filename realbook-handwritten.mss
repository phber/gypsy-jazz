<?xml version="1.0" encoding="UTF-8"?>
<museScore version="4.50">
  <Style>

    <!-- ===================================================================
         REAL BOOK / HANDWRITTEN LEAD SHEET
         MuseScore 4.4+  (Format > Load Style...)

         Music glyphs : MuseJazz        (hand-lettered jazz copyist font)
         All text     : MuseJazz Text
         Chord symbols: Jazz style, superscripted extensions

         To get a softer pencil-on-manuscript look instead, swap the two
         font blocks marked [FONT: GLYPHS] and [FONT: TEXT] for Petaluma and
         Petaluma Script. Exact alternates are listed at the bottom of this
         file.
         =================================================================== -->

    <!-- ========== PAGE: US Letter, generous margins like a fake book ========== -->
    <pageWidth>8.5</pageWidth>
    <pageHeight>11</pageHeight>
    <pagePrintableWidth>7.5</pagePrintableWidth>
    <pageEvenLeftMargin>0.5</pageEvenLeftMargin>
    <pageOddLeftMargin>0.5</pageOddLeftMargin>
    <pageEvenTopMargin>0.5</pageEvenTopMargin>
    <pageEvenBottomMargin>0.65</pageEvenBottomMargin>
    <pageOddTopMargin>0.5</pageOddTopMargin>
    <pageOddBottomMargin>0.65</pageOddBottomMargin>
    <pageTwosided>0</pageTwosided>

    <!-- Large staff: fake books are printed big enough to read on a stand -->
    <Spatium>1.95</Spatium>

    <!-- ========== SYSTEM / STAFF SPACING ==========
         Roomy, because chord symbols sit above every system. -->
    <staffUpperBorder>7.5</staffUpperBorder>
    <staffLowerBorder>6</staffLowerBorder>
    <staffDistance>6.5</staffDistance>
    <minSystemDistance>13</minSystemDistance>
    <maxSystemDistance>19</maxSystemDistance>
    <enableVerticalSpread>1</enableVerticalSpread>
    <minSystemSpread>4</minSystemSpread>
    <maxSystemSpread>12</maxSystemSpread>
    <frameSystemDistance>4</frameSystemDistance>
    <systemFrameDistance>7</systemFrameDistance>
    <lastSystemFillLimit>0.1</lastSystemFillLimit>

    <!-- ========== LEAD SHEET LAYOUT ==========
         No indent, no instrument name, no multimeasure rests: one staff,
         bars evenly spaced so 4 bars per system falls out naturally. -->
    <enableIndentationOnFirstSystem>0</enableIndentationOnFirstSystem>
    <firstSystemIndentationValue>0</firstSystemIndentationValue>
    <hideInstrumentNameIfOneInstrument>1</hideInstrumentNameIfOneInstrument>
    <createMultiMeasureRests>0</createMultiMeasureRests>
    <hideEmptyStaves>0</hideEmptyStaves>
    <concertPitch>1</concertPitch>
    <measureSpacing>1.5</measureSpacing>
    <minMeasureWidth>7</minMeasureWidth>
    <minNoteDistance>0.7</minNoteDistance>
    <barNoteDistance>1.1</barNoteDistance>
    <noteBarDistance>1.1</noteBarDistance>

    <!-- ========== INK WEIGHT ==========
         Everything a touch heavier than engraved default: hand-drawn lines
         are never hairlines. -->
    <staffLineWidth>0.13</staffLineWidth>
    <barWidth>0.19</barWidth>
    <doubleBarWidth>0.19</doubleBarWidth>
    <endBarWidth>0.55</endBarWidth>
    <doubleBarDistance>0.42</doubleBarDistance>
    <endBarDistance>0.42</endBarDistance>
    <repeatBarlineDotSeparation>0.45</repeatBarlineDotSeparation>
    <repeatBarTips>0</repeatBarTips>
    <startBarlineSingle>0</startBarlineSingle>
    <startBarlineMultiple>1</startBarlineMultiple>
    <stemWidth>0.14</stemWidth>
    <ledgerLineWidth>0.18</ledgerLineWidth>
    <ledgerLineLength>0.38</ledgerLineLength>
    <beamWidth>0.56</beamWidth>
    <beamDistance>0.42</beamDistance>
    <useWideBeams>1</useWideBeams>
    <useStraightNoteFlags>0</useStraightNoteFlags>

    <!-- Fatter, flatter slurs/ties read as drawn by hand -->
    <slurEndWidth>0.09</slurEndWidth>
    <slurMidWidth>0.20</slurMidWidth>
    <slurDottedWidth>0.12</slurDottedWidth>
    <slurMinDistance>0.5</slurMinDistance>
    <tieEndWidth>0.09</tieEndWidth>
    <tieMidWidth>0.20</tieMidWidth>
    <minTieLength>1.2</minTieLength>

    <!-- ========== [FONT: GLYPHS] ========== -->
    <musicalSymbolFont>MuseJazz</musicalSymbolFont>
    <musicalTextFont>MuseJazz Text</musicalTextFont>

    <!-- ========== CHORD SYMBOLS ==========
         Jazz spellings: superscript extensions, triangle for major 7,
         small raised alterations. This is the single most Real Book-ish
         setting in the file. -->
    <chordStyle>jazz</chordStyle>
    <chordDescriptionFile>chords_jazz.xml</chordDescriptionFile>
    <chordsXmlFile>0</chordsXmlFile>
    <chordExtensionMag>0.85</chordExtensionMag>
    <chordExtensionAdjust>-0.1</chordExtensionAdjust>
    <chordModifierMag>0.85</chordModifierMag>
    <chordModifierAdjust>0</chordModifierAdjust>
    <harmonyPlacement>above</harmonyPlacement>
    <harmonyFretDist>0.5</harmonyFretDist>
    <minHarmonyDistance>0.75</minHarmonyDistance>
    <maxHarmonyBarDistance>3</maxHarmonyBarDistance>
    <maxChordShiftAbove>0</maxChordShiftAbove>
    <maxChordShiftBelow>0</maxChordShiftBelow>
    <capoPosition>0</capoPosition>
    <automaticCapitalization>1</automaticCapitalization>
    <lowerCaseMinorChords>0</lowerCaseMinorChords>
    <lowerCaseBassNotes>0</lowerCaseBassNotes>
    <allCapsNoteNames>0</allCapsNoteNames>
    <useStandardNoteNames>1</useStandardNoteNames>
    <chordSymbolAFontFace>MuseJazz Text</chordSymbolAFontFace>
    <chordSymbolAFontSize>12</chordSymbolAFontSize>
    <chordSymbolAFontStyle>0</chordSymbolAFontStyle>
    <chordSymbolAAlign>left,baseline</chordSymbolAAlign>
    <chordSymbolAPosAbove x="0" y="-3.5"/>
    <chordSymbolBFontFace>MuseJazz Text</chordSymbolBFontFace>
    <chordSymbolBFontSize>12</chordSymbolBFontSize>
    <chordSymbolBFontStyle>2</chordSymbolBFontStyle>
    <romanNumeralFontFace>MuseJazz Text</romanNumeralFontFace>
    <nashvilleNumberFontFace>MuseJazz Text</nashvilleNumberFontFace>

    <!-- Swing playback so a straight-written sheet sounds like la pompe -->
    <swingUnit>eighth</swingUnit>
    <swingRatio>62</swingRatio>

    <!-- ========== REHEARSAL MARKS: boxed capitals, [A] [B] [C] ========== -->
    <rehearsalMarkFontFace>MuseJazz Text</rehearsalMarkFontFace>
    <rehearsalMarkFontSize>13</rehearsalMarkFontSize>
    <rehearsalMarkFontStyle>1</rehearsalMarkFontStyle>
    <rehearsalMarkAlign>center,baseline</rehearsalMarkAlign>
    <rehearsalMarkFrameType>1</rehearsalMarkFrameType>
    <rehearsalMarkFramePadding>0.4</rehearsalMarkFramePadding>
    <rehearsalMarkFrameWidth>0.16</rehearsalMarkFrameWidth>
    <rehearsalMarkFrameRound>0</rehearsalMarkFrameRound>
    <rehearsalMarkPlacement>above</rehearsalMarkPlacement>
    <rehearsalMarkPosAbove x="0" y="-4"/>
    <rehearsalMarkMinDistance>0.5</rehearsalMarkMinDistance>

    <!-- ========== MEASURE NUMBERS: once per system, not on bar 1 ========== -->
    <showMeasureNumber>1</showMeasureNumber>
    <showMeasureNumberOne>0</showMeasureNumberOne>
    <measureNumberInterval>1</measureNumberInterval>
    <measureNumberSystem>1</measureNumberSystem>
    <measureNumberAllStaves>0</measureNumberAllStaves>
    <measureNumberFontFace>MuseJazz Text</measureNumberFontFace>
    <measureNumberFontSize>8</measureNumberFontSize>
    <measureNumberFontStyle>0</measureNumberFontStyle>

    <!-- ========== [FONT: TEXT] Every text style on the jazz font ==========
         Listed exhaustively so nothing silently falls back to Edwin. -->
    <titleFontFace>MuseJazz Text</titleFontFace>
    <titleFontSize>26</titleFontSize>
    <titleFontStyle>0</titleFontStyle>
    <titleAlign>center,top</titleAlign>
    <subTitleFontFace>MuseJazz Text</subTitleFontFace>
    <subTitleFontSize>13</subTitleFontSize>
    <subTitleFontStyle>0</subTitleFontStyle>
    <subTitleAlign>center,top</subTitleAlign>
    <composerFontFace>MuseJazz Text</composerFontFace>
    <composerFontSize>11</composerFontSize>
    <composerFontStyle>0</composerFontStyle>
    <composerAlign>right,bottom</composerAlign>
    <lyricistFontFace>MuseJazz Text</lyricistFontFace>
    <lyricistFontSize>11</lyricistFontSize>
    <lyricistAlign>left,bottom</lyricistAlign>

    <lyricsOddFontFace>MuseJazz Text</lyricsOddFontFace>
    <lyricsOddFontSize>11</lyricsOddFontSize>
    <lyricsEvenFontFace>MuseJazz Text</lyricsEvenFontFace>
    <lyricsEvenFontSize>11</lyricsEvenFontSize>

    <tempoFontFace>MuseJazz Text</tempoFontFace>
    <tempoFontSize>12</tempoFontSize>
    <tempoFontStyle>1</tempoFontStyle>
    <tempoPlacement>above</tempoPlacement>
    <tempoPosAbove x="0" y="-4.5"/>
    <tempoChangeFontFace>MuseJazz Text</tempoChangeFontFace>
    <metronomeFontFace>MuseJazz Text</metronomeFontFace>
    <metronomeFontSize>12</metronomeFontSize>
    <metronomeFontStyle>0</metronomeFontStyle>

    <staffTextFontFace>MuseJazz Text</staffTextFontFace>
    <staffTextFontSize>11</staffTextFontSize>
    <systemTextFontFace>MuseJazz Text</systemTextFontFace>
    <systemTextFontSize>11</systemTextFontSize>
    <expressionFontFace>MuseJazz Text</expressionFontFace>
    <expressionFontSize>11</expressionFontSize>
    <expressionFontStyle>2</expressionFontStyle>

    <dynamicsFontFace>MuseJazz</dynamicsFontFace>
    <dynamicsFontSize>12</dynamicsFontSize>
    <hairpinFontFace>MuseJazz Text</hairpinFontFace>
    <hairpinFontSize>11</hairpinFontSize>
    <hairpinFontStyle>2</hairpinFontStyle>

    <longInstrumentFontFace>MuseJazz Text</longInstrumentFontFace>
    <shortInstrumentFontFace>MuseJazz Text</shortInstrumentFontFace>
    <partInstrumentFontFace>MuseJazz Text</partInstrumentFontFace>
    <partInstrumentFontSize>16</partInstrumentFontSize>
    <instrumentChangeFontFace>MuseJazz Text</instrumentChangeFontFace>

    <fingeringFontFace>MuseJazz Text</fingeringFontFace>
    <fingeringFontSize>9</fingeringFontSize>
    <lhGuitarFingeringFontFace>MuseJazz Text</lhGuitarFingeringFontFace>
    <rhGuitarFingeringFontFace>MuseJazz Text</rhGuitarFingeringFontFace>
    <stringNumberFontFace>MuseJazz Text</stringNumberFontFace>

    <tupletFontFace>MuseJazz Text</tupletFontFace>
    <tupletFontSize>10</tupletFontSize>
    <tupletFontStyle>2</tupletFontStyle>
    <tupletNumberType>0</tupletNumberType>
    <tupletBracketType>0</tupletBracketType>
    <tupletBracketWidth>0.14</tupletBracketWidth>
    <tupletMaxSlope>0.5</tupletMaxSlope>
    <tupletOufOfStaff>1</tupletOufOfStaff>

    <voltaFontFace>MuseJazz Text</voltaFontFace>
    <voltaFontSize>11</voltaFontSize>
    <voltaFontStyle>1</voltaFontStyle>
    <voltaLineWidth>0.16</voltaLineWidth>
    <voltaHook>1.9</voltaHook>
    <repeatLeftFontFace>MuseJazz Text</repeatLeftFontFace>
    <repeatLeftFontSize>18</repeatLeftFontSize>
    <repeatRightFontFace>MuseJazz Text</repeatRightFontFace>
    <repeatRightFontSize>18</repeatRightFontSize>

    <ottavaFontFace>MuseJazz Text</ottavaFontFace>
    <ottavaFontStyle>2</ottavaFontStyle>
    <pedalFontFace>MuseJazz Text</pedalFontFace>
    <glissandoFontFace>MuseJazz Text</glissandoFontFace>
    <glissandoFontStyle>2</glissandoFontStyle>
    <bendFontFace>MuseJazz Text</bendFontFace>
    <textLineFontFace>MuseJazz Text</textLineFontFace>
    <systemTextLineFontFace>MuseJazz Text</systemTextLineFontFace>
    <frameFontFace>MuseJazz Text</frameFontFace>
    <frameFontSize>12</frameFontSize>
    <stickingFontFace>MuseJazz Text</stickingFontFace>
    <harpPedalDiagramFontFace>MuseJazz Text</harpPedalDiagramFontFace>
    <harpPedalTextDiagramFontFace>MuseJazz Text</harpPedalTextDiagramFontFace>
    <mmRestRangeFontFace>MuseJazz Text</mmRestRangeFontFace>

    <headerFontFace>MuseJazz Text</headerFontFace>
    <headerFontSize>9</headerFontSize>
    <footerFontFace>MuseJazz Text</footerFontFace>
    <footerFontSize>8</footerFontSize>
    <copyrightFontFace>MuseJazz Text</copyrightFontFace>
    <copyrightFontSize>8</copyrightFontSize>
    <pageNumberFontFace>MuseJazz Text</pageNumberFontFace>
    <pageNumberFontSize>10</pageNumberFontSize>
    <translatorFontFace>MuseJazz Text</translatorFontFace>

    <user1FontFace>MuseJazz Text</user1FontFace>
    <user2FontFace>MuseJazz Text</user2FontFace>
    <user3FontFace>MuseJazz Text</user3FontFace>
    <user4FontFace>MuseJazz Text</user4FontFace>
    <user5FontFace>MuseJazz Text</user5FontFace>
    <user6FontFace>MuseJazz Text</user6FontFace>
    <user7FontFace>MuseJazz Text</user7FontFace>
    <user8FontFace>MuseJazz Text</user8FontFace>
    <user9FontFace>MuseJazz Text</user9FontFace>
    <user10FontFace>MuseJazz Text</user10FontFace>
    <user11FontFace>MuseJazz Text</user11FontFace>
    <user12FontFace>MuseJazz Text</user12FontFace>

    <!-- ========== HEADER / FOOTER: clean page, page number only ========== -->
    <showHeader>0</showHeader>
    <showFooter>1</showFooter>
    <footerFirstPage>1</footerFirstPage>
    <footerOddEven>0</footerOddEven>
    <evenFooterL></evenFooterL>
    <evenFooterC>$C</evenFooterC>
    <evenFooterR></evenFooterR>
    <oddFooterL></oddFooterL>
    <oddFooterC>$C</oddFooterC>
    <oddFooterR></oddFooterR>
    <showPageNumber>1</showPageNumber>
    <showPageNumberOne>0</showPageNumberOne>
    <pageNumberOddEven>0</pageNumberOddEven>

    <!-- ========== CLEFS / KEYS / ARTICULATIONS ========== -->
    <genClef>1</genClef>
    <genKeysig>1</genKeysig>
    <genCourtesyTimesig>1</genCourtesyTimesig>
    <genCourtesyKeysig>1</genCourtesyKeysig>
    <genCourtesyClef>1</genCourtesyClef>
    <keySigNaturals>0</keySigNaturals>
    <clefLeftMargin>0.85</clefLeftMargin>
    <keysigLeftMargin>0.6</keysigLeftMargin>
    <timesigLeftMargin>0.6</timesigLeftMargin>
    <articulationMag>1.1</articulationMag>
    <articulationMinDistance>0.5</articulationMinDistance>
    <graceNoteMag>0.7</graceNoteMag>
    <smallNoteMag>0.7</smallNoteMag>
    <dotNoteDistance>0.4</dotNoteDistance>
    <accidentalNoteDistance>0.3</accidentalNoteDistance>
    <accidentalDistance>0.28</accidentalDistance>
    <minVerticalDistance>0.6</minVerticalDistance>
    <autoplaceEnabled>1</autoplaceEnabled>

    <!-- ===================================================================
         ALTERNATE: pencil-on-manuscript (softer, more irregular) instead of
         the jazz copyist look. Replace the two font blocks above with:

           <musicalSymbolFont>Petaluma</musicalSymbolFont>
           <musicalTextFont>Petaluma Text</musicalTextFont>

         and every "MuseJazz Text" with "Petaluma Script"
         (keep <dynamicsFontFace> on "Petaluma").
         Petaluma Script runs small, so add about 1pt to each font size.
         =================================================================== -->

  </Style>
</museScore>
