from controllers.productControllers import GetProductsController, SearchProductByIdController, DeleteProductByIdController, PutProductByIdController, PostProductController, PostBuyProductController
from controllers.informationController import MainInformationController, AboutInformationController, GetProductsInformationController
from controllers.cartControllers import GetCartsController, PostCartsCheckoutController

menu = {
        "1": MainInformationController,
        "1_1": GetProductsInformationController,
        "1_1_1": GetProductsController,
        "1_1_2": SearchProductByIdController,
        "1_2": PostProductController,
        "1_3": PutProductByIdController,
        "1_4": DeleteProductByIdController,
        "1_5": PostBuyProductController,
        "1_6": GetCartsController,
        "1_7": PostCartsCheckoutController,
        "1_99": AboutInformationController,
}