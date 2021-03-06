from pytensor.ops.math_ops import *
from pytensor.ops.loss_ops import *
from pytensor.tutorial.part1.trainer import *
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


class LinearModel:

    def __init__(self, input_size, output_size):
        """
        a simple linear model: y = w*x

        :param input_size:
        :param output_size:
        """

        # initialize size
        self.input_size = input_size
        self.output_size = output_size

        # initialize parameters
        self.parameter = Parameter()
        self.W = self.parameter.get_tensor('weight', [self.input_size, self.output_size])

        # ops and loss
        self.matmul = Matmul()
        self.loss_ops = SoftmaxLoss()

    def forward(self, input_tensor):
        output_tensor = self.matmul.forward([input_tensor, self.W])
        self.loss_ops.forward(output_tensor)

        return output_tensor

    def loss(self, target_tensor):
        loss_val = self.loss_ops.loss(target_tensor)
        return loss_val

    def backward(self):
        self.loss_ops.backward()
        self.matmul.backward()


if __name__ == '__main__':

    digits = load_digits()
    digits.data /= 16.0
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target)

    model = LinearModel(64, 10)
    trainer = Trainer(model)
    trainer.train(x_train, y_train, x_test, y_test)