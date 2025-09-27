import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test1(self):
        evaluate_dominant_emotion=emotion_detector('I am glad this happened')
        result=evaluate_dominant_emotion.get("dominant_emotion")
        self.assertEqual(result,'joy')

    def test2(self):
        evaluate_dominant_emotion=emotion_detector('I am really mad about this')
        result=evaluate_dominant_emotion.get("dominant_emotion")
        self.assertEqual(result,'anger')

    def test3(self):
        evaluate_dominant_emotion=emotion_detector('I feel disgusted just hearing about this')
        result=evaluate_dominant_emotion.get("dominant_emotion")
        self.assertEqual(result,'disgust')

    def test4(self):
        evaluate_dominant_emotion=emotion_detector('I am so sad about this')
        result=evaluate_dominant_emotion.get("dominant_emotion")
        self.assertEqual(result,'sadness')

    def test5(self):
        evaluate_dominant_emotion=emotion_detector('I am really afraid that this will happen')
        result=evaluate_dominant_emotion.get("dominant_emotion")
        self.assertEqual(result,'fear')

if __name__ == '__main__':
    unittest.main()