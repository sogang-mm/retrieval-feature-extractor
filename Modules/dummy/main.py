import os
from Modules.dummy.example import test

class Dummy:
    model = None
    result = None
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        # TODO
        #   - initialize and load model here
        model_path = os.path.join(self.path, "model.txt")
        self.model = open(model_path, "r")

    def inference_by_path(self, image_path):
        result = []
        # TODO
        #   - Inference using image path
        import time
        time.sleep(2)
        result = [{'CONV': b"TEST", 'FC': b"DEBUG"}, {'CONV': b"TEST", 'FC': b"DEBUG"}]
        self.result = result

        return self.result
