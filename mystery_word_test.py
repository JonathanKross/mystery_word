import unittest
from mystery_word import *

test_words = ["BIRD", "CALF", "RIVER", "STREAM", "KNEECAP",  "COOKBOOK",
             "LANGUAGE", "SNEAKER", "ALGORITHM", "INTEGRATION", "BRAIN"]


class TestMysteryWord(unittest.TestCase):

    # def test_create_list_all_words(self):
    #     self.assertEqual(create_list_all_words(test_words), ["BIRD", "CALF", "RIVER", "STREAM", "KNEECAP",  "COOKBOOK",
    #                  "LANGUAGE", "SNEAKER", "ALGORITHM", "INTEGRATION", "BRAIN"])


    def test_list_easy_words(self):
        self.assertEqual(list_easy_words(test_words), ["BIRD", "CALF", "RIVER", "STREAM", "BRAIN"])


    def test_list_normal_words(self):
        self.assertEqual(list_normal_words(test_words), ["STREAM", "KNEECAP", "COOKBOOK", "LANGUAGE", "SNEAKER"])


    def test_list_hard_words(self):
        self.assertEqual(list_hard_words(test_words), ["COOKBOOK", "LANGUAGE", "ALGORITHM", "INTEGRATION"])


    def test_generate_random_word(self):
        word = generate_random_word(test_words)
        self.assertTrue(word in test_words)


    def test_display_visual_guesses(self):
        word = "INTEGRATION"
        self.assertEqual(display_visual_guesses(word, []), "___________")
        self.assertEqual(display_visual_guesses(word, ["Z"]), "___________")
        self.assertEqual(display_visual_guesses(word, ["G"]), "____G______")
        self.assertEqual(display_visual_guesses(word, ["I"]), "I_______I__")
        self.assertEqual(display_visual_guesses(word, ["I", "G"]), "I___G___I__")
        self.assertEqual(display_visual_guesses(word, ["I", "N", "Z"]), "IN______I_N")


    def test_is_word_complete(self):
        word = "RIVER"
        self.assertFalse(is_word_complete(word, []))
        self.assertFalse(is_word_complete(word, ["R"]))
        self.assertFalse(is_word_complete(word, ["R", "E"]))
        self.assertFalse(is_word_complete(word, ["R", "E", "E"]))
        self.assertTrue(is_word_complete(word, ["R", "E", "V", "R"]))


if __name__ == '__main__':
    unittest.main()
