# -*- encoding: utf-8 -*-
# Copyright (c) 2015, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals
from unittest import TestCase
from num2words import num2words

class Num2WordsITTest(TestCase):

    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="it")
        neg_crd = num2words(-number, lang="it")
        pos_ord = num2words(+number, lang="it", ordinal=True)
        neg_ord = num2words(-number, lang="it", ordinal=True)
        self.assertEqual("meno " + pos_crd, neg_crd)
        self.assertEqual("meno " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertTrue("tre virgola uno quattro uno" in num2words(3.1415, lang="it"))
        self.assertTrue("meno cinque virgola uno" in num2words(-5.15, lang="it"))
        self.assertTrue("meno zero virgola uno" in num2words(-0.15, lang="it"))

    def test_float_to_ordinal(self):
        self.assertTrue("terzo virgola uno quattro uno" in num2words(3.1415, lang="it", ordinal=True))
        self.assertTrue("meno quinto virgola uno" in num2words(-5.15, lang="it", ordinal=True))
        self.assertTrue("meno zero virgola uno" in num2words(-0.15, lang="it", ordinal=True))

    def test_0(self):
        self.assertEqual(num2words(0, lang="it"), "zero")
        self.assertEqual(num2words(0, lang="it", ordinal=True), "zero")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="it"), "uno")
        self.assertEqual(num2words(2, lang="it"), "due")
        self.assertEqual(num2words(7, lang="it"), "sette")
        self.assertEqual(num2words(10, lang="it"), "dieci")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="it"), "undici")
        self.assertEqual(num2words(13, lang="it"), "tredici")
        self.assertEqual(num2words(15, lang="it"), "quindici")
        self.assertEqual(num2words(16, lang="it"), "sedici")
        self.assertEqual(num2words(19, lang="it"), "diciannove")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="it"), "venti")
        self.assertEqual(num2words(21, lang="it"), "ventuno")
        self.assertEqual(num2words(23, lang="it"), "ventitré")
        self.assertEqual(num2words(28, lang="it"), "ventotto")
        self.assertEqual(num2words(31, lang="it"), "trentuno")
        self.assertEqual(num2words(40, lang="it"), "quaranta")
        self.assertEqual(num2words(66, lang="it"), "sessantasei")
        self.assertEqual(num2words(92, lang="it"), "novantadue")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="it"), "cento")
        self.assertEqual(num2words(111, lang="it"), "centoundici")
        self.assertEqual(num2words(150, lang="it"), "centocinquanta")
        self.assertEqual(num2words(196, lang="it"), "centonovantasei")
        self.assertEqual(num2words(200, lang="it"), "duecento")
        self.assertEqual(num2words(210, lang="it"), "duecentodieci")
        self.assertEqual(num2words(701, lang="it"), "settecentouno")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="it"), "mille")
        self.assertEqual(num2words(1001, lang="it"), "milleuno")
        self.assertEqual(num2words(1500, lang="it"), "millecinquecento")
        self.assertEqual(num2words(7378, lang="it"), "settemilatrecentosettantotto")
        self.assertEqual(num2words(2000, lang="it"), "duemila")
        self.assertEqual(num2words(2100, lang="it"), "duemilacento")
        self.assertEqual(num2words(6870, lang="it"), "seimilaottocentosettanta")
        self.assertEqual(num2words(10000, lang="it"), "diecimila")
        self.assertEqual(num2words(98765, lang="it"), "novantottomilasettecentosessantacinque")
        self.assertEqual(num2words(100000, lang="it"), "centomila")
        self.assertEqual(num2words(523456, lang="it"), "cinquecentoventitremilaquattrocentocinquantasei")

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="it"), "un milione")
        self.assertEqual(num2words(1000007, lang="it"), "un milione e sette")
        self.assertEqual(num2words(1200000, lang="it"), "un milione e duecentomila")
        self.assertEqual(num2words(3000000, lang="it"), "tre milioni")
        self.assertEqual(num2words(3000005, lang="it"), "tre milioni e cinque")
        self.assertEqual(num2words(3800000, lang="it"), "tre milioni e ottocentomila")
        self.assertEqual(num2words(1000000000, lang="it"), "un miliardo")
        self.assertEqual(num2words(1000000017, lang="it"), "un miliardo e diciassette")
        self.assertEqual(num2words(2000000000, lang="it"), "due miliardi")
        self.assertEqual(num2words(2000001000, lang="it"), "due miliardi e mille")
        self.assertEqual(num2words(1234567890, lang="it"), "un miliardo, duecentotrentaquattro milioni e cinquecentosessantasettemilaottocentonovanta")
        self.assertEqual(num2words(1000000000000, lang="it"), "un bilione")
        self.assertEqual(num2words(123456789012345678901234567890, lang="it"), "centoventitré quadriliardi, quattrocentocinquantasei quadrilioni, settecentottantanove triliardi, dodici trilioni, trecentoquarantacinque biliardi, seicentosettantotto bilioni, novecentouno miliardi, duecentotrentaquattro milioni e cinquecentosessantasettemilaottocentonovanta")

    def test_20_to_99_split(self):
        self.assertEqual(num2words(20, lang="it", splitwords=True), "venti")
        self.assertEqual(num2words(21, lang="it", splitwords=True), "ventuno")
        self.assertEqual(num2words(23, lang="it", splitwords=True), "venti tre")
        self.assertEqual(num2words(28, lang="it", splitwords=True), "ventotto")
        self.assertEqual(num2words(31, lang="it", splitwords=True), "trentuno")
        self.assertEqual(num2words(40, lang="it", splitwords=True), "quaranta")
        self.assertEqual(num2words(66, lang="it", splitwords=True), "sessanta sei")
        self.assertEqual(num2words(92, lang="it", splitwords=True), "novanta due")

    def test_100_to_999_split(self):
        self.assertEqual(num2words(100, lang="it", splitwords=True), "cento")
        self.assertEqual(num2words(111, lang="it", splitwords=True), "cento undici")
        self.assertEqual(num2words(150, lang="it", splitwords=True), "cento cinquanta")
        self.assertEqual(num2words(196, lang="it", splitwords=True), "cento novanta sei")
        self.assertEqual(num2words(200, lang="it", splitwords=True), "due cento")
        self.assertEqual(num2words(210, lang="it", splitwords=True), "due cento dieci")
        self.assertEqual(num2words(701, lang="it", splitwords=True), "sette cento uno")

    def test_1000_to_9999_split(self):
        self.assertEqual(num2words(1000, lang="it", splitwords=True), "mille")
        self.assertEqual(num2words(1001, lang="it", splitwords=True), "mille uno")
        self.assertEqual(num2words(1500, lang="it", splitwords=True), "mille cinque cento")
        self.assertEqual(num2words(7378, lang="it", splitwords=True), "sette mila tre cento settantotto")
        self.assertEqual(num2words(2000, lang="it", splitwords=True), "due mila")
        self.assertEqual(num2words(2100, lang="it", splitwords=True), "due mila cento")
        self.assertEqual(num2words(6870, lang="it", splitwords=True), "sei mila otto cento settanta")
        self.assertEqual(num2words(10000, lang="it", splitwords=True), "dieci mila")
        self.assertEqual(num2words(98765, lang="it", splitwords=True), "novantotto mila sette cento sessanta cinque")
        self.assertEqual(num2words(100000, lang="it", splitwords=True), "cento mila")
        self.assertEqual(num2words(523456, lang="it", splitwords=True), "cinque cento venti tre mila quattro cento cinquanta sei")

    def test_big_split(self):
        self.assertEqual(num2words(1000000, lang="it", splitwords=True), "un milione")
        self.assertEqual(num2words(1000007, lang="it", splitwords=True), "un milione e sette")
        self.assertEqual(num2words(1200000, lang="it", splitwords=True), "un milione e due cento mila")
        self.assertEqual(num2words(3000000, lang="it", splitwords=True), "tre milioni")
        self.assertEqual(num2words(3000005, lang="it", splitwords=True), "tre milioni e cinque")
        self.assertEqual(num2words(3800000, lang="it", splitwords=True), "tre milioni e otto cento mila")
        self.assertEqual(num2words(1000000000, lang="it", splitwords=True), "un miliardo")
        self.assertEqual(num2words(1000000017, lang="it", splitwords=True), "un miliardo e diciassette")
        self.assertEqual(num2words(2000000000, lang="it", splitwords=True), "due miliardi")
        self.assertEqual(num2words(2000001000, lang="it", splitwords=True), "due miliardi e mille")
        self.assertEqual(num2words(1234567890, lang="it", splitwords=True), "un miliardo, due cento trenta quattro milioni e cinque cento sessanta sette mila otto cento novanta")
        self.assertEqual(num2words(1000000000000, lang="it", splitwords=True), "un bilione")
        self.assertEqual(num2words(123456789012345678901234567890, lang="it", splitwords=True), "cento venti tre quadriliardi, quattro cento cinquanta sei quadrilioni, sette cento ottanta nove triliardi, dodici trilioni, tre cento quaranta cinque biliardi, sei cento settantotto bilioni, nove cento uno miliardi, due cento trenta quattro milioni e cinque cento sessanta sette mila otto cento novanta")

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="it", ordinal=True), "primo")
        self.assertEqual(num2words(8, lang="it", ordinal=True), "ottavo")
        self.assertEqual(num2words(23, lang="it", ordinal=True), "ventitreesimo")
        self.assertEqual(num2words(47, lang="it", ordinal=True), "quarantasettesimo")
        self.assertEqual(num2words(99, lang="it", ordinal=True), "novantanovesimo")

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="it", ordinal=True), "centesimo")
        self.assertEqual(num2words(112, lang="it", ordinal=True), "centododicesimo")
        self.assertEqual(num2words(120, lang="it", ordinal=True), "centoventesimo")
        self.assertEqual(num2words(316, lang="it", ordinal=True), "trecentosedicesimo")
        self.assertEqual(num2words(700, lang="it", ordinal=True), "settecentesimo")
        self.assertEqual(num2words(803, lang="it", ordinal=True), "ottocentotreesimo")
        self.assertEqual(num2words(923, lang="it", ordinal=True), "novecentoventitreesimo")

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="it", ordinal=True), "millesimo")
        self.assertEqual(num2words(1001, lang="it", ordinal=True), "milleunesimo")
        self.assertEqual(num2words(1003, lang="it", ordinal=True), "milletreesimo")
        self.assertEqual(num2words(1200, lang="it", ordinal=True), "milleduecentesimo")
        self.assertEqual(num2words(8640, lang="it", ordinal=True), "ottomilaseicentoquarantesimo")
        self.assertEqual(num2words(14000, lang="it", ordinal=True), "quattordicimillesimo")
        self.assertEqual(num2words(123456, lang="it", ordinal=True), "centoventitremilaquattrocentocinquantaseiesimo")
        self.assertEqual(num2words(987654, lang="it", ordinal=True), "novecentottantasettemilaseicentocinquantaquattresimo")

    def test_nth_big(self):
        self.assertEqual(num2words(1000000001, lang="it", ordinal=True), "un miliardo e unesimo")
        self.assertEqual(num2words(123456789012345678901234567890, lang="it", ordinal=True), "centoventitré quadriliardi, quattrocentocinquantasei quadrilioni, settecentottantanove triliardi, dodici trilioni, trecentoquarantacinque biliardi, seicentosettantotto bilioni, novecentouno miliardi, duecentotrentaquattro milioni e cinquecentosessantasettemilaottocentonovantesimo")
