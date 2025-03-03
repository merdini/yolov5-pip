import unittest

from tests.test_utils import TestConstants


class TestYolov5(unittest.TestCase):
    def test_load_model(self):
        from PIL import Image
        from yolov5 import YOLOv5

        # init model
        model_path = TestConstants.YOLOV5S_MODEL_PATH
        device = "cpu"
        yolov5 = YOLOv5(model_path, device, load_on_init=False)
        yolov5.load_model()

        # check if loaded
        self.assertNotEqual(yolov5.model, None)

    def test_load_model_on_init(self):
        from PIL import Image
        from yolov5 import YOLOv5

        # init model
        model_path = TestConstants.YOLOV5S_MODEL_PATH
        device = "cpu"
        yolov5 = YOLOv5(model_path, device, load_on_init=True)

        # check if loaded
        self.assertNotEqual(yolov5.model, None)

    def test_predict(self):
        from PIL import Image
        from yolov5 import YOLOv5

        # init yolov5s model
        model_path = TestConstants.YOLOV5S_MODEL_PATH
        device = "cpu"
        yolov5 = YOLOv5(model_path, device, load_on_init=True)

        # prepare image
        image_path = TestConstants.ZIDANE_IMAGE_PATH
        image = Image.open(image_path)

        # perform inference
        results = yolov5.predict(image, size=640, augment=False)

        # compare
        self.assertEqual(results.n, 1)
        self.assertEqual(len(results.names), 80)
        self.assertEqual(len(results.pred[0]), 4)
        
        # prepare image
        image = image_path

        # perform inference
        results = yolov5.predict(image, size=640, augment=False)

        # compare
        self.assertEqual(results.n, 1)
        self.assertEqual(len(results.names), 80)
        self.assertEqual(len(results.pred[0]), 4)
        
        # init yolov5l model
        model_path = TestConstants.YOLOV5L_MODEL_PATH
        device = "cpu"
        yolov5 = YOLOv5(model_path, device, load_on_init=True)

        # prepare image
        image_path = TestConstants.BUS_IMAGE_PATH
        image = Image.open(image_path)
        # perform inference
        results = yolov5.predict(image, size=1280, augment=False)

        # compare
        self.assertEqual(results.n, 1)
        self.assertEqual(len(results.names), 80)
        self.assertEqual(len(results.pred[0]), 8)
        
        # prepare image
        image = image_path

        # perform inference
        results = yolov5.predict(image, size=1280, augment=False)

        # compare
        self.assertEqual(results.n, 1)
        self.assertEqual(len(results.names), 80)
        self.assertEqual(len(results.pred[0]), 8)

        # init yolov5s model
        model_path = TestConstants.YOLOV5S_MODEL_PATH
        device = "cpu"
        yolov5 = YOLOv5(model_path, device, load_on_init=True)

        # prepare images
        image_path1 = TestConstants.ZIDANE_IMAGE_PATH
        image_path2 = TestConstants.BUS_IMAGE_PATH
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)

        # perform inference with multiple images and test augmentation
        results = yolov5.predict([image1, image2], size=1280, augment=True)

        # compare
        self.assertEqual(results.n, 2)
        self.assertEqual(len(results.names), 80)
        self.assertEqual(len(results.pred[0]), 4)
        self.assertEqual(len(results.pred[1]), 8)

        # prepare image
        image_path1 = TestConstants.ZIDANE_IMAGE_PATH
        image_path2 = TestConstants.BUS_IMAGE_PATH
        image1 = image_path1
        image2 = image_path2

        # perform inference
        results = yolov5.predict([image1, image2], size=1280, augment=True)

        # compare
        self.assertEqual(results.n, 2)
        self.assertEqual(len(results.names), 80)
        self.assertEqual(len(results.pred[0]), 4)
        self.assertEqual(len(results.pred[1]), 8)
        



if __name__ == "__main__":
    unittest.main()
