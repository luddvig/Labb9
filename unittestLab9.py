import unittest

from Syntaxfel import *

class SyntaxTest(unittest.TestCase):
    def testSyntaktisktKorrekt(self):
        """Testar syntaktiskt korrekt molekyl"""
        # Sample input 1
        self.assertEqual(checkMoleculeSyntax("Na"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("H2O"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(checkMoleculeSyntax("Na332"), "Formeln är syntaktiskt korrekt")

    def testSyntaktisktInkorrekt(self):
        """Testar syntaktiskt inkorrekt molekyl"""
        # Sample input 2
        self.assertEqual(checkMoleculeSyntax("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
        self.assertEqual(checkMoleculeSyntax("C(OH4)C"), "Saknad siffra vid radslutet C")
        self.assertEqual(checkMoleculeSyntax("C(OH4C"), "Saknad högerparentes vid radslutet")
        self.assertEqual(checkMoleculeSyntax("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
        self.assertEqual(checkMoleculeSyntax("H0"), "För litet tal vid radslutet ")
        self.assertEqual(checkMoleculeSyntax("H1C"), "För litet tal vid radslutet C")
        self.assertEqual(checkMoleculeSyntax("H02C"), "För litet tal vid radslutet 2C")
        self.assertEqual(checkMoleculeSyntax("Nacl"), "Saknad stor bokstav vid radslutet cl")
        self.assertEqual(checkMoleculeSyntax("a"), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(checkMoleculeSyntax("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
        self.assertEqual(checkMoleculeSyntax(")"), "Felaktig gruppstart vid radslutet )")
        self.assertEqual(checkMoleculeSyntax("2"), "Felaktig gruppstart vid radslutet 2")

if __name__ == "__main__":
    unittest.main()
